# Secure-Communication
Secure Communication: ECC Text Encryption and Image Encryption Time Correlation with Size using Fernet
<br>
[Project Report ](https://www.canva.com/design/DAFhXh-VpqQ/XuQc0WD5S_YI3PCDWEbaEg/view?utm_content=DAFhXh-VpqQ&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)




**Objective:** Your goal is to write a comprehensive README file for the "Secure-Communication" project on GitHub. The project consists of two parts: ECC Text Encryption and Image Encryption using the Fernet method. The first part involves ECC text encryption and decryption, while the second part deals with image encryption and decryption.

### Part 1: ECC Text Encryption and Decryption with Firebase

#### 1. ECC Text Encryption:

In this part of the project, we utilize the ECC (Elliptic Curve Cryptography) algorithm to encrypt text data securely. The ECC keys are generated, and the private key is serialized in PEM format, ensuring proper encryption and security.

```python
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

print("private key:\n", private_key_pem)
print("public key\n", public_key_pem)

```

#### 2. Firebase Integration

To store the encrypted text data, we integrate the project with Firebase, a cloud-based database solution. The serviceAccountKey.json file is used to initialize Firebase, ensuring secure access and authentication.

```python
# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
print(db)

```
#### 3. ECC Text Decryption

The encrypted text signatures are retrieved from Firebase, and the ECC private key is used to verify and decrypt the data securely.

```python
# Load the private key from file
with open("private_key.pem", "rb") as key_file:
    private_key_pem = key_file.read()

# Deserialize the private key from PEM format
private_key = load_pem_private_key(
    private_key_pem,
    password=None
)

# Verify and Decrypt the ECC signatures
# ...

# Signature Verification and Decryption
# ...

```
### Part 2: Image Encryption using Fernet Method

#### 1. Image Encryption using Fernet

In this part, we utilize the Fernet method for image encryption. A new Fernet key is generated, which is used to encrypt and save the images. The encryption time for each image is recorded.


```python
# Function to encrypt the image
# ...

# Generate a new Fernet key
# ...

# Encrypt the image and record encryption time
# ...


#### 2. Image Decryption using Fernet
```
To decrypt the encrypted images, the Fernet key is loaded, and the images are decrypted.


```python
# Function to decrypt the image
# ...

# Load the Fernet key
# ...

# Decrypt the images
# ...
```

#### 3. Correlation Analysis

The project performs a correlation analysis between image/file size and encryption time to evaluate the encryption performance.


```python
# Correlation analysis between image size and encryption time
# ...

# Correlation analysis between file size and encryption time
# ...
```

### Conclusion

This project aims to demonstrate secure communication through ECC text encryption and Fernet-based image encryption. It offers a robust and reliable solution for protecting sensitive data during communication. Feel free to contribute to the project or report any issues to make it better!

### Conclusion

This project aims to demonstrate secure communication through ECC text encryption and Fernet-based image encryption. It offers a robust and reliable solution for protecting sensitive data during communication. Feel free to contribute to the project or report any issues to make it better!
