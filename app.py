"""
🎯 BUT :
Interface web Streamlit pour interroger l'agent LangChain

WHY :
- rendre l'agent utilisable sans terminal
- expérience utilisateur (chat)

HOW :
- champ de saisie utilisateur
- historique stocké en session_state
- affichage conversation
- sidebar avec tools
"""

import streamlit as st
from agent import creer_agent

# INIT AGENT
if "agent" not in st.session_state:
    st.session_state.agent = creer_agent()

# INIT HISTORIQUE
if "messages" not in st.session_state:
    st.session_state.messages = []

# UI PRINCIPALE
st.title("🤖 Agent Financier IA")

# SIDEBAR (TOOLS)
st.sidebar.title("🛠️ Outils disponibles")

tools_list = [
    "rechercher_client",
    "rechercher_produit",
    "cours_action",
    "cours_crypto",
    "calculer_tva",
    "calculer_interets",
    "calculer_marge",
    "calculer_mensualite",
    "convertir_devise",
    "resumer_texte",
    "formater_rapport",
    "extraire_mots_cles",
    "recommander_produits",
    "calculer_portefeuille",
    "python_repl",
    "tavily_search"
]

for tool in tools_list:
    st.sidebar.write(f"• {tool}")

# BOUTON RESET
if st.sidebar.button("🔄 Réinitialiser conversation"):
    st.session_state.messages = []

# AFFICHAGE HISTORIQUE
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# INPUT UTILISATEUR
user_input = st.chat_input("Pose ta question...")

if user_input:
    # afficher message user
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # appeler agent
    response = st.session_state.agent.invoke({"input": user_input})
    answer = response["output"]

    # stocker réponse
    st.session_state.messages.append({"role": "assistant", "content": answer})

    # afficher réponse
    with st.chat_message("assistant"):
        st.markdown(answer)