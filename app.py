from flask import Flask, render_template, request
import requests
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route('/', methods=['GET', 'POST'])
def home():
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