import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from getwords import get_common_words

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route("/")
def index():
    print "Index time!"
    return render_template("index.html")

@app.route("/form_submit", methods=["POST"])
def form_submit():
    url = request.form["url"]
    data = get_common_words(url)
    labels, values = zip(*sorted(data.items(), key=lambda x: x[1]))
    labels = [repr(s)[2:-1].lower() for s in labels]
    print "Got Data!"
    print labels
    print values
    return render_template("index.html",
                           url=url,
                           labels=list(labels),
                           values=list(values))

if __name__ == "__main__":
   app.run()
