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
