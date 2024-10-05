import os
import json
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore, db, storage


# Load environment variables from .env file
load_dotenv()


def init_firebase():
    # Get Firebase credentials from the environment variable
    firebase_creds = os.getenv('FIREBASE_CREDENTIALS')

    # Parse the credentials into a dictionary
    cred_dict = json.loads(firebase_creds)

    # Initialize Firebase app with the parsed credentials
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),  # Realtime Database URL
        'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET')  # Storage bucket URL
    })

# Initialize Firebase
init_firebase()

# Firestore client
firestore_db = firestore.client()

# Realtime Database client
realtime_db = db.reference()

# Firebase Storage client
storage_bucket = storage.bucket()
