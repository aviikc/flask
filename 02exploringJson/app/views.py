import json
import os
from flask import Flask, jsonify, render_template, request
from app.quote_maker import QuoteMaker
from app import app

my_quote = QuoteMaker()

@app.route('/home', methods = ['GET'])
def home():
    quote = my_quote.random_quote().get("text")
    author = my_quote.random_quote().get("from")
    return render_template("layout.html", quote=quote, author=author)

