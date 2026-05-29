from flask import Flask, render_template, request,redirect
import mysql.connector
from dotenv import load_dotenv
import os
import requests
import re
from datetime import datetime, date
import joblib
import numpy as np


load_dotenv()

app = Flask(__name__)

#Mysql Connection
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT"))
)
cursor = db.cursor()

#Prediction Condition
model = joblib.load("health_model.pkl")

def predict_health(glucose, haemoglobin, cholesterol):

    data = np.array([[glucose, haemoglobin, cholesterol]])
    result = model.predict(data)[0]

    mapping = {
        0: "Normal",
        1: "High Risk (Diabetes/Cholesterol)",
        2: "Possible Anemia",
        3: "Borderline Risk"
    }

    return mapping.get(result, "Unknown")

# Routes
@app.route("/")
def index():
    cursor.execute("SELECT * FROM patients ORDER BY id DESC")
    data = cursor.fetchall()
    #to debug whether data is retrieve or not
    # for row in data:
    #     print(row)
    #
    # exit()
    today = date.today().strftime("%Y-%m-%d")
    return render_template("index.html", patients=data, today=today)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    dob = request.form["dob"]
    email = request.form["email"]

    glucose = request.form.get("glucose")
    haemoglobin = request.form.get("haemoglobin")
    cholesterol = request.form.get("cholesterol")

    errors = {}
    # Name validation
    if not name.replace(" ", "").isalpha():
        errors["name"] = "Name must contain only letters"

    # Email validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        errors["email"] = "Invalid email format"

    # DOB validation
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        if dob_date > datetime.now():
            errors["dob"] = "DOB cannot be future"
    except:
        errors["dob"] = "Invalid date"

    # Numeric validation
    try:
        glucose = float(glucose)
    except:
        errors["glucose"] = "Must be number"

    try:
        haemoglobin = float(haemoglobin)
    except:
        errors["haemoglobin"] = "Must be number"

    try:
        cholesterol = float(cholesterol)
    except:
        errors["cholesterol"] = "Must be number"

    # if error
    if errors:
        cursor.execute("SELECT * FROM patients ORDER BY id DESC")
        data = cursor.fetchall()

        today = date.today().strftime("%Y-%m-%d")

        return render_template(
            "index.html",
            errors=errors,
            old=request.form,
            patients=data,
            today=today
        )

    # Prediction
    remarks = predict_health(glucose, haemoglobin, cholesterol)

    cursor.execute("""
        INSERT INTO patients
        (name, dob, email, glucose, haemoglobin, cholesterol, remarks)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, dob, email, glucose, haemoglobin, cholesterol, remarks))

    db.commit()

    return redirect("/")


@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    name = request.form["name"]
    dob = request.form["dob"]
    email = request.form["email"]

    glucose = request.form.get("glucose")
    haemoglobin = request.form.get("haemoglobin")
    cholesterol = request.form.get("cholesterol")

    errors = {}

    # Name validation
    if not name.replace(" ", "").isalpha():
        errors["name"] = "Name must contain only letters"

    # Email validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        errors["email"] = "Invalid email format"

    # DOB validation
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        if dob_date > datetime.now():
            errors["dob"] = "DOB cannot be future"
    except:
        errors["dob"] = "Invalid date"

    # Numeric validation
    try:
        glucose = float(glucose)
    except:
        errors["glucose"] = "Must be number"

    try:
        haemoglobin = float(haemoglobin)
    except:
        errors["haemoglobin"] = "Must be number"

    try:
        cholesterol = float(cholesterol)
    except:
        errors["cholesterol"] = "Must be number"

    # If error → reload page
    if errors:
        cursor.execute("SELECT * FROM patients ORDER BY id DESC")
        data = cursor.fetchall()

        today = date.today().strftime("%Y-%m-%d")

        return render_template(
            "index.html",
            errors=errors,
            patients=data,
            today=today
        )

    # OPTIONAL: recalculate remarks (recommended)
    remarks = predict_health(glucose, haemoglobin, cholesterol)

    cursor.execute("""
        UPDATE patients
        SET name=%s,
            dob=%s,
            email=%s,
            glucose=%s,
            haemoglobin=%s,
            cholesterol=%s,
            remarks=%s
        WHERE id=%s
    """, (name, dob, email, glucose, haemoglobin, cholesterol, remarks, id))

    db.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM patients WHERE id=%s", (id,))
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
