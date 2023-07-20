import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
docs = db.collection(u'signatures').stream()
docs_copy=[]
for doc in docs:
    docs_copy.append(doc.to_dict())
print(docs_copy)
with open("public_key.pem", "rb") as key_file:
    print("aata")
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )
    print(public_key)




for signature_doc in docs_copy:
    signature = signature_doc["signature"]
    message = b"example message"
    try:
        # Verify the signature with the public key
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        print("Signature is valid")
    except InvalidSignature:
        print("Signature is invalid")
    print(signature)