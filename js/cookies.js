/* Bandeau cookies Sarah Prod.
   Le bandeau n'apparaît que si un outil de mesure est configuré ci-dessous.
   Aucun traceur n'est chargé avant l'accord du visiteur. Choix gardé 6 mois. */
(function () {
  var CONFIG = {
    ga4: "G-EVM16W30VM",      // identifiant Google Analytics, ex. "G-XXXXXXX"
    pixelMeta: ""   // identifiant du pixel Meta, ex. "1234567890"
  };
  var CLE = "sp-cookies", DUREE = 182 * 24 * 3600 * 1000;
  var actif = !!(CONFIG.ga4 || CONFIG.pixelMeta);

  function lire() { try { var c = JSON.parse(localStorage.getItem(CLE) || "null"); return c && Date.now() - c.t < DUREE ? c : null; } catch (e) { return null; } }
  function ecrire(ok) { try { localStorage.setItem(CLE, JSON.stringify({ ok: ok, t: Date.now() })); } catch (e) {} }

  function charger() {
    if (CONFIG.ga4) {
      var s = document.createElement("script"); s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + CONFIG.ga4; document.head.appendChild(s);
      window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); };
      gtag("js", new Date()); gtag("config", CONFIG.ga4, { linker: { domains: ["weezevent.com"] } });
    }
    if (CONFIG.pixelMeta) {
      !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0"; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); }(window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
      fbq("init", CONFIG.pixelMeta); fbq("track", "PageView");
    }
  }

  function bandeau() {
    if (document.getElementById("sp-cookies")) return;
    var d = document.createElement("div"); d.id = "sp-cookies"; d.setAttribute("role", "dialog"); d.setAttribute("aria-label", "Cookies");
    d.innerHTML = '<p>Nous utilisons des cookies de mesure d\'audience et de publicité pour savoir comment le site est utilisé et mesurer nos campagnes. Vous pouvez accepter ou refuser. <a href="/confidentialite#cookies">En savoir plus</a></p>' +
      '<div><button type="button" data-c="0">Tout refuser</button><button type="button" data-c="1">Tout accepter</button></div>';
    var st = document.createElement("style");
    st.textContent = "#sp-cookies{position:fixed;left:16px;right:16px;bottom:16px;z-index:999;max-width:720px;margin:0 auto;background:#0B0726;color:#fff;border:2px solid #5B3CD5;padding:18px 20px;display:flex;gap:16px;align-items:center;flex-wrap:wrap;font:500 14.5px/1.5 'Schibsted Grotesk',system-ui,sans-serif;box-shadow:0 18px 40px rgba(0,0,0,.4)}#sp-cookies p{margin:0;flex:1 1 320px}#sp-cookies a{color:#FCDE02;font-weight:700}#sp-cookies div{display:flex;gap:10px}#sp-cookies button{font:inherit;font-weight:800;padding:11px 18px;border:2px solid #FCDE02;cursor:pointer;background:none;color:#FCDE02}#sp-cookies button[data-c='1']{background:#FCDE02;color:#0B0726}";
    document.head.appendChild(st); document.body.appendChild(d);
    d.addEventListener("click", function (e) {
      var c = e.target.getAttribute && e.target.getAttribute("data-c"); if (c === null) return;
      ecrire(c === "1"); d.remove(); if (c === "1") charger();
    });
  }

  window.spCookies = { ouvrir: function () { if (actif) bandeau(); else location.href = "/confidentialite#cookies"; } };
  if (!actif) return;
  var choix = lire();
  if (choix && choix.ok) charger();
  else if (!choix) { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", bandeau); else bandeau(); }
})();
