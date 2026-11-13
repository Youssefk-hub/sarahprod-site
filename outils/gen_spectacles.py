"""Génère les pages spectacles du site Sarah Prod à partir des données ci-dessous.
Usage, depuis la racine du dépôt : python3 outils/gen_spectacles.py
"""
import sys, html, os

SITE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = lambda s: html.escape(s, quote=True)
AC = '<span class="a-completer">À compléter</span>'

TOUS = [  # slug, titre court, catégorie, couleurs de secours
    ("grease", "Grease Is The Word", "Comédie musicale", "#7A1F1F", "#D94F2B"),
    ("flashdance", "Flashdance The Musical", "Comédie musicale", "#5B1B5E", "#E0457B"),
    ("dirty-dancing", "Dirty Dancing Tribute Concert", "Concert hommage", "#1E3A5F", "#C98A3C"),
    ("sardou", "Générations Connemara - Tribute Michel Sardou", "Concert hommage", "#1F4034", "#8FBF6A"),
    ("mamma-mia", "Mama Mia ! Célébration ABBA", "Concert hommage", "#2B2170", "#F2C14E"),
    ("gitans", "Gitan(s) Le Musical", "Comédie musicale", "#6B2414", "#E0A030"),
    ("jungle-book", "Le Livre de la Jungle le Musical", "Spectacle familial", "#1F4034", "#8FBF6A"),
    ("cendrillon", "Cendrillon Le Musical", "Spectacle familial", "#4B2A6B", "#C9A2E0"),
    ("aladin", "Aladin Le Musical", "Spectacle familial", "#1B3A6B", "#E8B23A"),
    ("petite-sirene", "La Petite Sirène le Musical", "Spectacle familial", "#0E3A52", "#45C4C0"),
    ("pinocchio", "Pinocchio Le Voyage Musical", "Spectacle familial", "#6B3410", "#E0A030"),
]

MOIS = {"01": "janv", "02": "fév", "03": "mars", "04": "avr", "05": "mai", "06": "juin",
        "07": "juil", "08": "août", "09": "sept", "10": "oct", "11": "nov", "12": "déc"}
MOIS_LONG = {"01": "Janvier", "02": "Février", "03": "Mars", "04": "Avril", "05": "Mai", "06": "Juin",
             "07": "Juillet", "08": "Août", "09": "Septembre", "10": "Octobre", "11": "Novembre", "12": "Décembre"}

