import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Reference to your collection
collection_ref = db.collection("qrcodes")
query = collection_ref.where("checkout", "==", "true")
docs = query.stream()
zero_count = 0
one_count = 0
for doc in docs:
    if doc.to_dict()["count"]==0:
        zero_count+=1
    else:
        one_count+=1
print(zero_count)
print(one_count)