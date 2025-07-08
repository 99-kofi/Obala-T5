
import streamlit as st
from model_utils import translate_to_french

st.set_page_config(page_title="OBALA French Translator", page_icon="🇫🇷")

st.title("🔥 OBALA French Translator")
st.markdown("Enter text in English and get the French translation instantly.")

user_input = st.text_area("📝 Enter English Text", height=150)
if st.button("Translate"):
    if user_input.strip():
        with st.spinner("Translating..."):
            french = translate_to_french(user_input)
        st.success(f"**French:** {french}")
    else:
        st.warning("Please enter some text.")
