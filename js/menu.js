/* Menu téléphone : bouton « Menu » qui déplie la navigation */
(function () {
  function init() {
    var nav = document.querySelector('header.nav'); if (!nav) return;
    var menu = nav.querySelector('.menu'); if (!menu || nav.querySelector('.burger')) return;
    menu.id = menu.id || 'menu-principal';
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'burger'; b.setAttribute('aria-expanded', 'false'); b.setAttribute('aria-controls', menu.id);
    b.innerHTML = '<span aria-hidden="true"></span><span aria-hidden="true"></span><span aria-hidden="true"></span><b>Menu</b>';
    nav.appendChild(b);
    b.addEventListener('click', function () {
      var o = nav.classList.toggle('ouvert'); b.setAttribute('aria-expanded', o ? 'true' : 'false');
    });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) { nav.classList.remove('ouvert'); b.setAttribute('aria-expanded', 'false'); } });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

/* Arrivée depuis une pub : /spectacle/flashdance?ville=evry
   → la page descend sur la date de la ville, la met en avant, et une barre « Acheter un billet » reste visible en bas. */
(function () {
  var q = new URLSearchParams(location.search).get('ville'); if (!q) return;
  function n(s) { return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); }
  function init() {
    var rows = [].slice.call(document.querySelectorAll('.d[data-ville]'));
    var r = rows.filter(function (x) { return n(x.getAttribute('data-ville')) === n(q); })[0]; if (!r) return;
    var st = document.createElement('style');
    st.textContent = '.d.cible{outline:4px solid #FCDE02;outline-offset:3px;position:relative;z-index:1}' +
      '#sp-cible{position:fixed;left:12px;right:12px;bottom:12px;z-index:998;max-width:640px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:14px;background:#FCDE02;color:#0B0726;padding:14px 18px;text-decoration:none;font:800 16px/1.2 "Source Sans 3",system-ui,sans-serif;box-shadow:0 10px 0 rgba(11,7,38,.3)}' +
      '#sp-cible b{font-family:Antonio,sans-serif;font-size:22px;text-transform:uppercase;letter-spacing:.01em}#sp-cible span{white-space:nowrap}';
    document.head.appendChild(st);
    r.classList.add('cible');
    var mois = r.previousElementSibling; while (mois && !mois.classList.contains('mois')) mois = mois.previousElementSibling;
    var jour = r.querySelector('.jour'), j = jour && jour.firstChild ? jour.firstChild.textContent.trim() : '';
    var m = mois ? mois.firstChild.textContent.trim() : '';
    setTimeout(function () { r.scrollIntoView({ block: 'center' }); }, 60);
    if (!r.href) return;
    var a = document.createElement('a'); a.id = 'sp-cible'; a.href = r.href; a.target = '_blank'; a.rel = 'noopener';
    var s = location.pathname.match(/\/spectacle\/([^\/?#.]+)/);
    if (s) a.setAttribute('data-s', s[1]); a.setAttribute('data-ville', r.getAttribute('data-ville'));
    a.innerHTML = '<b>' + r.getAttribute('data-ville') + ' · ' + j + ' ' + m + '</b><span>Acheter un billet →</span>';
    document.body.appendChild(a);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
