from flask import flask, render_template
app = flask(__name__)

#app.py #/template/
@app.route("/")
def index():
    return render_template("index.html")
