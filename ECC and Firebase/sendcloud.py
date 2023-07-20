import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
# add service account key 
# you can take help of https://sharma-vikashkr.medium.com/firebase-how-to-setup-a-firebase-service-account-836a70bb6646
firebase_admin.initialize_app(cred)
db = firestore.client()
print(db)

# Load the private key from file
with open("private_key.pem", "rb") as key_file:
    print("aata")
    private_key_pem = key_file.read()

# Deserialize the private key from PEM format
private_key = load_pem_private_key(
    private_key_pem,
    password=None
)

# Define the message to sign
message = b"example message"

# Sign the message with the private key
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# Store the signature in Firebase
signature_data = {
    "signature": signature
}
try:
    db.collection("signatures").add(signature_data)
    print("signature added")
except:
    print("error")