SPECTACLES = {
 "grease": dict(
    titre="Grease Is The Word", t1="Grease", t2="Is The Word", cat="Comédie musicale",
    seo_title="Grease Is The Word, comédie musicale en tournée | Sarah Prod",
    seo_desc="Grease Is The Word, le spectacle rock'n'roll des années 50 en tournée en novembre 2026 : Liège, Mons, Saint-Quentin, Compiègne. Réservez vos billets.",
    accroche="Replongez dans l'univers électrisant des années 50 ! Rock'n'roll, romance et rébellion se mêlent dans ce spectacle culte qui fait vibrer toutes les générations.",
    infos=[("4", "dates"), ("NOVEMBRE", "2026"), ("2", "pays : France et Belgique")],
    texte=["Replongez dans l'univers électrisant des années 50 !",
           "Rock'n'roll, romance et rébellion se mêlent dans ce spectacle culte qui fait vibrer toutes les générations.",
           "Des chorégraphies endiablées, des tubes inoubliables et une énergie contagieuse."],
    fiche=[("Genre", "Comédie musicale"), ("Tournée", "Novembre 2026"), ("Pays", "France, Belgique"),
           ("Durée", AC), ("Distribution", AC), ("Tarifs", AC)],
    dates=[('13/11/26', 'Liège', 'Le Forum', 'Belgique'),
           ('14/11/26', 'Mons', 'Théâtre Royal', 'Belgique'),
           ('27/11/26', 'Saint-Quentin', 'Le Splendid', 'France'),
           ('28/11/26', 'Compiègne', 'Le Tigre', 'France')],
    fond="fond.jpg", fond_pos="center 55%",
    video="/videos/grease-teaser.mp4", poster="photo-10.jpg",
    grandes=[(10, "Danny et Sandy au bal"), (8, "Portée devant le décor de Rydell School"), (13, "La troupe au salut"),
             (11, "Sandy en cuir noir"), (12, "Les T-Birds"), (14, "La troupe en coulisses"), (9, "Les T-Birds au garage")],
    vignettes=list(range(1, 8)),
    credit="Certaines photos : crédit Bureau France pour La République des Pyrénées.",
    final_titre="Grease passe près de chez vous",
    final_texte="Quatre soirs en novembre 2026, à Liège, Mons, Saint-Quentin et Compiègne.",
 ),
 "flashdance": dict(
    titre="Flashdance The Musical", t1="Flashdance", t2="The Musical", cat="Comédie musicale",
    seo_title="Flashdance The Musical, tournée 2027 | Sarah Prod",
    seo_desc="Flashdance The Musical : 40e anniversaire du film, plus de 18 artistes et les hits des années 80. 34 dates en France de janvier à avril 2027.",
    accroche="Célébrant son 40e anniversaire, le phénomène du film à succès Flashdance revient sur scène au Casino de Paris puis en tournée dans toutes les villes de France !",
    infos=[("34", "représentations"), ("JANVIER - AVRIL", "2027"), ("18+", "artistes sur scène")],
    texte=["Une comédie musicale avec une bande son qui comprend les plus grands hits dance des années 80.",
           "Le spectacle Flashdance raconte l'histoire inoubliable d'Alex, ouvrière dans une aciérie de Pittsburgh le jour, et danseuse dans un bar la nuit, rêvant de devenir un jour une star de la danse.",
           "Quand une romance avec son patron à l'usine, menace de compliquer ses ambitions, Alex apprend la signification de l'amour et se sert de son talent afin de réaliser son rêve.",
           "Retrouvez sur scène plus de 18 artistes qui vous feront danser sur les plus grands titres tels que « What a Feeling », « Maniac », « Gloria », « Manhunt », « I Love Rock & Roll », « Cameleon Girls »..."],
    fiche=[("Genre", "Comédie musicale"), ("Tournée", "Janvier à avril 2027"), ("Pays", "France"),
           ("Sur scène", "Plus de 18 artistes"), ("Durée", AC), ("Tarifs", AC)],
    dates=[('29/01/27', 'Évry', "L'Agora", ''),
           ('31/01/27', 'Clermont-Ferrand', 'Zénith', ''),
           ('05/02/27', 'Toulon', 'Zénith', ''),
           ('06/02/27', 'Montpellier', 'Zénith', ''),
           ('07/02/27', 'Toulouse', 'Casino · 14h30', ''),
           ('07/02/27', 'Toulouse', 'Casino · 18h00', ''),
           ('12/02/27', 'Montélimar', 'Palais des Congrès', ''),
           ('13/02/27', 'Mâcon', 'Le Spot', ''),
           ('14/02/27', 'Bordeaux', 'Arkéa Arena', ''),
           ('18/02/27', 'Lille', 'Palais des Congrès', ''),
           ('19/02/27', 'Beauvais', 'Elispace', ''),
           ('20/02/27', 'Saint-Omer', 'Scénéo', ''),
           ('21/02/27', 'Compiègne', 'Le Tigre', ''),
           ('26/02/27', 'Rennes', 'Le Liberté', ''),
           ('28/02/27', 'Nantes', 'Zénith', ''),
           ('06/03/27', 'Orléans', 'Zénith', ''),
           ('07/03/27', 'Paris', 'Salle Pleyel', ''),
           ('18/03/27', 'Strasbourg', 'Zénith', ''),
           ('19/03/27', 'Dunkerque', 'Kursaal', ''),
           ('20/03/27', 'Amnéville', 'Galaxie', ''),
           ('27/03/27', 'Enghien-les-Bains', 'Casino', ''),
           ('28/03/27', 'Le Touquet', 'Casino', ''),
           ('01/04/27', 'Brest', 'Zénith', ''),
           ('02/04/27', 'Mouilleron-le-Captif', 'Vendéespace', ''),
           ('03/04/27', 'Niort', "L'Acclameur", ''),
           ('04/04/27', 'Caen', 'Zénith', ''),
           ('10/04/27', 'Nice', 'Nikaïa', ''),
           ('11/04/27', 'Marseille', 'Le Dôme', ''),
           ('15/04/27', 'Grenoble', 'Auditorium', ''),
           ('16/04/27', 'Lyon', 'Amphithéâtre', ''),
           ('17/04/27', 'Saint-Étienne', 'Zénith', ''),
           ('18/04/27', 'Annecy', 'Arcadium', ''),
           ('23/04/27', 'Roanne', 'Le Scarabée', ''),
           ('25/04/27', 'Biarritz', 'Gare du Midi', '')],
    fond="photo-02.jpg", fond_pos="38% 50%",
    video="/videos/flashdance-teaser.mp4", poster="photo-01.jpg",
    grandes=[(1, "La troupe en bleus de travail à l'aciérie"), (2, "Alex sous la pluie, sur sa chaise"), (4, "L'audition devant le jury"),
             (6, "Alex chante"), (5, "Le grand saut de l'audition"), (3, "Tableau dans la fumée rose"), (7, "Chorégraphie autour du lit")],
    vignettes=[],
    credit="Photos de scène prises au Zénith de Toulon, signées par le photographe.",
    final_titre="Flashdance passe près de chez vous",
    final_texte="34 représentations de janvier à avril 2027, d'Évry à Biarritz.",
 ),
 "dirty-dancing": dict(
    titre="Dirty Dancing Tribute Concert", t1="Dirty Dancing", t2="Tribute Concert", cat="Concert hommage",
    seo_title="Dirty Dancing Tribute Concert, tournée 2027 | Sarah Prod",
    seo_desc="Dirty Dancing Tribute Concert : les chansons culte du film en live avec band, choristes et danseurs. 10 dates de janvier à avril 2027.",
    accroche="Basé sur les musiques du film Dirty Dancing sorti il y a plus de 38 ans, la tournée 26/27 passera par plus de 30 villes, dans toute la France ainsi qu'en Suisse et en Belgique.",
    infos=[("10", "dates annoncées"), ("JANVIER - AVRIL", "2027"), ("LIVE", "band, choristes et danseurs")],
    texte=["L'intrigue se déroule à l'été 1963. Baby Houseman (Jennifer Grey) et sa famille passent des vacances au Kellerman's, une magnifique station balnéaire des Catskills.",
           "Intriguée par le professeur de danse de l'équipe, Johnny Castle (Patrick Swayze), et par le mode de vie très différent des autres, Baby apprend à danser tout en s'amusant et en tombant amoureuse. Un été qu'elle n'oubliera jamais !",
           "À sa sortie en 1987, le film fut un véritable phénomène au box-office international et a donné naissance à une bande originale de deux albums platine et à de nombreux singles, dont \"(I've Had) The Time of My Life\".",
           "Magnifique expérience que celle du Dirty Dancing Le Tribute Concert avec la Song List des chansons culte qui ont marqué plusieurs générations. Le spectacle accompagnera un band de chanteurs, choristes et danseurs interprétant en live la plupart des titres ayant fait le succès du film.",
           "Pendant le spectacle plusieurs passages permettront une interaction avec le public ou celui-ci sera invité à chanter et danser avec la troupe. Un véritable show sur scène et en salle.",
           "Dirty Dancing Le Tribute Concert, une soirée exceptionnelle à ne pas rater. Un classique pour toutes les générations."],
    fiche=[("Genre", "Concert hommage"), ("Tournée", "Janvier à avril 2027"), ("Pays", "France"),
           ("Sur scène", "Band, chanteurs, choristes et danseurs en live"), ("Durée", AC), ("Tarifs", AC)],
    dates=[('30/01/27', 'Melun', "L'Escale", ''),
           ('06/02/27', 'Sanary-sur-Mer', 'Galli', ''),
           ('20/03/27', 'Péronne', 'Espace Mac Orlan', ''),
           ('21/03/27', 'Compiègne', 'Le Tigre', ''),
           ('02/04/27', 'Bordeaux', '', ''),
           ('03/04/27', 'Saint-Grégoire', 'EMC2', ''),
           ('08/04/27', 'Châteauneuf-sur-Isère', 'O Lac', ''),
           ('16/04/27', 'Beauvais', 'Elispace', ''),
           ('17/04/27', 'Arras', "Casino, La Grand'Scène", ''),
           ('18/04/27', 'Lille', 'Théâtre Sébastopol', '')],
    fond="photo-02.jpg", fond_pos="50% 35%",
    video="/videos/dirty-dancing-teaser.mp4", poster="photo-01.jpg", video_vertical=True,
    grandes=[(1, "Le band et les chanteurs sur scène, sous les projecteurs"), (2, "Le visuel du spectacle")],
    vignettes=[],
    credit="®, ™ & © 2022 Lions Gate Entertainment Inc. All rights reserved.",
    final_titre="Dirty Dancing passe près de chez vous",
    final_texte="10 dates de janvier à avril 2027, de Melun à Lille.",
 ),
 "sardou": dict(
    titre="Générations Connemara", t1="Générations", t2="Connemara", cat="Concert hommage",
    seo_title="Générations Connemara, hommage à Sardou | Sarah Prod",
    seo_desc="Générations Connemara : les chansons de Michel Sardou dans un concert spectaculaire. 37 dates en France et en Suisse, de janvier à avril 2028.",
    accroche="Un hommage grandiose à l'un des plus grands artistes français.",
    infos=[("37", "représentations"), ("JANVIER - AVRIL", "2028")],
    texte=["Un hommage grandiose à l'un des plus grands artistes français.",
           "Les chansons emblématiques de Michel Sardou reprises avec puissance et émotion dans un concert spectaculaire qui traverse les générations."],
    fiche=[("Genre", "Concert hommage à Michel Sardou"), ("Tournée", "Janvier à avril 2028"), ("Pays", "France, Suisse"),
           ("Durée", AC), ("Distribution", AC), ("Tarifs", AC)],
    dates=[('13/01/28', 'Évry', "L'Agora · avant-première", ''),
           ('14/01/28', 'Saint-Quentin', 'Le Splendid', ''),
           ('15/01/28', 'Lille', 'Théâtre Sébastopol', ''),
           ('16/01/28', 'Boulogne-sur-Mer', "L'Embarcadère", ''),
           ('22/01/28', 'Troyes', 'Le Cube', ''),
           ('23/01/28', 'Amiens', 'Zénith', ''),
           ('29/01/28', 'Mouilleron-le-Captif', 'Vendéespace', ''),
           ('30/01/28', 'Niort', "L'Acclameur", ''),
           ('12/02/28', 'Tours', 'Le Vinci, Palais des Congrès', ''),
           ('13/02/28', 'Poitiers', 'Palais des Congrès du Futuroscope', ''),
           ('18/02/28', 'Rennes', 'Le Liberté', ''),
           ('19/02/28', 'Saint-Brieuc', "L'Hermione", ''),
           ('25/02/28', 'Orléans', 'Zénith', ''),
           ('04/03/28', 'Le Mans', 'Le Forum', ''),
           ('05/03/28', 'Le Havre', 'Le Carré des Docks', ''),
           ('10/03/28', 'Avignon', 'Confluences', ''),
           ('11/03/28', 'Châteauneuf-sur-Isère', 'O Lac', ''),
           ('17/03/28', 'Pau', 'Zénith', ''),
           ('18/03/28', 'Bordeaux', 'Théâtre Fémina', ''),
           ('23/03/28', 'Bourg-en-Bresse', 'Ekinox', ''),
           ('24/03/28', 'Roanne', 'Le Scarabée', ''),
           ('25/03/28', 'Annecy', 'Arcadium', ''),
           ('26/03/28', 'Grenoble', 'Summum', ''),
           ('31/03/28', 'Montélimar', 'Palais des Congrès', ''),
           ('01/04/28', 'Lyon', 'Amphithéâtre', ''),
           ('02/04/28', 'Toulouse', 'Casino Barrière · séance 1', ''),
           ('02/04/28', 'Toulouse', 'Casino Barrière · séance 2', ''),
           ('07/04/28', 'Nice', 'Nikaïa', ''),
           ('08/04/28', 'Toulon', 'Zénith', ''),
           ('09/04/28', 'Marseille', 'Le Dôme', ''),
           ('15/04/28', 'Genève', '', 'Suisse'),
           ('20/04/28', 'Nantes', 'Zénith', ''),
           ('21/04/28', 'Caen', 'Zénith', ''),
           ('22/04/28', 'Rouen', 'Zénith', ''),
           ('23/04/28', 'Beauvais', 'Elispace', ''),
           ('28/04/28', 'Perpignan', 'Auditorium Charles Trenet', ''),
           ('29/04/28', 'Biarritz', 'Gare du Midi', '')],
    fond="fond.jpg", fond_pos="30% 50%",
    video="/videos/sardou-teaser.mp4", poster="poster.jpg",
    grandes=[], vignettes=[], credit="",
    final_titre="Générations Connemara passe près de chez vous",
    final_texte="37 représentations de janvier à avril 2028, d'Évry à Biarritz, et Genève.",
 ),
 "jungle-book": dict(
    titre="Le Livre de la Jungle le Musical", t1="Le Livre de la Jungle", t2="le Musical", cat="Spectacle familial",
    seo_title="Le Livre de la Jungle, Apollo Théâtre Paris | Sarah Prod",
    seo_desc="Le Livre de la Jungle le Musical : l'aventure de Mowgli dans un spectacle féerique pour toute la famille, à l'Apollo Théâtre Paris et en tournée.",
    accroche="L'aventure magique de Mowgli prend vie dans un spectacle féerique pour toute la famille.",
    infos=[("APOLLO", "Théâtre, Paris"), ("+", "en tournée")],
    texte=["L'aventure magique de Mowgli prend vie dans un spectacle féerique pour toute la famille.",
           "Des décors luxuriants, des costumes époustouflants et une mise en scène enchanteresse transportent petits et grands au cœur de la jungle."],
    fiche=[("Genre", "Spectacle familial"), ("Lieu", "Apollo Théâtre, Paris"), ("Tournée", "Dates à venir"),
           ("Durée", AC), ("Âge conseillé", AC), ("Tarifs", AC)],
    dates=[],
    salle_unique=("Apollo Théâtre", "Paris", "https://indiv.themisweb.fr/0512/fEventChoiceIsMade.aspx?idstructure=0512&idevent=622&ProfilALibe=PROMOLIVRE&ProfilAPass=NOPASSW"),
    fond="photo-01.jpg", fond_pos="30% 40%", h1_size="clamp(48px,6.4vw,98px)",
    video="/videos/jungle-book-teaser.mp4", poster="photo-03.jpg",
    grandes=[(1, "Mowgli et Baloo"), (3, "Le roi Louie et ses singes"), (8, "Mowgli et Bagheera"), (2, "La meute des loups recueille Mowgli"),
             (9, "Le roi Louie sur son trône"), (4, "Les lionnes autour de Mowgli et Baloo"), (6, "Shere Khan"), (10, "Kaa, le serpent"),
             (5, "Les loups en costume"), (7, "La danse des papillons")],
    vignettes=[], credit="",
    final_titre="Une sortie en famille au cœur de la jungle",
    final_texte="À l'Apollo Théâtre à Paris, puis en tournée. Les dates arrivent bientôt.",
 ),
 "cendrillon": dict(
    titre="Cendrillon Le Musical", t1="Cendrillon", t2="Le Musical", cat="Spectacle familial",
    seo_title="Cendrillon Le Musical, spectacle familial | Sarah Prod",
    seo_desc="Cendrillon Le Musical : un spectacle familial haut en couleurs, de magnifiques costumes et la Fée Toctoc. Bientôt en tournée.",
    accroche="Un spectacle haut en couleurs doté de magnifiques costumes et qui fera rêver toutes les générations.",
    infos=[("BIENTÔT", "en tournée")],
    texte=["Cendrillon, est une jeune fille laissée à la garde de sa belle-mère à la mort de son père. Bien que maltraitée par celle-ci, elle vit avec sa demi-sœur dans une masure dans la forêt entourée de personnages plus attachants les uns que les autres.",
           "Rentrant de la guerre, le jeune Prince doit trouver une épouse afin d'être couronné roi et c'est au cours d'un bal donné au château que celui-ci désignera sa promise.",
           "Toutes les jeunes filles du village se voient déjà sur le trône sauf Cendrillon mais c'est sans compter sur la Fée Toctoc qui veille sur elle.",
           "Ira-t-elle au bal ? Rencontrera-t-elle le Prince ? Sera-t-elle rentrée avant minuit ? La citrouille se transformera-t-elle en carrosse ?",
           "Un spectacle haut en couleurs doté de magnifiques costumes et qui fera rêver toutes les générations. Un grand saut dans l'univers des contes de fées."],
    fiche=[("Genre", "Spectacle familial"), ("Tournée", "Bientôt annoncée"), ("Durée", AC), ("Âge conseillé", AC), ("Tarifs", AC)],
    dates=[], bientot=True,
    fond="photo-01.jpg", fond_pos="45% 35%", h1_size="clamp(52px,7.6vw,120px)",
    video=None, poster=None,
    grandes=[(1, "Le bal au château"), (4, "Cendrillon et sa pantoufle"), (7, "Le Prince sur son trône"), (6, "La cour chante au château"),
             (2, "Au village"), (5, "Les demi-sœurs reviennent des courses"), (3, "Le bouquet de fleurs")],
    vignettes=[], credit="",
    final_titre="Cendrillon arrive bientôt près de chez vous",
    final_texte="Les premières dates de la tournée seront annoncées ici. Laissez votre email pour être prévenu en premier.",
 ),
 "aladin": dict(
    titre="Aladin Le Musical", t1="Aladin", t2="Le Musical", cat="Spectacle familial",
    seo_title="Aladin Le Musical, spectacle familial | Sarah Prod",
    seo_desc="Aladin Le Musical : la lampe magique, le génie Al et Shéhérazade dans une comédie musicale pour toute la famille. Bientôt en tournée.",
    accroche="Issue des 1001 Nuits, l'histoire d'Aladin nous transporte au cœur des trésors de l'Orient et de ses nombreux mystères.",
    infos=[("BIENTÔT", "en tournée")],
    texte=["Issue des 1001 Nuits, l'histoire d'Aladin nous transporte au cœur des trésors de l'Orient et de ses nombreux mystères.",
           "ALADIN, prince des voleurs, passe son temps dans les ruelles de la ville au grand dam de sa mère. Toujours à l'affût du moindre larcin, celui-ci croise un jour le chemin de MASTABAR, le grand vizir du royaume qui ne rêve que d'une chose : prendre le pouvoir de son maître, le Sultan, dont la seule préoccupation est de marier sa fille à un prince aussi riche que lui.",
           "MASTABAR tend un piège à ALADIN afin de récupérer la lampe magique qui lui permettra d'atteindre son but. Dans la grotte magique, le jeune homme trouve la lampe et, en frottant celle-ci par hasard, délivre le puissant génie AL, qui l'aidera par la suite à conquérir la belle SHÉHÉRAZADE, fille unique du sultan, et à vaincre les desseins maléfiques du diabolique vizir.",
           "« ALADIN » est une comédie musicale transportant toute la famille, grands comme petits, dans un monde de rêve et de magie… Cette merveilleuse histoire prend vie grâce aux artistes, parés de magnifiques costumes alliant sublimes chorégraphies et envoûtantes chansons."],
    fiche=[("Genre", "Comédie musicale familiale"), ("Tournée", "Bientôt annoncée"), ("Paroles et musique", "Bernard Poli"),
           ("Mise en scène et chorégraphies", "Jeanne Deschaux"), ("Effets spéciaux", "Dani Lary"), ("Durée", AC), ("Âge conseillé", AC)],
    dates=[], bientot=True,
    fond="photo-06.jpg", fond_pos="50% 50%", h1_size="clamp(52px,7.6vw,120px)",
    video=None, youtube="ur0AUEj7Ugo", poster="photo-04.jpg",
    grandes=[(6, "Le marché de la ville"), (4, "La grande danse au palais"), (3, "Le Sultan"), (1, "Aladin et la troupe"),
             (5, "Le génie Al"), (2, "Le génie en costume argenté")],
    vignettes=[], credit="",
    final_titre="Aladin arrive bientôt près de chez vous",
    final_texte="Les premières dates de la tournée seront annoncées ici. Laissez votre email pour être prévenu en premier.",
 ),
 "petite-sirene": dict(
    titre="La Petite Sirène le Musical", t1="La Petite Sirène", t2="le Musical", cat="Spectacle familial",
    seo_title="La Petite Sirène, comédie musicale familiale | Sarah Prod",
    seo_desc="La Petite Sirène le Musical : le conte d'Andersen en comédie musicale, 12 artistes sur scène, pour toute la famille. Bientôt en tournée.",
    accroche="La Petite Sirène, fille du Roi de la Mer, rêve de découvrir le monde des humains.",
    infos=[("DATES", "à venir"), ("12", "artistes sur scène")],
    texte=["La Petite Sirène, fille du Roi de la Mer, rêve de découvrir le monde des humains. Le jour de son 15e anniversaire elle monte à la surface de l'eau et observe émerveillée un navire en fête.",
           "Soudain une violente tempête éclate et le bateau sombre dans les fonds marins. Elle parvient à sauver un jeune et beau marin de la noyade dont elle tombe follement amoureuse.",
           "Pour rejoindre son amour sur terre elle fait appel à la terrible Bertha, sorcière de la mer, et sacrifie sa merveilleuse voix contre des jambes qui la rendront humaine. Parviendra-t-elle à séduire son bel amour malgré le sortilège de la sorcière ?",
           "Librement adapté de « La Petite Sirène », l'un des contes les plus connus de l'écrivain Hans Christian Andersen, l'histoire nous transporte au cœur du royaume des fonds marins.",
           "Une comédie musicale, jeune, moderne aux sonorités des plus grands spectacles. 12 artistes survitaminés qui feront danser et chanter sur une musique exceptionnelle."],
    fiche=[("Genre", "Comédie musicale familiale"), ("Sur scène", "12 artistes"), ("Musique", "Bernard Poli"),
           ("Livret et paroles", "Serge Tapierman"), ("Mise en scène et chorégraphies", "Jeanne Deschaux"),
           ("Orchestrations", "Bernard Poli et Gilles Simonet"), ("Durée", AC), ("Âge conseillé", AC)],
    dates=[], bientot=True,
    fond="photo-01.jpg", fond_pos="40% 40%", h1_size="clamp(48px,6.4vw,98px)",
    video=None, youtube="pUkRE1CeOkE", poster="photo-02.jpg",
    grandes=[(1, "La Petite Sirène et le marin"), (3, "La Petite Sirène"), (2, "Les sœurs de la Petite Sirène"),
             (4, "Le Roi de la Mer sur son trône"), (5, "Les créatures des fonds marins")],
    vignettes=[], credit="",
    final_titre="La Petite Sirène arrive bientôt près de chez vous",
    final_texte="Les premières dates de la tournée seront annoncées ici. Laissez votre email pour être prévenu en premier.",
 ),
 "pinocchio": dict(
    titre="Pinocchio Le Voyage Musical", t1="Pinocchio", t2="Le Voyage Musical", cat="Spectacle familial",
    seo_title="Pinocchio Le Voyage Musical, en famille | Sarah Prod",
    seo_desc="Pinocchio Le Voyage Musical : Gepetto, la Fée Bleue, le Chat et le Renard dans une comédie musicale familiale. Bientôt en tournée.",
    accroche="Il était une fois… un morceau de bois.",
    infos=[("DATES", "à venir")],
    texte=["Il était une fois… un morceau de bois. Gepetto, un pauvre menuisier, est triste de ne pas avoir eu d'enfant. Il décide de fabriquer un pantin à partir d'un morceau de bois qu'il nomme Pinocchio.",
           "Surprise ! Voilà qu'en pleine nuit la Fée Bleue arrive pour donner vie à la marionnette, qui va devenir vivante et dotée de la parole. Gepetto décide dès lors de l'élever comme son fils.",
           "Très vite, ce petit garçon désobéissant à son père, n'en faisant qu'à sa tête, partira seul à l'aventure de l'école de la vie. En chemin, il rencontre plusieurs personnages amicaux ou brigands — le Chat et le Renard, le Grillon… — qui lui feront vivre de merveilleuses aventures.",
           "Parviendra-t-il à devenir un vrai petit garçon ? Son souhait le plus cher…",
           "Librement adaptée des « Aventures de Pinocchio » de Carlo Collodi, cette comédie musicale prend vie grâce à une troupe d'artistes parés de costumes féeriques, alliant chorégraphies et chansons, évoluant dans de somptueux décors.",
           "Créé en décembre 2009 à l'Amphithéâtre de Lyon et au Zénith de Saint-Étienne, puis joué au théâtre de l'Alhambra à Paris d'octobre 2012 à mars 2013, ce classique intemporel repart aujourd'hui en tournée avec Sarah Prod."],
    fiche=[("Genre", "Comédie musicale familiale"), ("Musique et paroles", "Bernard Poli"), ("Mise en scène et chorégraphies", "Jeanne Deschaux"),
           ("Direction vocale", "Pierre-Yves Duchesne"), ("Costumes", "Edith Vesperini"), ("Décors", "Ludovic Layeux"),
           ("Durée", AC), ("Âge conseillé", AC)],
    dates=[], bientot=True,
    fond="photo-08.jpg", fond_pos="50% 60%", h1_size="clamp(48px,6.4vw,98px)",
    video="/videos/pinocchio-teaser.mp4", poster="photo-07.jpg",
    grandes=[(8, "Pinocchio et ses compagnons au village"), (2, "Pinocchio"), (7, "La Fée Bleue donne vie à Pinocchio"), (1, "Le Renard"),
             (6, "Pinocchio au cirque"), (3, "Le Chat"), (4, "Le Grillon"), (9, "Pinocchio sur le chemin de l'école"), (5, "Une marionnette du cirque")],
    vignettes=[], credit="",
    final_titre="Pinocchio arrive bientôt près de chez vous",
    final_texte="Les premières dates de la tournée seront annoncées ici. Laissez votre email pour être prévenu en premier.",
 ),
 "mamma-mia": dict(
    titre="Mama Mia ! Célébration ABBA", t1="Mama Mia !", t2="Célébration ABBA", cat="Concert hommage",
    seo_title="Mama Mia ! Célébration ABBA, création 2028 | Sarah Prod",
    seo_desc="Mama Mia ! Célébration ABBA : Dancing Queen, Waterloo, Super Trouper… un spectacle festif pour toute la famille. Nouvelle création 2028.",
    accroche="Une célébration explosive de l'un des groupes les plus iconiques de l'histoire de la musique pop.",
    infos=[("2028", "nouvelle création"), ("DATES", "à venir")],
    texte=["MAMA MIA ! Célébration ABBA, c'est une célébration explosive de l'un des groupes les plus iconiques de l'histoire de la musique pop.",
           "Revivez la magie des années 70 et 80 à travers les plus grands tubes qui ont fait danser le monde entier : Dancing Queen, Waterloo, Super Trouper, Fernando, The Winner Takes It All, Gimme! Gimme! Gimme!...",
           "Un spectacle coloré, festif et entraînant porté par des artistes talentueux qui rendent un vibrant hommage à ABBA. Costumes pailletés, mise en scène grandiose et énergie communicative garantie — un moment de pur bonheur pour toute la famille !"],
    fiche=[("Genre", "Concert hommage à ABBA"), ("Création", "2028"), ("Public", "Toute la famille"), ("Durée", AC), ("Tarifs", AC)],
    dates=[], bientot=True,
    fond="fond.jpg", fond_pos="55% 50%", h1_size="clamp(52px,7.6vw,120px)",
    video="/videos/mamma-mia-teaser.mp4", poster="poster.jpg",
    grandes=[], vignettes=[], credit="",
    final_titre="Mama Mia ! arrive en 2028",
    final_texte="Les premières dates seront annoncées ici. Laissez votre email pour être prévenu en premier.",
 ),
 "gitans": dict(
    titre="Gitan(s) Le Musical", t1="Gitan(s)", t2="Le Musical", cat="Comédie musicale",
    seo_title="Gitan(s) Le Musical, comédie musicale flamenco | Sarah Prod",
    seo_desc="Gitan(s) Le Musical : l'histoire de Tiago et de sa tribu, guitares, flamenco et plus de 15 artistes sur scène. Soyez prévenu des dates.",
    accroche="Plongez dans l'univers vibrant et passionné de GITAN(S) le Musical !",
    infos=[("15+", "artistes sur scène"), ("DATES", "à venir")],
    texte=["Plongez dans l'univers vibrant et passionné de GITAN(S) le Musical ! L'histoire de Tiago et de sa tribu, une communauté gitane fière de ses racines, de sa liberté et de ses traditions.",
           "Sur fond de guitares enflammées, de flamenco et de rythmes chaleureux, ce spectacle raconte l'amour, la fraternité, la transmission et la résistance d'un peuple qui refuse d'abandonner son identité.",
           "La Mame, gardienne de la mémoire, guide les siens à travers les épreuves avec sagesse et tendresse.",
           "Des chansons originales comme « Ven Ven Ven », « Santa Maria », « Caballeros » ou encore « Sans toi » vous transporteront dans un monde de passion et de poésie.",
           "Plus de 15 artistes sur scène — danseurs, guitaristes, chanteurs — pour un spectacle d'une puissance émotionnelle rare."],
    fiche=[("Genre", "Comédie musicale"), ("Diffusion", "Disponible à l'international"), ("Sur scène", "Plus de 15 artistes"),
           ("Mise en scène et chorégraphies", "Jeanne Deschaux"), ("Co-chorégraphe", "Sophie Murguet"), ("Durée", AC), ("Tarifs", AC)],
    dates=[], bientot=True,
    fond="photo-12.jpg", fond_pos="60% 50%",
    video="/videos/gitans-teaser.mp4", poster="photo-06.jpg",
    grandes=[(6, "La troupe chante"), (1, "Les danseuses de flamenco"), (2, "La procession dans la lumière"), (8, "Le mariage"),
             (3, "La tribu"), (7, "Autour du canapé"), (4, "Tiago et la Mame"), (5, "Le drame"), (9, "La fête"),
             (10, "Le deuil"), (11, "Sous le projecteur"), (12, "La danse et le balcon")],
    vignettes=[], credit="",
    final_titre="Gitan(s) arrive bientôt près de chez vous",
    final_texte="Les premières dates seront annoncées ici. Laissez votre email pour être prévenu en premier.",
 ),
}

