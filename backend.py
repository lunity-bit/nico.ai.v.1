from flask import Flask, render_template, request
from brain import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    cevap = ""
    mesaj = ""

    if request.method == "POST":
        mesaj = request.form.get("message")
        cevap = get_response(mesaj)

    return render_template("index.html", cevap=cevap, mesaj=mesaj)

if __name__ == "__main__":
    app.run(debug=True)