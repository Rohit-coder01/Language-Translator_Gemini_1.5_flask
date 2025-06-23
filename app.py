import streamlit as st
import google.generativeai as genai
import os

# --- API Setup ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])


model = genai.GenerativeModel("gemini-1.5-flash")

# --- Page Config ---
st.set_page_config(page_title="Language Translator", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
    html, body {
        zoom: 1.1; /* Works reliably across browsers */
    }
    body {
        background-color: #0e1117;
        color: white;
    }
    .main {
        max-width: 700px;
        margin: auto;
        padding-top: 50px;
    }
    .stTextArea textarea {
        background-color: #1e1e1e;
        color: white;
    }
    .stSelectbox div {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🌍 Language Translator Using Gemini AI")
st.markdown("Translate text instantly using Google's Gemini 1.5 Flash model.")

# --- Input Section ---
user_text = st.text_area("✍️ Enter text to translate:")

languages = [
    "English", "Hindi", "Spanish", "French", "German", "Urdu", "Chinese", "Japanese", "Russian", "Arabic", "Portuguese",
    "Italian", "Korean", "Dutch", "Greek", "Hebrew", "Turkish", "Thai", "Vietnamese", "Bengali",
    "Punjabi", "Tamil", "Telugu", "Marathi", "Gujarati", "Malayalam", "Kannada", "Swedish", "Polish", "Czech",
    "Indonesian", "Romanian"
]

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("🔤 Source Language", languages)
with col2:
    target_lang = st.selectbox("🎯 Target Language", languages)

# --- Translation Logic ---
def language_translate(user_text, source_lang, target_lang):
    prompt = f"""Translate this text from {source_lang} to {target_lang}. 
Return only the exact translated version — no extra explanations, no examples, no formatting, and no interpretation. 


Text:
\"{user_text}\"
"""
    response = model.generate_content(prompt)
    return response.text if response else "Translation failed."

# --- Button & Output ---
if st.button("🚀 Translate"):
    if user_text.strip():
        result = language_translate(user_text, source_lang, target_lang)
        st.subheader("✅ Translated Text:")
        st.success(result)
    else:
        st.warning("⚠️ Please enter some text to translate.")

st.markdown("</div>", unsafe_allow_html=True)
