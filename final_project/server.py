import machinetranslation
from flask import Flask, render_template, request
from machinetranslation.translator import englishToFrench, frenchToEnglish

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrenchEndpoint():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = englishToFrench(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglishEndpoint():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = frenchToEnglish(textToTranslate)
    return translated_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
