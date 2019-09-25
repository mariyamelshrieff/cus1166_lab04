from flask import flask, render_template
app = flask(__name__)

#app.py #/template/
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/ <string:student_name>")
def welcome (student_name):
    return render_template("welcome.html", student_name= student_name)


@app.route("/roster/<int:grade_view>")
def class_roster (grade_view):
    class_roster= [("John","A", "Sophomore"),
    ("Tom","B","Junior"), ("Sam","C","Senior"), ("Arly","D","Freshman"), ("Stevie","A", "Freshman")
    ("Sandra","A","Junior"), ("Maya","B","Senior"),("Mike","C","Senior"), ("Holly","A","Freshman")]

    return render_template ("roster.html",student_name=student_name,class_roster=class_roster)
