from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

translator = Translator()
# Simplified transliteration function for demonstration purposes
def transliterate_to_roman(odia_text):
    mapping = {
    # Vowels
    'ଅ': 'a', 'ଆ': 'aa', 'ଇ': 'i', 'ଈ': 'ii', 'ଉ': 'u', 'ଊ': 'uu',
    'ଋ': 'ri', 'ୠ': 'rii', 'ଏ': 'e', 'ଐ': 'ai', 'ଓ': 'o', 'ଔ': 'au',

    # Vowel Diacritics
    'ା': 'aa', 'ି': 'i', 'ୀ': 'ii', 'ୁ': 'u', 'ୂ': 'uu',
    'ୃ': 'ri', 'େ': 'e', 'ୈ': 'ai', 'ୋ': 'o', 'ୌ': 'au',

    # Consonants
    'କ': 'k', 'ଖ': 'kh', 'ଗ': 'g', 'ଘ': 'gh', 'ଙ': 'ng',
    'ଚ': 'ch', 'ଛ': 'chh', 'ଜ': 'j', 'ଝ': 'jh', 'ଞ': 'ny',
    'ଟ': 'ṭ', 'ଠ': 'ṭh', 'ଡ': 'ḍ', 'ଢ': 'ḍh', 'ଣ': 'ṇ',
    'ତ': 't', 'ଥ': 'th', 'ଦ': 'd', 'ଧ': 'dh', 'ନ': 'n',
    'ପ': 'p', 'ଫ': 'ph', 'ବ': 'b', 'ଭ': 'bh', 'ମ': 'm',
    'ଯ': 'y', 'ର': 'r', 'ଲ': 'l', 'ଳ': 'ḷ', 'ଶ': 'sh',
    'ଷ': 'ṣ', 'ସ': 's', 'ହ': 'h',

    # Conjunct Consonants
    'କ୍ଷ': 'kṣ', 'ଜ୍ଞ': 'jñ', 'ଡ଼': 'ṛ', 'ଢ଼': 'ṛh',

    # Numerals
    '୦': '0', '୧': '1', '୨': '2', '୩': '3', '୪': '4',
    '୫': '5', '୬': '6', '୭': '7', '୮': '8', '୯': '9'
}

    return ''.join(mapping.get(char, char) for char in odia_text)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    input_text = data['text']
    translated = translator.translate(input_text, dest='or')
    print(translated.text)
    transliterated_text = transliterate_to_roman(translated.text)
    print(({'transliteratedText': transliterated_text}))
    return jsonify({'transliteratedText': transliterated_text,'oriyaText':translated.text})

if __name__ == '__main__':
    app.run(debug=True)
