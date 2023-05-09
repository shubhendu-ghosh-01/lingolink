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
        return render_template('index.html', translation=translation)
    else:
        return render_template('index.html')
    

tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
@app.route('/translate')
def translate():
    src_lang = request.args.get('src_lang')
    tgt_lang = request.args.get('tgt_lang')
    text = request.args.get('text')
    translator = pipeline(
        "translation",
        model=model,
        tokenizer=tokenizer,
        src_lang=src_lang,
        tgt_lang=tgt_lang,
    )
    
    output = translator(text, max_length=400)
    result = output[0]["translation_text"]
    return result

if __name__ == '__main__':
    app.run(debug=True)