from flask import Flask, render_template, request, redirect, jsonify
from db import save_review, load_reviews, delete_all_reviews


app = Flask(__name__)
app.secret_key = "subi"

# Home Page
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/api/reviews")
def list_jobs():
    reviews = load_reviews()
    reviews_list = []
    for review in reviews:
        id = str(review['_id'])
        review = review['review'].strip()
        reviews_list.append({'id': id, 'review': review})

    return jsonify(reviews_list)


# QR Page
@app.route("/qr")
def qr():
    return render_template("qr.html")

# Review Submitted Page
@app.route("/review_submitted", methods = ['POST','GET'])
def review_submitted():
    data = request.form
    save_review(data['message'])
    return render_template("review_submitted.html")

# Reviews Page
@app.route("/reviews")
def reviews():
    reviews = load_reviews()
    return render_template("reviews.html", reviews=reviews)

# Delete All Reviews
@app.route("/delete_reviews")
def delete_reviews():
    delete_all_reviews()
    return redirect("/reviews")       