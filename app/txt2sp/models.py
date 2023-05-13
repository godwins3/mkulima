from flask import current_app
from flask_pymongo import PyMongo

mongo = PyMongo(current_app)

class Text:
    def __init__(self, text):
        self.text = text

    def save(self):
        texts = mongo.db.texts
        texts.insert_one({
            'text': self.text
        })

    @classmethod
    def find_all(cls):
        texts = mongo.db.texts
        return texts.find()
