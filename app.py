from flask import Flask, render_template, request
from db import save_review, load_reviews


app = Flask(__name__)
app.secret_key = "subi"

# Home Page
@app.route("/")
def hello_world():
    return render_template("index.html")

# QR Page
@app.route("/qr")
def qr():
    return render_template("qr.html")

# Review Submitted Page
@app.route("/review_submitted", methods = ['POST','GET'])
def review_submitted():
    data = request.form
    # print(data['username'])
    # print(data['message'])
    save_review(data['username'], data['message'])

    return render_template("review_submitted.html")

# Reviews Page
@app.route("/reviews")
def reviews():
    reviews = load_reviews()  # Assuming you have a function to load reviews from the database
    return render_template("reviews.html", reviews=reviews)

