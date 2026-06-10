from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def my_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template("thankyou.html")
    else:
        return "Something went wrong. Try again!"