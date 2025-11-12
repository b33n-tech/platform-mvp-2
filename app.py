import streamlit as st

# ------------------------
# CONFIG
# ------------------------
st.set_page_config(page_title="Copilote Projet", page_icon="🚀", layout="centered")
st.markdown("<h1 style='text-align:center;'>🚀 Copilote Projet</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Avançons ensemble, concrètement.</p>", unsafe_allow_html=True)

# ------------------------
# SESSION STATE
# ------------------------
if "step" not in st.session_state:
    st.session_state.step = 1
if "etat" not in st.session_state:
    st.session_state.etat = None
if "blocage" not in st.session_state:
    st.session_state.blocage = None

# ------------------------
# RESSOURCES FICTIVES
# ------------------------
ressources = {
    "🚀 Passer à l’action": {
        "Manque de clarté": [
            {"titre": "Cadre des 3 prochains pas", "desc": "Un outil pour décider rapidement quoi faire dans les 48h.", "type": "Outil"},
            {"titre": "Méthode Sprint 48h", "desc": "Fiche pour enclencher un mini sprint projet.", "type": "Méthode"},
            {"titre": "Action directe", "desc": "Définis ton horizon 2 jours / 2 semaines / 2 mois.", "type": "Exercice"}
        ],
        "Manque de cadre": [
            {"titre": "Template Focus", "desc": "Un modèle Notion pour poser ton cadre hebdo.", "type": "Outil"},
            {"titre": "Framework du juste effort", "desc": "Comment calibrer ton énergie et tes priorités.", "type": "Ressource"},
            {"titre": "Mini action", "desc": "Écris ton objectif du jour en une phrase.", "type": "Exercice"}
        ],
        "Peur de mal faire": [
            {"titre": "Manifeste du progrès imparfait", "desc": "Lecture rapide pour débloquer l’action.", "type": "Lecture"},
            {"titre": "Fiche ‘Test rapide’", "desc": "Une méthode pour expérimenter sans pression.", "type": "Méthode"},
            {"titre": "Action mentale", "desc": "Liste 3 micro-victoires récentes.", "type": "Exercice"}
        ]
    },
    "🧭 Trouver ma direction": {
        "Trop d’idées": [
            {"titre": "Carte de tri des idées", "desc": "Outil visuel pour hiérarchiser tes intuitions.", "type": "Outil"},
            {"titre": "Méthode du fil rouge", "desc": "Identifier le lien commun à tes projets.", "type": "Méthode"},
            {"titre": "Action", "desc": "Choisis une idée à explorer 48h sans réfléchir.", "type": "Exercice"}
        ],
        "Aucune idée claire": [
            {"titre": "Journal des signaux faibles", "desc": "Note ce qui te touche ou t’énerve chaque jour.", "type": "Exercice"},
            {"titre": "Podcast ‘L’étincelle’", "desc": "Écoute 3 histoires de projets inattendus.", "type": "Ressource"},
            {"titre": "Outil: Carte de curiosité", "desc": "Un outil visuel pour repérer tes aimants naturels.", "type": "Outil"}
        ],
        "Doute sur la bonne voie": [
            {"titre": "Grille de sens personnel", "desc": "Croise tes valeurs et tes leviers d’énergie.", "type": "Outil"},
            {"titre": "Lecture : ‘Les bifurcations’", "desc": "Essai court sur le changement de trajectoire.", "type": "Lecture"},
            {"titre": "Exercice", "desc": "Décris ton projet comme s’il était déjà réalisé.", "type": "Exercice"}
        ]
    },
    "💡 Clarifier mon idée": {
        "Trop floue": [
            {"titre": "Template ‘Pitch éclair’", "desc": "Un canevas pour formuler ton idée en 5 phrases.", "type": "Outil"},
            {"titre": "Méthode ‘Zoom arrière’", "desc": "Prends de la hauteur sur ton intention de départ.", "type": "Méthode"},
            {"titre": "Exercice", "desc": "Explique ton idée à un ami en 2 min.", "type": "Exercice"}
        ],
        "Trop complexe": [
            {"titre": "Fiche ‘Épure’", "desc": "Comment simplifier sans perdre le fond.", "type": "Méthode"},
            {"titre": "Outil : Carte simplifiée", "desc": "Découpe ton idée en 3 blocs de sens.", "type": "Outil"},
            {"titre": "Action", "desc": "Écris ta promesse en une phrase de 10 mots max.", "type": "Exercice"}
        ]
    }
}

# ------------------------
# LOGIQUE NAVIGATION
# ------------------------

# Étape 1 : Choix état
if st.session_state.step == 1:
    st.subheader("Où veux-tu avancer aujourd’hui ?")
    cols = st.columns(3)
    for i, etat in enumerate(ressources.keys()):
        if cols[i % 3].button(etat):
            st.session_state.etat = etat
            st.session_state.step = 2

# Étape 2 : Choix blocage
elif st.session_state.step == 2:
    etat = st.session_state.etat
    st.subheader(f"🧠 {etat}")
    st.markdown("Qu’est-ce qui t’empêche d’avancer le plus ?")
    for blocage in ressources[etat].keys():
        if st.button(blocage):
            st.session_state.blocage = blocage
            st.session_state.step = 3

# Étape 3 : Affichage des ressources
elif st.session_state.step == 3:
    etat = st.session_state.etat
    blocage = st.session_state.blocage
    st.subheader(f"💡 Ressources pour toi – {etat}")
    st.markdown(f"*Blocage identifié : {blocage}*")

    # cartes de ressources
    for r in ressources[etat][blocage]:
        st.markdown(f"### {r['titre']} — *{r['type']}*")
        st.markdown(r['desc'])
        st.button(f"✨ Explorer {r['titre']}", key=r['titre'])

    st.markdown("---")
    if st.button("⬅️ Revenir au début"):
        st.session_state.step = 1
        st.session_state.etat = None
        st.session_state.blocage = None
