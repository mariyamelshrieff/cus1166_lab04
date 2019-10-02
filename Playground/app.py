from flask import Flask
from flask import render_template



app = Flask(__name__)
#Bootstrap(app)

class_roster = [("Sam" , "A", "Sophomore"),
                ("Stevie","B", "Freshman"),
                ("Arly","B","Senior"),
                ("Bodan", "A", "Sophomore"),
                ("Mike", "C","Freshman"),
                ("Lauren","C","Senior"),
                ("Joseph","A","Senior")]

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/welcome/<string:student_name>/')
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)


@app.route('/roster/<string:grade_view>/')
def roster(grade_view):

    return render_template("roster.html", class_roster = class_roster, grade_view = grade_view)
#For Running the app
if __name__ == '__main__':
    app.run(debug=true)
