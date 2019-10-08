from flask import Flask, render_template, request, url_for, redirect
from app import app
from app.model import Applicants

all_applicants = []

@app.route('/', methods = ['GET'])
def home():
    return render_template("index.html")

@app.route('/applicant_list')
def reg_list():
    return render_template("a_list.html", all_applicants=all_applicants)


@app.route('/register', methods=['POST'])
def registration():
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    gender = request.form.get("gender")
    drive = request.form.get("drive")
    if not first_name or not last_name or not gender or not drive:
        return render_template("error.html")
    p = Applicants(first_name, last_name, gender, drive)
    all_applicants.append(p.__repr__())
    return redirect(url_for('reg_list'))



