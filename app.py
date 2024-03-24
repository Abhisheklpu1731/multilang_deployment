from flask import Flask, render_template, request
from mtranslate import translate as mtranslate_translate

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['POST'])
def translate_text():
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    text = request.form['text']
    
    source_lang_code = [k for k, v in languages.items() if v == source_lang][0]
    target_lang_code = [k for k, v in languages.items() if v == target_lang][0]
    translated_text = translate(text, source_lang_code, target_lang_code)
    
    if translated_text:
        return render_template('index.html', languages=languages, translated_text=translated_text, font=get_font(target_lang_code))
    else:
        return render_template('index.html', languages=languages, error_message="Translation Failed.")


