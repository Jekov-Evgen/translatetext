from flask import Flask, render_template, request
from Logic.translate import text_translation

app = Flask(__name__)

@app.route('/')
def trans():
    return render_template("home.html")

@app.route("/res", methods=['POST'])
def result():
    text = request.form['translate_text']
    language = request.form['lang']
    res = text_translation(text=text, lan=language)
    
    return render_template('res.html', res=res)

if __name__ == "__main__":
    app.run(debug=True)

