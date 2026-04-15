from flask import Flask, render_template, request
from brain import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    cevap = ""

    if request.method == "POST":
        mesaj = request.form.get("message")
        cevap = get_response(mesaj)

    return render_template("index.html", cevap=cevap)

# 🔥 Render için gerekli kısım
import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
