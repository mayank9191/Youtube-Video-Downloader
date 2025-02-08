from flask import Flask, render_template,  redirect, request
from Search import listvideo

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        name = request.form["video_name"]

        video_list = listvideo(name)

        return render_template("index1.html", list=video_list)

    return render_template("index1.html")


if __name__ == "__main__":
    app.run(debug=True)
