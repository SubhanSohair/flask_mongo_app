from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()
CON_STRING =  os.getenv('CON_STRING')

client = MongoClient(CON_STRING)

db = client.get_database('ReviewDB')

reviews_collection = db.get_collection('reviews')


# Save Review
def save_review(username, review):
    reviews_collection.insert_one({'username': username, 'review': review})


def load_reviews():
    reviews = list(reviews_collection.find())
    return reviews

print(CON_STRING)