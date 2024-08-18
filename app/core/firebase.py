import firebase_admin
from firebase_admin import credentials, firestore

def init_firebase():
    cred = credentials.Certificate("app/core/firebase_credentials.json")
    firebase_admin.initialize_app(cred)

# Initialize Firebase
init_firebase()

# Firestore client
db = firestore.client()
