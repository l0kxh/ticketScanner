import firebase_admin
from firebase_admin import credentials, firestore
import qrcode
import os

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./serviceAccountKey.json")  # Update with your service account key
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to generate QR code for a given data
def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Generate 4000 QR codes
output_dir = "extra_qr_codes_count_0"
os.makedirs(output_dir, exist_ok=True)

for i in range(1200, 1500):
    # Generate unique ID for Firebase document
    doc_ref = db.collection("qrcodes").document()
    doc_ref.set({"checkout": "false", "count":0})  # Set data as needed

    # Get the document ID
    doc_id = doc_ref.id

    # Generate QR code with the document ID
    qr_filename = os.path.join(output_dir, f"qr_code_{i+1}.png")
    generate_qr(doc_id, qr_filename)

print("QR codes generated successfully!")
