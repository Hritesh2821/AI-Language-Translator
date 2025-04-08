from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    lang = request.form['language']
    result = translator.translate(text, dest=lang)
    return f"<h2>Translated Text:</h2><p>{result.text}</p><br><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