CSS_LINK = '<link rel="stylesheet" href="/css/spectacle.css">\n<script src="/js/cookies.js" defer></script>\n<script src="/js/menu.js" defer></script>'
FONTS = '<link rel="preload" href="/fonts/antonio-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>\n<link rel="preload" href="/fonts/source-sans-3-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>\n<link rel="stylesheet" href="/css/fonts.css">'


import csv, json as _json, re as _re
LIENS = {
 # Liens d'achat directs par date (sites de vente officiels). Aucune date ne renvoie vers Weezevent.
 ("grease","Liège"):"https://go.utick.be/?pos=LEFORUM&s=C491F317-304E-7626-CB64-C1ED8CD8FC26",
 ("grease","Mons"):"https://www.ticketmaster.be/event/grease-is-the-word-billets/611530393?language=fr-be",
 ("grease","Saint-Quentin"):"https://www.fnacspectacles.com/event/grease-is-the-word-le-splendid-st-quentin-20180705/",
 ("grease","Compiègne"):"https://nuitsdartistes.trium.fr/fr/t/-/event/61019",
}
# Lien par spectacle repris de l'ancien site sarahprod.com (bouton « Acheter un billet »), utilisé quand une date n'a pas de lien Weezevent propre.
BILLETTERIE = {
 "grease": "https://www.ticketmaster.fr/fr/resultat?ipSearch=grease",
 "flashdance": "https://www.ticketmaster.fr/fr/artiste/flashdance/idartiste/751",
 "dirty-dancing": "https://www.leclercbilletterie.com/fr/artiste/dirty-dancing-tribute/idartiste/63220",
 "sardou": "https://www.francebillet.com/en/artist/generations-connemara-tribute-sardou/?inApp=true",
 "jungle-book": "https://www.ticketmaster.fr/fr/resultat?ipSearch=livre%20de%20la%20jungle",
}
def lien_de(slug, ville):
    return LIENS.get((slug, ville)) or BILLETTERIE.get(slug, "")
