"""
    Web development Project

    Kyriakos Giannakis - P14021
    Panagiotis Efstathiadis - P14042
    Basilis Zwgrafos - P14050
    Mprazitikos Kwnstantinos - P14123
"""
from flask import Flask, session, redirect, request, render_template, url_for
import Program as p
app = Flask(__name__)
from db_operations import TryLogin, getUidFromUsername, getPrograms, getUserProp, insertProgram, deleteProgram

import random
random = random.SystemRandom()



##### Random Secret Key Generation #####

def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(allowed_chars) for i in range(length))

def get_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)

app.secret_key = get_secret_key()

#Check if logged in user is admin
def isAdmin():
    if session["accesslvl"] == 3:
        return True
    else:
        return False

##### Session error resetters #####

def resetLoginErrors():
    session["login_error"] = None
    return ""

def resetProgramAddErrors():
    session["program_add_err"] = None
    return ""

##### Routes #####

#Index route. Temporarily redirects to the programs route.
@app.route("/")
def hello():
    if "login" in session:
        return redirect("/programs/view")
    else:
        return render_template("login.html", session=session, resetLoginErrors=resetLoginErrors)

#Login processing
@app.route("/login_action", methods=["POST"])
def login_action():
    if request.form["username"] != None and request.form["password"]:
        if TryLogin(request.form["username"], request.form["password"]):
            print "Logged in!"
            session["login_uid"] = getUidFromUsername(request.form["username"])
            session["accesslvl"] = getUserProp(getUidFromUsername(request.form["username"]))
            return redirect("/programs/view")
        else:
            session["login_error"] = 2
            return redirect("/")
    else:
        session["login_error"] = 1
        return redirect("/")

#Programs Viewing route
@app.route("/programs/view")
def view_programs():
    if "login_uid" in session:
        if getUserProp(session["login_uid"]) >= 1:
            return render_template("programs.html", getPrograms=getPrograms, isAdmin=isAdmin, session=session)
    else:
        return redirect("/")

#Program adding route
@app.route("/programs/add", methods=["POST", "GET"])
def add_program():
    if "login_uid" in session:
        if getUserProp(session["login_uid"]) == 3:
            if request.method == "GET":
                return render_template("add_program.html", resetProgramAddErrors=resetProgramAddErrors)
            elif request.method == "POST":
                #TODO Add verification
                newTitle = request.form["title"]
                newDesc = request.form["description"]
                newCost = request.form["cost"]
                try:
                    newProgram = p.Program(newTitle, newDesc, newCost)
                except ValueError:
                    session["program_add_err"] = 1
                    #TODO Display error from template
                    return redirect("/programs/add")
                if insertProgram(newProgram):
                    return redirect("/programs/view")
                else:
                    session["program_add_err"] = 2
                    return redirect("/programs/add")
    else:
        return redirect("/")

#Program removing route
@app.route("/programs/remove", methods=["GET"])
def del_Prog():
    if "login_uid" in session:
        if isAdmin():
            deleteProgram(request.args.get("id", ""))
            return redirect("/programs/view")
    else:
        return redirect("/")

"""
    No logout functionality has been added yet. Will be added to the final project.
"""

if __name__ == "__main__":
    app.run(debug=True, host="localhost")
