from flask import Flask, render_template, url_for
from app.forms import myForm
from app import app 


@app.route('/home', methods=['GET','POST'])
def home():     
    form = myForm()
    if form.validate_on_submit():
        return "Hello {}".format(form.username.data)   
    return render_template('index.html', form=form)