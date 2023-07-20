from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate a new ECC private key
private_key = ec.generate_private_key(ec.SECP256R1())

# Serialize the private key in PEM format
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Serialize the public key in PEM format
public_key_pem = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save the private key and public key to files
with open('private_key.pem', 'wb') as f:
    f.write(private_key_pem)

with open('public_key.pem', 'wb') as f:
    f.write(public_key_pem)


print("private key:\n",private_key_pem)
print("public key\n",public_key_pem)