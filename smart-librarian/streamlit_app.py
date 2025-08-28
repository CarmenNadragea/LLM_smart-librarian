"""
streamlit_app.py
UI Streamlit pentru Smart Librarian – AI cu RAG + Tool
"""
import streamlit as st
from src.rag_chat import get_full_recommendation

st.set_page_config(page_title="Smart Librarian", page_icon="📚")
st.title("Smart Librarian – AI Book Recommender")
st.write("Pune o întrebare despre ce fel de carte vrei să citești!")

query = st.text_input("Întrebare", "Vreau o carte despre prietenie și magie")
if st.button("Recomandă!"):
    with st.spinner("Se caută recomandarea..."):
        result = get_full_recommendation(query)
        st.subheader("Recomandare scurtă")
        st.write(result["short"])
        st.subheader("Rezumat complet")
        st.write(result["summary"])
