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
if "axe" not in st.session_state:
    st.session_state.axe = None
if "sous_option" not in st.session_state:
    st.session_state.sous_option = None

# ------------------------
# RESSOURCES FICTIVES
# ------------------------
ressources = {
    "💰 Ressources & finances": {
        "Financer temporairement mon projet": [
            {"titre": "Subventions express", "desc": "Liste fictive de subventions rapides.", "type": "Outil"},
            {"titre": "Template budget minimal", "desc": "Plan simple pour organiser tes ressources.", "type": "Outil"}
        ],
        "Optimiser la trésorerie": [
            {"titre": "Checklist trésorerie", "desc": "Points clés pour anticiper les imprévus.", "type": "Méthode"},
            {"titre": "Fiche économies rapides", "desc": "Idées fictives pour réduire les coûts.", "type": "Exercice"}
        ],
        "Accéder à des financements stratégiques": [
            {"titre": "Guide levée de fonds", "desc": "Fictif, étapes pour convaincre un investisseur.", "type": "Lecture"},
            {"titre": "Pitch deck modèle", "desc": "Template à adapter pour ton projet.", "type": "Outil"}
        ]
    },
    "🛠️ Stratégie & opération": {
        "Clarifier ou pivoter le business model": [
            {"titre": "Canvas simplifié", "desc": "Outil fictif pour visualiser ton modèle.", "type": "Outil"},
            {"titre": "Fiche pivot rapide", "desc": "Méthode pour tester rapidement une nouvelle idée.", "type": "Méthode"}
        ],
        "Prioriser les actions à forte valeur": [
            {"titre": "Matrix impact/effort", "desc": "Outil fictif pour hiérarchiser les tâches.", "type": "Outil"},
            {"titre": "Checklist focus 48h", "desc": "Exercice pour choisir 3 actions clés.", "type": "Exercice"}
        ],
        "Développer compétences internes": [
            {"titre": "Plan formation interne", "desc": "Guide fictif pour structurer apprentissage.", "type": "Outil"},
            {"titre": "Exercice d’auto-évaluation", "desc": "Fiche pour identifier gaps de compétences.", "type": "Exercice"}
        ]
    },
    "🌐 Relations & impact": {
        "Trouver partenaires ou mentors": [
            {"titre": "Annuaire fictif mentors", "desc": "Liste pour inspiration et contact.", "type": "Ressource"},
            {"titre": "Fiche réseautage rapide", "desc": "Méthode pour approcher partenaires clés.", "type": "Méthode"}
        ],
        "Gagner en visibilité": [
            {"titre": "Template post impact", "desc": "Exemple fictif pour communiquer efficacement.", "type": "Outil"},
            {"titre": "Checklist médias sociaux", "desc": "Guide pour planifier publications simples.", "type": "Méthode"}
        ],
        "Mobiliser communauté": [
            {"titre": "Mini-guide engagement", "desc": "Exercice pour impliquer ta communauté.", "type": "Exercice"},
            {"titre": "Fiche storytelling", "desc": "Structurer ton récit pour fédérer.", "type": "Méthode"}
        ]
    }
}

# ------------------------
# LOGIQUE NAVIGATION
# ------------------------

# Étape 1 : Choix axe
if st.session_state.step == 1:
    st.subheader("Quel type de besoin veux-tu traiter ?")
    cols = st.columns(3)
    axes = list(ressources.keys())
    for i, axe in enumerate(axes):
        if cols[i].button(axe):
            st.session_state.axe = axe
            st.session_state.step = 2

    st.markdown("---")
    st.markdown("💡 Ou si tu sais exactement ce que tu cherches, tape un mot-clé :")
    recherche = st.text_input("Recherche rapide")
    if recherche:
        # Recherche simple : trouver sous-option contenant le mot-clé
        resultats = []
        for axe_key, sous_options in ressources.items():
            for so_key, res_list in sous_options.items():
                if recherche.lower() in so_key.lower():
                    resultats.append((axe_key, so_key, res_list))
        if resultats:
            for axe_key, so_key, res_list in resultats:
                st.markdown(f"### {so_key} ({axe_key})")
                for r in res_list:
                    st.markdown(f"**{r['titre']}** — *{r['type']}*")
                    st.markdown(r['desc'])

# Étape 2 : Choix sous-option
elif st.session_state.step == 2:
    axe = st.session_state.axe
    st.subheader(f"🧠 {axe}")
    st.markdown("Choisis une option précise :")
    for sous_option in ressources[axe].keys():
        if st.button(sous_option):
            st.session_state.sous_option = sous_option
            st.session_state.step = 3

    if st.button("⬅️ Revenir au début"):
        st.session_state.step = 1
        st.session_state.axe = None
        st.session_state.sous_option = None

# Étape 3 : Affichage ressources
elif st.session_state.step == 3:
    axe = st.session_state.axe
    sous_option = st.session_state.sous_option
    st.subheader(f"💡 Ressources pour : {sous_option} ({axe})")

    for r in ressources[axe][sous_option]:
        st.markdown(f"### {r['titre']} — *{r['type']}*")
        st.markdown(r['desc'])
        st.button(f"✨ Explorer {r['titre']}", key=r['titre'])

    st.markdown("---")
    if st.button("⬅️ Revenir au début"):
        st.session_state.step = 1
        st.session_state.axe = None
        st.session_state.sous_option = None
