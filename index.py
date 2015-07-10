from flask import Flask, render_template, request, url_for

from getwords import get_common_words

app = Flask(__name__)

#def get_word_data(url):
    #return {"a": 100, "the": 125}

@app.route("/")
def index():
    print "Index time!"
    return render_template("index.html")

@app.route("/form_submit", methods=["POST"])
def form_submit():
    url = request.form["url"]
    data = get_common_words(url)
    data = {str(k): data[k] for k in data}
    print "Got Data!"
    print data
    return render_template("index.html",
                           url=url,
                           labels=data.keys(),
                           values=data.values())

if __name__ == "__main__":
   app.run()
