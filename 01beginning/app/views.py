from flask import render_template, redirect, request, url_for
from app import app
from users import UserBase

@app.route('/home', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        # named = request.form.get['customer_name']
        named =request.form['customer_name']
        return render_template("thanks.html", named=named)
    else:
        return render_template("layout.html")



# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     named =request.form['customer_name']
#     return render_template("thanks.html",named=named)
#     # return "Hi"
        