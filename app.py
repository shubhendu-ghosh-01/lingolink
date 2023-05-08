from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        from_lang = request.form['from_lang']
        to_lang = request.form['to_lang']
        text = request.form['text']
        translation = translate(from_lang, to_lang, text)
        return render_template('home.html', translation=translation)
    else:
        return render_template('home.html')

def translate(from_lang, to_lang, text):
    # Replace with your AI translation API endpoint
    url = 'https://your-translation-service.com/translate'
    payload = {'from_lang': from_lang, 'to_lang': to_lang, 'text': text}
    response = requests.post(url, json=payload)
    return response.json()['translation']

if __name__ == '__main__':
    app.run(debug=True)
