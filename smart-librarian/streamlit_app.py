"""
streamlit_app.py
UI Streamlit pentru Smart Librarian – AI cu RAG + Tool
"""
import streamlit as st
from src.rag_chat import get_full_recommendation
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Smart Librarian", page_icon="📚")
st.title("Smart Librarian – AI Book Recommender")
st.write("Pune o întrebare despre ce fel de carte vrei să citești!")
query = st.text_input("Întrebare", "Vreau o carte despre prietenie și magie")
if "result" not in st.session_state:
    st.session_state.result = None
if "audio_path" not in st.session_state:
    st.session_state.audio_path = None

if st.button("Recomandă!"):
    with st.spinner("Se caută recomandarea..."):
        result = get_full_recommendation(query)
        st.session_state.result = result
        st.session_state.audio_path = None

if st.session_state.result:
    result = st.session_state.result
    st.subheader("Recomandare scurtă")
    st.write(result["short"])
    st.subheader("Rezumat complet")
    st.write(result["summary"])
    if st.button("Ascultă recomandarea și rezumatul"):
        tts_text = f"{result['short']} {result['summary']}"
        tts = gTTS(tts_text, lang='ro')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.session_state.audio_path = fp.name
    if st.session_state.audio_path:
        st.audio(st.session_state.audio_path, format="audio/mp3")
