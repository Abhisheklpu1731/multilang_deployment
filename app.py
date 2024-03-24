import streamlit as st
from mtranslate import translate as mtranslate_translate
import locale
from flask import Flask, render_template, request

# Supported languages (code: language name)
languages = {
    'ar': 'Arabic',
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'hi': 'Hindi',
    'ja': 'Japanese',
    'ko': 'Korean',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'zh-CN': 'Chinese (Simplified)',
}

# Function to translate text
def translate(text, source_lang, target_lang):
  try:
    translated_text = mtranslate_translate(text, target_lang, source_lang)
    return translated_text
  except Exception as e:
    print("Translation failed:", e)
    return None

# Function to set font based on language
def get_font(lang_code):
  # Implement logic to determine font based on language code
  # (e.g., using external libraries or language-specific fonts)
  # For simplicity, this example returns a generic font for now
  return "sans-serif"  # Replace with appropriate font names

# Streamlit App
st.title("Multi-Language Translator")
st.subheader("Hello welcome to Abhishek's Multi-language translator here you can Target multiple languages:")

# Source and target language selection
source_lang = st.selectbox("Source Language", list(languages.values()))
target_lang = st.selectbox("Target Language", list(languages.values()))

# Text input field
text_area = st.text_area("Enter Text:", height=100)

# Translate button
if st.button("Translate"):
  if text_area:
    source_lang_code = [k for k, v in languages.items() if v == source_lang][0]
    target_lang_code = [k for k, v in languages.items() if v == target_lang][0]
    translated_text = translate(text_area, source_lang_code, target_lang_code)
    if translated_text:
      st.success("Translation Successful!")
      st.write(f"Translation ({target_lang}):", translated_text)
      st.markdown(f"<div style='font-family: {get_font(target_lang_code)};'> {translated_text} </div>", unsafe_allow_html=True)  # Attempt to set font
    else:
      st.error("Translation Failed.")
  else:
    st.warning("Please enter text to translate.")

# Display list of supported languages
st.subheader("Supported Languages:")
for lang_code, lang_name in languages.items():
  st.write(f"- {lang_name} ({lang_code})")
