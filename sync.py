import os
import pyrebase
import json
from dotenv import load_dotenv, find_dotenv
from gocard_scraper import GoCardScraper
from myki_scraper import MykiScraper

load_dotenv(find_dotenv())

config = {
    'apiKey': os.environ['FIREBASE_API_KEY'],
    'authDomain': os.environ['FIREBASE_AUTH_DOMAIN'],
    'databaseURL': os.environ['FIREBASE_DATABASE_URL'],
    'storageBucket': os.environ['FIREBASE_STORAGE_BUCKET'],
    'serviceAccount': json.loads(os.environ['FIREBASE_PRIVATE_KEY'])
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
gocards = GoCardScraper().execute()
mykis = MykiScraper().execute()
cards = gocards + mykis
for card in cards:
    key = "{}-{}".format(card.provider, card.number)
    db.child('cards').child(key).set(card.to_dict())
