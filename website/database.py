from google.cloud import firestore

db = firestore.Client.from_service_account_json("secrets\\firestore.json")