MOIS_NUM = {"janvier":1,"février":2,"mars":3,"avril":4,"mai":5,"juin":6,"juillet":7,"août":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12}
CSV_INFO = {}
try:
    for r in csv.DictReader(open(os.path.join(SITE, "donnees", "dates-horaires.csv"), encoding="utf-8"), delimiter=";"):
        _j, _m, _a = r["Date"].split()[1:4]
        cle = (f"{int(_j):02d}/{MOIS_NUM[_m]:02d}/{_a[2:]}", r["Ville"].strip())
        CSV_INFO[cle] = r
except FileNotFoundError:
    pass

def json_ld(slug, s):
    evts = []
    for d, ville, salle, pays in s["dates"]:
        j, m, a = d.split("/")
        info = CSV_INFO.get((d, ville), {})
        h = _re.fullmatch(r"(\d{1,2})h(\d{2})", (info.get("Heure") or "").strip())
        debut = f"20{a}-{m}-{j}" + (f"T{int(h.group(1)):02d}:{h.group(2)}:00{'+01:00' if int(m) in (1,2,3,11,12) or (int(m)==10 and int(j)>25) else '+02:00'}" if h else "")
        pays_ = pays or info.get("Pays") or ""
        lieu = {"@type": "Place", "name": salle.split(" · ")[0] or ville,
                "address": {"@type": "PostalAddress", "addressLocality": ville, **({"addressCountry": {"France":"FR","Belgique":"BE","Suisse":"CH","Luxembourg":"LU"}.get(pays_, pays_)} if pays_ else {})}}
        e = {"@type": "Event", "name": f"{s['titre']} à {ville}", "startDate": debut,
             "eventStatus": "https://schema.org/EventScheduled",
             "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
             "location": lieu, "description": s["seo_desc"],
             "organizer": {"@type": "Organization", "name": "Sarah Prod", "url": "https://sarahprod.com/"},
             "url": f"https://sarahprod.com/spectacle/{slug}"}
        if s.get("fond"): e["image"] = [f"https://sarahprod.com/images/{slug}/{s['fond']}"]
        lien = lien_de(slug, ville)
        if lien: e["offers"] = {"@type": "Offer", "url": lien, "availability": "https://schema.org/InStock",
                                "priceCurrency": "CHF" if pays_ == "Suisse" else "EUR"}
        evts.append(e)
    if not evts: return ""
    return '<script type="application/ld+json">' + _json.dumps({"@context": "https://schema.org", "@graph": evts}, ensure_ascii=False) + '</script>'

