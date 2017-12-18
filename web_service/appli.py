import csv
from datetime import date
from flask import Flask, render_template, make_response, url_for
from data import DATA_DIR

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/notifications")
def notif():
    today = date.today().strftime("%d-%B-%Y")
    try:
        with open(DATA_DIR + "/Historique_des_logs/historique{}.csv".format(today), "r") as file:
            data = ["    ".join(row) for row in csv.reader(file, delimiter=";")]
        return make_response("<br/>".join(data))
    except FileNotFoundError:
        return make_response("There is no historique.")
    #return render_template("pages/logs.csv")

def launchWebService():
    app.run(host='0.0.0.0', port=6666, debug=True)
