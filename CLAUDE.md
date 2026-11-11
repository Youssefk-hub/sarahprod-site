# Site sarahprod.com : consignes pour Claude

Site statique (HTML, CSS, JS) hébergé sur Vercel. Chaque push sur la branche `main` met le site en ligne automatiquement en 1 à 2 minutes. Il n'y a rien à installer.

## Où se trouve quoi

- `index.html` : accueil (liste de toutes les dates, mur d'affiches, historique).
- `spectacle/*.html` : une page par spectacle. Ces pages sont générées, ne pas les modifier à la main.
- `outils/gen_spectacles.py` : le générateur. Il contient les textes des spectacles, leurs dates (`SPECTACLES[...]["dates"]`) et les liens de billetterie (`LIENS` pour un lien propre à une date, `BILLETTERIE` pour le lien par spectacle).
- `donnees/dates-horaires.csv` : heures et pays des représentations.
- `images/`, `videos/`, `css/`, `js/` : ressources. `js/cookies.js` porte GA4, le pixel Meta et la mesure des clics « Acheter un billet ».
- `sitemap.xml`, `robots.txt`, `llms.txt` : référencement Google et IA.

## Modifier une date, un lien ou un texte de spectacle

1. Modifier `outils/gen_spectacles.py`.
2. Lancer `python3 outils/gen_spectacles.py` depuis la racine du dépôt : il réécrit les pages spectacles et la liste des dates de l'accueil.
3. Vérifier avec `git diff` que seul ce qui était demandé a changé.
4. Commit, puis push sur `main`.

Les autres pages (accueil hors dates, qui-sommes-nous, contact, programmateurs, mentions) se modifient directement dans leur fichier HTML.

## Règles à respecter

- Billetterie : aucun lien Weezevent. Chaque date renvoie vers le site de vente officiel (Ticketmaster, Leclerc Billetterie, France Billet, Fnac, billetterie de la salle).
- Pas de mention interne visible sur le site (« À compléter », « À brancher », notes de travail).
- Ne rien inventer : dates, salles, prix, distributions et chiffres viennent de la prod.
- Garder la direction artistique : violet #5B3CD5, nuit #0B0726, jaune #FCDE02, titres en Antonio, texte en Source Sans 3.
- Pubs Meta : lien d'arrivée `https://sarahprod.com/spectacle/<spectacle>?ville=<ville>&utm_source=meta&utm_medium=paid_social&utm_campaign=<campagne>&utm_content=<ville>`. Le paramètre `ville` fait descendre la page sur la date et affiche la barre « Acheter un billet ».
- Mettre à jour la date `<lastmod>` du sitemap quand une page change beaucoup.
