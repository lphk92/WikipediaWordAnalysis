from flask import Flask, render_template, request, url_for

app = Flask(__name__)

def get_word_data(url):
    return {"a": 100, "the": 125}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form_submit", methods=["POST"])
def form_submit():
    url = request.form["url"]
    data = sorted(get_word_data(url))
    print data
    return "Success!"
    return render_template("index.html",
                           labels=data.keys(),
                           values=data.values())
