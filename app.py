import streamlit as st

st.set_page_config(page_title="Copilote Projet", page_icon="🚀", layout="centered")

st.title("🚀 Copilote Projet")
st.markdown("### En 3 clics, avance sur ton projet — sans surcharge, sans perte de temps.")

# Dictionnaire de structure
structure = {
    "💡 Clarifier mon projet": {
        "Trouver mon angle / raison d’être": (
            "Pour comprendre ce qui te motive profondément.",
            "Tu repars avec une formulation claire de ta mission et ton pourquoi."
        ),
        "Identifier mes bénéficiaires": (
            "Pour savoir à qui ton projet rend service.",
            "Tu repars avec 1 à 2 profils précis de bénéficiaires."
        ),
        "Définir mon offre": (
            "Pour passer d'une idée à une proposition concrète.",
            "Tu repars avec une offre testable à présenter."
        ),
    },

    "💰 Financer / rendre viable": {
        "Trouver une aide / bourse": (
            "Pour identifier les leviers financiers disponibles.",
            "Tu obtiens une première liste d’aides compatibles avec ton profil."
        ),
        "Poser mon modèle économique": (
            "Pour que ton projet puisse durer dans le temps.",
            "Tu repars avec un schéma de modèle économique simple et adapté."
        ),
        "Évaluer mes besoins réels": (
            "Pour éviter de chercher trop ou pas assez.",
            "Tu définis les besoins financiers essentiels à court terme."
        ),
    },

    "🚀 Passer à l’action": {
        "Lancer une première version": (
            "Pour tester sans attendre d’avoir tout prêt.",
            "Tu obtiens un plan de lancement concret en 3 étapes."
        ),
        "Trouver des partenaires": (
            "Pour ne pas avancer seul.",
            "Tu repars avec des pistes pour identifier et contacter les bons alliés."
        ),
        "Tester / prototyper": (
            "Pour confronter ton idée au réel rapidement.",
            "Tu obtiens une méthode simple pour prototyper ton idée."
        ),
    },

    "🤝 Trouver du soutien": {
        "Intégrer un réseau": (
            "Pour te connecter à des pairs et mentors.",
            "Tu repars avec 2-3 réseaux pertinents à explorer."
        ),
        "Obtenir du feedback": (
            "Pour progresser plus vite grâce au regard des autres.",
            "Tu repars avec une stratégie pour obtenir des retours utiles."
        ),
        "Trouver un mentor": (
            "Pour bénéficier d’une expérience directe.",
            "Tu obtiens une méthode pour repérer et contacter des mentors."
        ),
    },

    "📈 Structurer et croître": {
        "Organiser mon temps": (
            "Pour garder le cap sans t’épuiser.",
            "Tu repars avec une méthode simple de priorisation hebdo."
        ),
        "Formaliser ma stratégie": (
            "Pour donner une direction claire à ton développement.",
            "Tu repars avec une première roadmap réaliste."
        ),
        "Communiquer efficacement": (
            "Pour que ton projet devienne visible et compris.",
            "Tu obtiens les bases d’un message clair et cohérent."
        ),
    },
}

# Étape 1 : choix du besoin principal
st.subheader("1️⃣ Ton besoin du moment")
main_choice = st.radio(
    "Choisis ce qui te correspond le mieux :",
    list(structure.keys()),
    index=None,
)

if main_choice:
    st.markdown("---")
    st.subheader("2️⃣ Ce que tu veux faire précisément")
    sub_choice = st.radio(
        "Affinons un peu ton besoin 👇",
        list(structure[main_choice].keys()),
        index=None,
    )

    if sub_choice:
        why, result = structure[main_choice][sub_choice]
        st.markdown("---")
        st.subheader("3️⃣ Ce que ton copilote te propose 💡")
        st.markdown(f"**🎯 Pour :** {why}")
        st.markdown(f"**✅ Résultat attendu :** {result}")
        st.success("👉 Prochaine étape : explore cette piste ou note ta progression.")
