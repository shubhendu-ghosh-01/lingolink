from flask import Flask, render_template, request
import requests
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        src_lang = request.form['src_lang']
        tgt_lang = request.form['tgt_lang']
        text = request.form['text']
        translation = translate(src_lang, tgt_lang, text)
        return render_template('home.html', translation=translation)
    else:
        return render_template('home.html')
    

tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")

def translate(tgt_lang, src_lang, text):
    translator = pipeline(
        "translation",
        model=model,
        tokenizer=tokenizer,
        src_lang=src_lang,
        tgt_lang=tgt_lang,
    )

    output = translator(text, max_length=400)
    output = output[0]["translation_text"]
    return output

if __name__ == '__main__':
    app.run(debug=True)