import datetime as _dt
JOURS = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
def orientation(chemin):
    try:
        from PIL import Image
        with Image.open(chemin) as im: w, h = im.size
        return "portrait" if h > w * 1.05 else "paysage"
    except Exception:
        return "paysage"

def disposition_photos(photos, dossier):
    """Range les photos dans une grille de 6 colonnes sans trou.
    Renvoie [(n, alt, classe)]. Les photos verticales vont dans des cases hautes."""
    n = len(photos)
    if n == 0: return []
    ori = {p[0]: orientation(os.path.join(dossier, f"photo-{p[0]:02d}.jpg")) for p in photos}
    if n == 1: return [(photos[0][0], photos[0][1], "plein")]
    if n == 2: return [(a, b, "moitie haute") for a, b in photos]
    tete = photos[0]
    verticales = [p for p in photos[1:] if ori[p[0]] == "portrait"]
    reste = [p for p in photos[1:] if p not in verticales[:1]]
    out = [(tete[0], tete[1], "grande")]
    if verticales:                       # une verticale à côté de la grande, en case haute
        v = verticales[0]; out.append((v[0], v[1], "haute"))
    else:
        out += [(p[0], p[1], "") for p in reste[:2]]; reste = reste[2:]
    # les autres verticales passent en cases simples ; les cases larges reçoivent des horizontales
    r = len(reste)
    if r % 3 == 0: classes = [""] * r
    elif r % 3 == 2: classes = [""] * (r - 2) + ["moitie", "moitie"]
    elif r == 1: classes = ["plein"]
    else: classes = [""] * (r - 4) + ["large", "", "", "large"]
    larges = [k for k, c in enumerate(classes) if c in ("large", "plein", "moitie")]
    paysages = [p for p in reste if ori[p[0]] == "paysage"]
    autres = [p for p in reste if ori[p[0]] != "paysage"]
    # place des horizontales dans les grandes cases si possible
    ordre = [None] * r
    for k in larges:
        if paysages: ordre[k] = paysages.pop(0)
    pile = [p for p in reste if p not in [x for x in ordre if x]]
    for k in range(r):
        if ordre[k] is None: ordre[k] = pile.pop(0)
    out += [(p[0], p[1], c) for p, c in zip(ordre, classes)]
    return out

