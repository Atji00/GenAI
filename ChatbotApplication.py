import streamlit as st

# Fonction pour interroger le modèle et afficher les réponses
def display_chat():
    st.title("Chatbot FAQ - Gestion des Fonds Immobiliers")
    
    # Entrée utilisateur
    user_question = st.text_input("Posez votre question :")
    
    if user_question:
        # Obtenir la réponse à partir du modèle RAG
        response = qa_chain({"query": user_question})
        
        # Afficher la réponse
        st.write("Réponse :", response['result'])
        
        # Collecter le feedback utilisateur
        feedback = st.radio("Feedback", ["Correct", "Incorrect"])
        
        # Enregistrer le feedback
        if st.button("Envoyer le feedback"):
            collect_feedback(user_question, response['result'], feedback)

# Lancer l'interface Streamlit
if __name__ == '__main__':
    display_chat()
