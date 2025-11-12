import streamlit as st

st.set_page_config(page_title="Copilote Projet", page_icon="🚀", layout="centered")

st.title("🚀 Copilote Projet")
st.markdown("### En 3 clics, avance sur ton projet — sans surcharge, sans perte de temps.")

# Structure enrichie avec ressources fictives/idéalement utiles
structure = {
    "💡 Clarifier mon projet": {
        "Trouver mon angle / raison d’être": {
            "why": "Pour comprendre ce qui te motive profondément.",
            "result": "Tu repars avec une formulation claire de ta mission et ton pourquoi.",
            "resources": [
                {"titre": "Atelier introspectif : les 5 couches du pourquoi", "type": "Atelier guidé", "durée": "30 min"},
                {"titre": "Podcast : 'Trouver ce qui te met en mouvement' (épisode 4)", "type": "Podcast", "durée": "20 min"},
                {"titre": "Template Notion : formuler sa mission personnelle", "type": "Template", "durée": "—"},
            ],
        },
        "Identifier mes bénéficiaires": {
            "why": "Pour savoir à qui ton projet rend service.",
            "result": "Tu repars avec 1 à 2 profils précis de bénéficiaires.",
            "resources": [
                {"titre": "Mini-guide : cartographier ses publics cibles", "type": "Guide PDF", "durée": "10 min"},
                {"titre": "Exercice miroir : décrire son utilisateur type", "type": "Exercice", "durée": "15 min"},
            ],
        },
        "Définir mon offre": {
            "why": "Pour passer d'une idée à une proposition concrète.",
            "result": "Tu repars avec une offre testable à présenter.",
            "resources": [
                {"titre": "Framework : proposition de valeur en 3 phrases", "type": "Outil", "durée": "10 min"},
                {"titre": "Étude de cas : 'Comment une asso a défini son offre en 1 semaine'", "type": "Cas pratique", "durée": "5 min"},
            ],
        },
    },

    "💰 Financer / rendre viable": {
        "Trouver une aide / bourse": {
            "why": "Pour identifier les leviers financiers disponibles.",
            "result": "Tu obtiens une première liste d’aides compatibles avec ton profil.",
            "resources": [
                {"titre": "Base de données : aides associatives et citoyennes 2025", "type": "Base en ligne", "durée": "—"},
                {"titre": "Simulateur : quelles aides pour mon profil ?", "type": "Outil interactif", "durée": "3 min"},
            ],
        },
        "Poser mon modèle économique": {
            "why": "Pour que ton projet puisse durer dans le temps.",
            "result": "Tu repars avec un schéma de modèle économique simple et adapté.",
            "resources": [
                {"titre": "Canvas simplifié du modèle économique citoyen", "type": "Template", "durée": "15 min"},
                {"titre": "Vidéo : 'Comment équilibrer sens et viabilité'", "type": "Vidéo", "durée": "12 min"},
            ],
        },
        "Évaluer mes besoins réels": {
            "why": "Pour éviter de chercher trop ou pas assez.",
            "result": "Tu définis les besoins financiers essentiels à court terme.",
            "resources": [
                {"titre": "Tableur pré-rempli : calcul de besoins essentiels", "type": "Outil Excel", "durée": "10 min"},
                {"titre": "Checklist : tout ce qui coûte sans qu’on s’en rende compte", "type": "Checklist", "durée": "5 min"},
            ],
        },
    },

    "🚀 Passer à l’action": {
        "Lancer une première version": {
            "why": "Pour tester sans attendre d’avoir tout prêt.",
            "result": "Tu obtiens un plan de lancement concret en 3 étapes.",
            "resources": [
                {"titre": "Mini-cours : créer un prototype à coût zéro", "type": "Vidéo", "durée": "10 min"},
                {"titre": "Template : plan de lancement 3 étapes", "type": "Template", "durée": "—"},
            ],
        },
        "Trouver des partenaires": {
            "why": "Pour ne pas avancer seul.",
            "result": "Tu repars avec des pistes pour identifier et contacter les bons alliés.",
            "resources": [
                {"titre": "Carte interactive : acteurs solidaires et partenaires locaux", "type": "Carte", "durée": "—"},
                {"titre": "Guide : comment formuler une demande de collaboration", "type": "Guide PDF", "durée": "8 min"},
            ],
        },
        "Tester / prototyper": {
            "why": "Pour confronter ton idée au réel rapidement.",
            "result": "Tu obtiens une méthode simple pour prototyper ton idée.",
            "resources": [
                {"titre": "Atelier : le prototype d’un après-midi", "type": "Atelier", "durée": "1h"},
                {"titre": "Exemples : 5 projets qui ont testé avant d’avoir les moyens", "type": "Cas pratiques", "durée": "10 min"},
            ],
        },
    },

    "🤝 Trouver du soutien": {
        "Intégrer un réseau": {
            "why": "Pour te connecter à des pairs et mentors.",
            "result": "Tu repars avec 2-3 réseaux pertinents à explorer.",
            "resources": [
                {"titre": "Annuaire des communautés actives (France 2025)", "type": "Base de données", "durée": "—"},
                {"titre": "Tuto : comment approcher un réseau sans syndrome de l’imposteur", "type": "Vidéo", "durée": "7 min"},
            ],
        },
        "Obtenir du feedback": {
            "why": "Pour progresser plus vite grâce au regard des autres.",
            "result": "Tu repars avec une stratégie pour obtenir des retours utiles.",
            "resources": [
                {"titre": "Guide : organiser une session feedback rapide", "type": "Guide", "durée": "10 min"},
                {"titre": "Template : grille de feedback bienveillant", "type": "Template", "durée": "—"},
            ],
        },
        "Trouver un mentor": {
            "why": "Pour bénéficier d’une expérience directe.",
            "result": "Tu obtiens une méthode pour repérer et contacter des mentors.",
            "resources": [
                {"titre": "Checklist : que demander à un mentor (et quoi éviter)", "type": "Checklist", "durée": "5 min"},
                {"titre": "Mini-guide : formuler une demande de mentorat claire", "type": "Guide", "durée": "8 min"},
            ],
        },
    },

    "📈 Structurer et croître": {
        "Organiser mon temps": {
            "why": "Pour garder le cap sans t’épuiser.",
            "result": "Tu repars avec une méthode simple de priorisation hebdo.",
            "resources": [
                {"titre": "Template Notion : plan d’action hebdomadaire minimaliste", "type": "Template", "durée": "—"},
                {"titre": "Exercice : les 3 objectifs essentiels de la semaine", "type": "Exercice", "durée": "10 min"},
            ],
        },
        "Formaliser ma stratégie": {
            "why": "Pour donner une direction claire à ton développement.",
            "result": "Tu repars avec une première roadmap réaliste.",
            "resources": [
                {"titre": "Mini-cours : la stratégie sans bullshit", "type": "Vidéo", "durée": "12 min"},
                {"titre": "Outil : construire une roadmap visuelle simple", "type": "Outil", "durée": "15 min"},
            ],
        },
        "Communiquer efficacement": {
            "why": "Pour que ton projet devienne visible et compris.",
            "result": "Tu obtiens les bases d’un message clair et cohérent.",
            "resources": [
                {"titre": "Template : ton pitch en 30 secondes", "type": "Template", "durée": "—"},
                {"titre": "Atelier audio : 'dire ton projet comme une histoire'", "type": "Atelier audio", "durée": "20 min"},
            ],
        },
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
        data = structure[main_choice][sub_choice]
        st.markdown("---")
        st.subheader("3️⃣ Ce que ton copilote te propose 💡")
        st.markdown(f"**🎯 Pour :** {data['why']}")
        st.markdown(f"**✅ Résultat attendu :** {data['result']}")

        st.markdown("#### 📚 Ressources à explorer")
        for res in data["resources"]:
            with st.container():
                st.markdown(f"**{res['titre']}** — *{res['type']}* ({res['durée']})")
                st.progress(0)
        st.success("👉 Explore une ressource ou note ta progression ici.")
