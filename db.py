from pymongo import MongoClient

client = MongoClient("mongodb+srv://subi:subi@reviewapp.wgo96zx.mongodb.net/?retryWrites=true&w=majority&appName=ReviewApp")

db = client.get_database('ReviewDB')

reviews_collection = db.get_collection('reviews')


# Save Review
def save_review(review):
    reviews_collection.insert_one({'review': review})


def load_reviews():
    reviews = list(reviews_collection.find())
    return reviews