def taille_h1(t1):
    """Taille du grand titre : le mot le plus long tient toujours sur la largeur, même sur téléphone."""
    mot = max(len(m) for m in t1.split())
    return f"min(clamp(56px,12vw,150px),calc((100vw - 40px) / {mot * 0.56:.2f}),calc(1240px / {mot * 0.56:.2f}))"

def fil_ariane(slug, titre):
    d = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://sarahprod.com/"},
        {"@type": "ListItem", "position": 2, "name": "Spectacles", "item": "https://sarahprod.com/#spectacles"},
        {"@type": "ListItem", "position": 3, "name": titre, "item": f"https://sarahprod.com/spectacle/{slug}"}]}
    return '<script type="application/ld+json">' + _json.dumps(d, ensure_ascii=False) + '</script>'

def jour_mois(d):
    j, m, a = d.split("/")
    return j, MOIS[m], "20" + a, m

def page(slug, s, existants):
    img = f"/images/{slug}/"
    pays_list = sorted({p for *_, p in s["dates"] if p})
    # dates groupées par mois
    lignes, mois_courant = [], None
    for d, ville, salle, pays in s["dates"]:
        j, m, a, mnum = jour_mois(d)
        if (mnum, a) != mois_courant:
            mois_courant = (mnum, a)
            lignes.append(f'      <div class="mois">{MOIS_LONG[mnum]} <span class="an">{a}</span></div>')
        ancre = f"#weezevent-{slug}-{ville.lower().replace(' ', '-').replace('/', '-')}"
        lien = lien_de(slug, ville)
        if lien: ancre = lien
        salle_html = f"<small>{E(salle)}</small>" if salle else ""
        debut = (f'      <a class="d" href="{E(lien)}" target="_blank" rel="noopener"' if lien else '      <div class="d sans-lien"') + f' data-ville="{E(ville)}">'
        fin = '<span class="acheter">Acheter un billet</span></a>' if lien else '<span class="acheter attente">Billetterie bientôt ouverte</span></div>'
        lignes.append(debut + f'<div class="jour">{j}<span>{JOURS[_dt.date(int(a), int(mnum), int(j)).weekday()]}</span></div>'
                      f'<div class="lieu">{E(ville)}{salle_html}</div><div class="pays">{E(pays)}</div>' + fin)
    dates_html = "\n".join(lignes)
    filtre = ""
    if len(s["dates"]) > 0:
        filtre = ('    <label class="filtre-ville"><span>Chercher une ville</span>'
                  '<input id="filtre" type="search" placeholder="Ex. Lyon, Nantes, Paris…" autocomplete="off"></label>\n'
                  '    <p class="vide" id="vide" hidden>Pas de date dans cette ville pour l\'instant.</p>\n')
    n = len(s["dates"])
    plus_btn = (f'    <button class="voir-plus" id="voir-plus" type="button" data-n="{n - 10}">Voir les {n - 10} autres dates</button>\n') if n > 10 else ""
    infos = "".join((f'<span><b>{E(a)}</b><i class="an">{E(b)}</i></span>' if _re.fullmatch(r"\d{4}", b) else f'<span><b>{E(a)}</b>{E(b)}</span>') for a, b in s["infos"])
    texte = "".join(f"<p>{E(p)}</p>" for p in s["texte"])
    fiche = "".join(f"<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>" for a, b in s["fiche"] if b != AC)
    photos = [(n, f'{s["titre"]} : {t}') for n, t in s["grandes"]] + [(n, f'{s["titre"]}, photo de scène {n}') for n in s["vignettes"]]
    grandes = "".join(f'      <button class="ph {c}" type="button"><img src="{img}photo-{n:02d}.jpg" alt="{E(a)}" loading="lazy"></button>\n'
                      for n, a, c in disposition_photos(photos, os.path.join(SITE, "images", slug)))
    vign = ""
    su = s.get("salle_unique")
    cache_dates = 'hidden' if su else ''
    if s.get("bientot"):
        cache_dates = 'hidden'
        dates_section = f'''<section class="blanc section g" id="dates">
  <div class="c">
    <div class="entete">
      <h2 class="a-venir">Dates<br><span>à venir</span></h2>
      <p>Les premières villes et salles seront annoncées ici. Soyez prévenu dès l'ouverture de la billetterie.</p>
    </div>
    <div class="liste">
      <a class="d" href="/#alertes"><div class="jour">BIENTÔT<span>TOURNÉE</span></div><div class="lieu">Premières dates<small>Bientôt annoncées</small></div><div class="pays"></div><span class="acheter">Être prévenu</span></a>
      <a class="d" href="/programmateurs"><div class="jour">SALLES<span>PROGRAMMATEURS</span></div><div class="lieu">Accueillir le spectacle<small>Recevoir le dossier de diffusion</small></div><div class="pays"></div><span class="acheter">Nous contacter</span></a>
    </div>
  </div>
</section>'''
    else:
      dates_section = (f'''<section class="blanc section g" id="dates">
  <div class="c">
    <div class="entete">
      <h2 class="a-venir">Tournée<br><span>à venir</span></h2>
      <p>En attendant les dates de la tournée, le spectacle se joue à l'Apollo Théâtre, à Paris. Laissez votre email pour être prévenu.</p>
    </div>
    <div class="liste">
      <a class="d" href="{E(su[2])}" target="_blank" rel="noopener"><div class="jour">PARIS<span>À L'AFFICHE</span></div><div class="lieu">{E(su[0])}<small>{E(su[1])}</small></div><div class="pays"></div><span class="acheter">Acheter un billet</span></a>
      <a class="d" href="/#alertes"><div class="jour">BIENTÔT<span>TOURNÉE</span></div><div class="lieu">Nouvelles villes<small>Dates bientôt annoncées</small></div><div class="pays"></div><span class="acheter">Être prévenu</span></a>
    </div>
  </div>
</section>''') if su else ''
    if s.get("video"):
        video_html = (f'<div class="video{" vertical" if s.get("video_vertical") else ""}" id="teaser">\n'
                      f'      <video controls preload="metadata" playsinline poster="{img}{s["poster"]}" src="{s["video"]}">\n'
                      f'        Votre navigateur ne lit pas cette vidéo. <a href="{s["video"]}">Ouvrir le teaser</a>\n      </video>\n    </div>')
    elif s.get("youtube"):
        yt = s["youtube"]
        video_html = (f'<div class="video" id="teaser"><button class="yt" type="button" data-yt="{yt}" aria-label="Lancer le teaser sur YouTube">'
                      f'<img src="{img}{s["poster"]}" alt="" loading="lazy"><span class="play">▶</span><span class="yt-note">Teaser · la vidéo se charge depuis YouTube</span></button></div>')
    else:
        video_html = ''
    a_video = s.get("video") or s.get("youtube")
    if s.get("bientot"):
        hero_btns = ('          <a class="btn jaune" href="/#alertes">Être prévenu des dates</a>\n'
                     + (('          <a class="btn contour" href="#teaser">▶ Voir le teaser</a>\n' if a_video else '') + ('          <a class="btn contour" href="#photos">Voir les photos</a>' if s["grandes"] else '') or '          <a class="btn contour" href="/programmateurs#' + slug + '">Programmer le spectacle</a>'))
    else:
        hero_btns = ('          <a class="btn jaune" href="#dates">Acheter un billet</a>\n'
                     + ('          <a class="btn contour" href="#teaser">▶ Voir le teaser</a>\n' if a_video else '') + ('          <a class="btn contour" href="#photos">Voir les photos</a>' if s["grandes"] else ''))
    final_btns = ('      <a class="btn noir" href="/#alertes">Être prévenu des dates</a>\n      <a class="btn contour" href="/programmateurs#' + slug + '">Programmer le spectacle</a>') if s.get("bientot") else ('      <a class="btn noir" href="#dates">Acheter un billet</a>\n      <a class="btn contour" href="/#alertes">Être prévenu des nouvelles dates</a>')
    fond_html = (f'  <img class="fond" src="{img}{s["fond"]}" alt="{E(s["titre"])} sur scène">') if s.get("fond") else '  <div class="fond-disco" aria-hidden="true"></div>'
    og_img = (f'<meta property="og:image" content="https://sarahprod.com{img}{s["fond"]}">') if s.get("fond") else ''
    cache_medias = '' if (s["grandes"] or s.get("video") or s.get("youtube")) else 'hidden'
    galerie_html = ('    <h2>En images</h2>\n    <div class="galerie" id="photos">\n' + grandes + '    </div>\n' + f'    <p class="compteur"><span>Faites glisser pour voir les photos</span><span><b id="ph-n">1</b> / {len(photos)}</span></p>\n' + '    <script>(function(){const g=document.getElementById("photos"),n=document.getElementById("ph-n");if(!g||!n)return;g.addEventListener("scroll",()=>{const w=g.firstElementChild.getBoundingClientRect().width+10;n.textContent=Math.min(g.children.length,Math.round(g.scrollLeft/w)+1);},{passive:true});})();</script>\n' + vign + f'    <p class="credit">{E(s["credit"])}</p>') if s["grandes"] else '    <h2>Le teaser</h2>'
    autres = "".join(
        f'<a href="{"/spectacle/" + sl if sl in existants else "#"}"><img src="/images/affiches/{sl}.jpg" alt="{E(t)}" loading="lazy" '
        f'onerror="this.onerror=null;this.src=secours(\'{c1}\',\'{c2}\')"><b>{E(t)}</b><small>{E(cat)}</small></a>'
        for sl, t, cat, c1, c2 in TOUS if sl != slug)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<title>{E(s["seo_title"])}</title>
