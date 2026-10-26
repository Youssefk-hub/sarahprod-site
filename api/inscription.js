// Relais entre les formulaires du site et Brevo. La clé reste côté serveur (variable d'environnement Vercel).
// Variables à renseigner dans Vercel : BREVO_API_KEY, BREVO_LISTE_ALERTES, BREVO_LISTE_PROGRAMMATEURS
const API = 'https://api.brevo.com/v3';
// lit les variables sans tenir compte des majuscules/minuscules
const env = (...noms) => { for (const n of noms) { const k = Object.keys(process.env).find(x => x.toUpperCase() === n); if (k && process.env[k]) return process.env[k].trim(); } return ''; };
const CLE = () => env('BREVO_API_KEY');
const num = v => Number((String(v).match(/\d+/) || [0])[0]) || 0; // accepte « 3 », « #3 »…
const LISTE_ALERTES = () => num(env('BREVO_LISTE_ALERTES', 'BREVO_LISTE_CLIENTS'));
const LISTE_PRO = () => num(env('BREVO_LISTE_PROGRAMMATEURS'));
const EMAIL_OK = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const propre = (v, max = 120) => String(v || '').trim().slice(0, max);

async function brevo(chemin, corps) {
  const r = await fetch(API + chemin, {
    method: 'POST',
    headers: { 'api-key': CLE(), 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify(corps),
  });
  return r;
}

module.exports = async (req, res) => {
  if (req.method === 'GET') { // vérification de la configuration, sans rien révéler
    const etat = { cle: !!CLE(), liste_alertes: LISTE_ALERTES() || null, liste_programmateurs: LISTE_PRO() || null };
    if (etat.cle) {
      const r = await fetch(API + '/contacts/lists?limit=50', { headers: { 'api-key': CLE(), Accept: 'application/json' } }).catch(() => null);
      etat.brevo = r ? r.status : 'injoignable';
      if (r && r.ok) { const j = await r.json(); etat.listes_brevo = (j.lists || []).map(l => ({ id: l.id, nom: l.name })); }
      else if (r) { etat.message = ((await r.json().catch(() => ({}))).message || '').slice(0, 160); }
    }
    return res.status(200).json(etat);
  }
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  if (!CLE()) return res.status(503).json({ ok: false, erreur: 'non-configure' });
  let d = req.body || {};
  if (typeof d === 'string') { try { d = JSON.parse(d); } catch { d = {}; } }
  if (d.site) return res.status(200).json({ ok: true }); // champ piège anti-robots
  const email = propre(d.email, 160).toLowerCase();
  if (!EMAIL_OK.test(email)) return res.status(400).json({ ok: false, erreur: 'email' });

  const pro = d.type === 'programmateur';
  const liste = pro ? LISTE_PRO() : LISTE_ALERTES();
  const attributs = {};
  if (d.ville) attributs.VILLE = propre(d.ville, 80);
  if (d.nom) attributs.NOM = propre(d.nom, 80);
  if (d.prenom) attributs.PRENOM = propre(d.prenom, 80);
  if (d.source) attributs.SOURCE = propre(d.source, 80);

  // crée les champs VILLE et SOURCE s'ils n'existent pas encore (erreur ignorée s'ils existent)
  await Promise.all(['VILLE', 'SOURCE'].map(n => brevo('/contacts/attributes/normal/' + n, { type: 'text' }).catch(() => {})));

  const r = await brevo('/contacts', { email, attributes: attributs, listIds: liste ? [liste] : [], updateEnabled: true });
  if (!r.ok && r.status !== 204) {
    const t = await r.text().catch(() => '');
    console.error('Brevo', r.status, t);
    return res.status(502).json({ ok: false });
  }

  if (pro) { // prévient Serge à chaque nouveau programmateur
    await brevo('/smtp/email', {
      sender: { name: 'Site Sarah Prod', email: 'infosarahproductions@gmail.com' },
      to: [{ email: 'infosarahproductions@gmail.com' }],
      replyTo: { email },
      subject: `Nouveau programmateur : ${attributs.PRENOM || ''} ${attributs.NOM || ''}`.trim(),
      textContent: `${attributs.PRENOM || ''} ${attributs.NOM || ''}\n${email}\n\nIl a accédé aux fiches techniques et dossiers de presse sur sarahprod.com/programmateurs.`,
    }).catch(() => {});
  }
  return res.status(200).json({ ok: true });
};
