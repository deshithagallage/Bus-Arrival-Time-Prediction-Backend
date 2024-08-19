import firebase_admin
from firebase_admin import credentials, firestore, db, storage

def init_firebase():
    # Initialize Firebase app with service account credentials
    cred = credentials.Certificate("app/core/firebase_credentials.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://urban-eta-default-rtdb.asia-southeast1.firebasedatabase.app/',  # Realtime Database URL
        'storageBucket': 'gs://urban-eta.appspot.com'  # Storage bucket URL
    })

# Initialize Firebase
init_firebase()

# Firestore client
firestore_db = firestore.client()

# Realtime Database client
realtime_db = db.reference()

# Firebase Storage client
storage_bucket = storage.bucket()