<meta name="description" content="{E(s["seo_desc"])}">
<link rel="canonical" href="https://sarahprod.com/spectacle/{slug}">
<meta property="og:url" content="https://sarahprod.com/spectacle/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sarah Prod">
<meta property="og:title" content="{E(s["titre"])} | Sarah Prod">
<meta property="og:description" content="{E(s["seo_desc"])}">
{og_img}
{json_ld(slug, s)}
{fil_ariane(slug, s["titre"])}
<meta name="twitter:card" content="summary_large_image">
{FONTS}
{CSS_LINK}
<style>.hero .fond{{object-position:{s["fond_pos"]}}}.hero h1{{font-size:{taille_h1(s["t1"])};line-height:.95}}</style>
<script>
function secours(c1,c2){{c1=c1||'#3A23A6';c2=c2||'#5B3CD5';const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="420" height="600"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${{c2}}"/><stop offset="1" stop-color="${{c1}}"/></linearGradient></defs><rect width="420" height="600" fill="url(#g)"/><circle cx="330" cy="110" r="140" fill="#fff" opacity=".12"/><rect x="34" y="40" width="60" height="6" fill="#FCDE02"/><text x="34" y="560" font-family="sans-serif" font-weight="800" font-size="18" letter-spacing="3" fill="#fff">SARAH PROD</text></svg>`;return 'data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);}}
</script>
</head>
<body>

<section class="hero">
{fond_html}
  <div class="g"><div class="c">
    <header class="nav">
      <a class="logo" href="/" aria-label="Sarah Prod, accueil"><img src="/images/commun/logo-clair.png" alt="Sarah Prod"></a>
      <nav class="menu" aria-label="Navigation principale">
        <a href="/#spectacles" aria-current="page">Spectacles</a>
        <a href="/#dates">Dates</a>
        <a href="/qui-sommes-nous">Qui sommes-nous</a>
        <a href="/contact">Contact</a>
        <a class="pro" href="/programmateurs">Programmateurs</a>
      </nav>
    </header>
    <div class="fil"><a href="/">Accueil</a> / <a href="/#spectacles">Spectacles</a> / {E(s["titre"])}</div>
    <div class="scene">
      <div>
        <span class="chip">{E(s["cat"])}</span>
        <h1>{E(s["t1"])}<span>{E(s["t2"])}</span></h1>
        <p class="accroche">{E(s["accroche"])}</p>
        <div class="infos">{infos}</div>
        <div class="actions">
{hero_btns}
        </div>
      </div>
      <div aria-hidden="true"></div>
    </div>
  </div></div>
</section>

{dates_section}
<section class="blanc section g" id="dates" {cache_dates}>
  <div class="c">
    <div class="entete">
      <h2>Les dates<br>de la tournée</h2>
      <p>Choisissez votre ville. Le bouton vous emmène directement sur la billetterie de la date.</p>
    </div>
{filtre}    <div class="liste" id="liste">
{dates_html}
    </div>
{plus_btn}  </div>
</section>

<section class="section g">
  <div class="c histoire">
    <div class="texte">
      <h2 style="margin-bottom:28px">Le spectacle</h2>
      {texte}
    </div>
    <dl class="fiche" style="margin:0">{fiche}</dl>
  </div>
</section>

<section class="section g" style="padding-top:0" {cache_medias}>
  <div class="c">
{galerie_html}
{video_html}
  </div>
</section>

<section class="section g" style="padding-top:0">
  <div class="c">
    <h2>Les autres spectacles</h2>
    <div class="autres">{autres}</div>
  </div>
</section>

<section class="final section g">
  <div class="c">
    <h2>{E(s["final_titre"])}</h2>
    <p>{E(s["final_texte"])}</p>
    <div class="actions">
{final_btns}
    </div>
  </div>
</section>

<footer class="g">
  <div class="c">
    <img src="/images/commun/logo-clair.png" alt="Sarah Prod">
    <nav aria-label="Pied de page"><a href="/#spectacles">Spectacles</a><a href="/#dates">Dates</a><a href="/programmateurs">Programmateurs</a><a href="/#historique">Notre historique</a><a href="/qui-sommes-nous">Qui sommes-nous</a><a href="/contact">Contact</a><a href="/mentions-legales">Mentions légales</a><a href="/confidentialite">Confidentialité</a></nav>
  </div>
</footer>

<div class="visionneuse" id="visionneuse" hidden><img alt=""><button type="button" id="fermer">Fermer ✕</button></div>
<script>
(function(){{
  const v=document.getElementById('visionneuse'),im=v.querySelector('img');
  document.querySelectorAll('button.ph').forEach(b=>b.addEventListener('click',()=>{{const i=b.querySelector('img');im.src=i.src;im.alt=i.alt;v.hidden=false;}}));
  const fermer=()=>{{v.hidden=true;}};
  document.getElementById('fermer').addEventListener('click',fermer);
  v.addEventListener('click',e=>{{if(e.target===v)fermer();}});
  document.addEventListener('keydown',e=>{{if(e.key==='Escape')fermer();}});
  document.querySelectorAll('button.yt').forEach(b=>b.addEventListener('click',()=>{{const f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.yt+'?autoplay=1&rel=0';f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;f.title='Teaser';b.replaceWith(f);}}));
  const rows=[...document.querySelectorAll('#liste .d')],mois=[...document.querySelectorAll('#liste .mois')],btn=document.getElementById('voir-plus');
  let ouvert=!btn;
  const majMois=()=>mois.forEach(m=>{{let x=m.nextElementSibling,vis=false;while(x&&!x.classList.contains('mois')){{if(!x.hidden)vis=true;x=x.nextElementSibling;}}m.hidden=!vis;}});
  const replier=()=>{{rows.forEach((d,i)=>{{d.hidden=!ouvert&&i>=10;}});majMois();if(btn){{btn.innerHTML=ouvert?'Voir moins de dates':'Voir les '+btn.dataset.n+' autres dates';}}}};
  if(btn){{btn.addEventListener('click',()=>{{ouvert=!ouvert;replier();if(!ouvert)document.getElementById('dates').scrollIntoView({{behavior:'smooth'}});}});}}
  replier();
  const f=document.getElementById('filtre');
  if(f){{
    const norm=t=>t.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();
    f.addEventListener('input',()=>{{
      const q=norm(f.value.trim());
      if(!q){{document.getElementById('vide').hidden=true;if(btn)btn.hidden=false;replier();return;}}
      let n=0;rows.forEach(d=>{{const ok=norm(d.dataset.ville).includes(q);d.hidden=!ok;if(ok)n++;}});
      majMois();if(btn)btn.hidden=true;
      document.getElementById('vide').hidden=n>0;
    }});
  }}
}})();
</script>
</body>
</html>
"""

existants = set(SPECTACLES)
os.makedirs(os.path.join(SITE, "spectacle"), exist_ok=True)
for slug, s in SPECTACLES.items():
    open(os.path.join(SITE, "spectacle", slug + ".html"), "w", encoding="utf-8").write(page(slug, s, existants))
    print("écrit", slug)
open(os.path.join(SITE, "spectacles.json"), "w").write('["' + '","'.join(sorted(existants)) + '"]\n')

# --- toutes les dates sur l'accueil (index.html) ---
_toutes = []
for _slug, _s in SPECTACLES.items():
    if _s.get("bientot"): continue
    for _d, _v, _salle, _p in _s["dates"]:
        _j, _m, _a = _d.split("/")
        _toutes.append((f"20{_a}{_m}{_j}", {"j": _j, "m": MOIS_LONG[_m], "a": "20" + _a, "ville": _v, "salle": _salle, "s": _slug,
                                           "l": lien_de(_slug, _v)}))
_toutes.sort(key=lambda x: x[0])
_js = "const DATES = [\n" + ",\n".join("  " + _json.dumps(x, ensure_ascii=False) for _, x in _toutes) + "\n];"
_ip = os.path.join(SITE, "index.html"); _html = open(_ip, encoding="utf-8").read()
_html = _re.sub(r"const DATES = \[.*?\n\];", lambda m: _js, _html, count=1, flags=_re.S)
open(_ip, "w", encoding="utf-8").write(_html)
print("accueil :", len(_toutes), "dates")

# --- version HTML statique de la liste des dates et du mur d'affiches (lisible par Google et les IA sans JavaScript) ---
_html = open(_ip, encoding="utf-8").read()
_t = {sl: (SPECTACLES[sl]["t1"], SPECTACLES[sl]["t2"]) if sl in SPECTACLES else (t, "") for sl, t, *_ in TOUS}
_lignes = []
for _, d in _toutes:
    t1, t2 = _t[d["s"]]
    href = d["l"] or f'/spectacle/{d["s"]}#dates'
    cible = ' target="_blank" rel="noopener"' if d["l"] else ''
    _lignes.append(f'<a class="d" href="{E(href)}"{cible} data-s="{d["s"]}" data-ville="{E(d["ville"])}"><div class="jour">{d["j"]} <em>{E(d["m"])}</em><span>{d["a"]}</span></div>'
                   f'<div class="lieu">{E(d["ville"])}<small>{E(d["salle"])}</small></div><div class="titre-sp">{E(t1)}<small>{E(t2)}</small></div><span class="resa">Acheter un billet</span></a>')
_aff = "".join(f'<figure class="aff" style="margin-block:0"><span class="punaise"></span><a href="/spectacle/{sl}"><img src="/images/affiches/{sl}.jpg" alt="Affiche {E(t)}" loading="lazy">'
               f'<figcaption><b>{E(_t[sl][0])}</b><i>{E(_t[sl][1])}</i><small>Voir le spectacle</small></figcaption></a></figure>' for sl, t, *_ in TOUS)
_html = _re.sub(r'<div class="liste" id="liste">.*?</div><!--/liste-->|<div class="liste" id="liste"></div>', lambda m: '<div class="liste" id="liste">' + "".join(_lignes) + '</div><!--/liste-->', _html, count=1, flags=_re.S)
_html = _re.sub(r'<div class="affiches" id="affiches">.*?</div><!--/affiches-->|<div class="affiches" id="affiches"></div>', lambda m: '<div class="affiches" id="affiches">' + _aff + '</div><!--/affiches-->', _html, count=1, flags=_re.S)
open(_ip, "w", encoding="utf-8").write(_html)
print("accueil statique :", len(_lignes), "dates,", len(TOUS), "affiches")
