from flask import Flask
from flask import render_template
import templates

app = Flask(__name__)

class_roster = [("Sam" , "A", "Sophomore"),
                ("Stevie","B", "Freshman"),
                ("Arly","C","Senior"),
                ("Bodan", "A", "Sophomore"),
                ("Mike", "B","Freshman")
                ("Lauren","D","Senior")
                ("Joseph","A","Senior")]

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/welcome/<string:student_name>/')
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)


@app.route('/roster/<int:grade_view>/')
def roster(grade_roster):

    return render_template("roster.html", class_roster= class_roster, grade_view=grade_view)

if __name__ == '__main__':
    app.run()
