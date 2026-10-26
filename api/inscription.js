// Relais entre les formulaires du site et Brevo. La clé reste côté serveur (variable d'environnement Vercel).
// Variables à renseigner dans Vercel : BREVO_API_KEY, BREVO_LISTE_ALERTES, BREVO_LISTE_PROGRAMMATEURS
const API = 'https://api.brevo.com/v3';
const EMAIL_OK = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const propre = (v, max = 120) => String(v || '').trim().slice(0, max);

async function brevo(chemin, corps) {
  const r = await fetch(API + chemin, {
    method: 'POST',
    headers: { 'api-key': process.env.BREVO_API_KEY, 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify(corps),
  });
  return r;
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ ok: false });
  if (!process.env.BREVO_API_KEY) return res.status(503).json({ ok: false, erreur: 'non-configure' });
  let d = req.body || {};
  if (typeof d === 'string') { try { d = JSON.parse(d); } catch { d = {}; } }
  if (d.site) return res.status(200).json({ ok: true }); // champ piège anti-robots
  const email = propre(d.email, 160).toLowerCase();
  if (!EMAIL_OK.test(email)) return res.status(400).json({ ok: false, erreur: 'email' });

  const pro = d.type === 'programmateur';
  const liste = Number(pro ? process.env.BREVO_LISTE_PROGRAMMATEURS : process.env.BREVO_LISTE_ALERTES);
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
