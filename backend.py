from flask import Flask, render_template, request
from brain import get_response
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    cevap = ""
    mesaj = ""

    if request.method == "POST":
        mesaj = request.form.get("message")

        if mesaj:
            cevap = get_response(mesaj)
        else:
            cevap = "Bir sey yaz."

    return render_template("index.html", cevap=cevap, mesaj=mesaj)

# Render / Railway uyumlu
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
