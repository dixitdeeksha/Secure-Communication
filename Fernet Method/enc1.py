import os
from cryptography.fernet import Fernet
# from datetime import datetime
import pandas as pd 
import time
# Function to encrypt the image
def encrypt_image(image_path, key):
    with open(image_path, 'rb') as file:
        original_data = file.read()
    
    encrypted_data = key.encrypt(original_data)
    return encrypted_data

# Function to decrypt the image
def decrypt_image(encrypted_data, key):
    decrypted_data = key.decrypt(encrypted_data)
    return decrypted_data

# Generate a new Fernet key

def enc(image_path,i):
    start_time=time.time()
# Encrypt the image
    encrypted_image = encrypt_image(image_path, f)
    endt_time=time.time()
    # print(encrypted_image)
    # Get the size of the image
    image_size = os.path.getsize(image_path)

    # Get the current date and time
    encryption_time = endt_time-start_time
    print("Image No",i ," Encription time=", encryption_time)
    # Create a dictionary to store the data
    data = {'Image Path': [image_path], 'Encrypted Image Path': ['encrypted_image.bin'], 'Image_Size': [image_size], 'Encryption_Time': [encryption_time]}
    bin_name="bin/encrypted_image_"+str(i)+".bin"
    # Save the encrypted data to a binary file
    with open(bin_name, 'wb') as file:
        file.write(encrypted_image)

    # Check if the Excel file exists
    if os.path.exists('encrypted_images.xlsx'):
        # Load the existing file
        existing_df = pd.read_excel('encrypted_images.xlsx')
        # Append the new data to the existing file
        updated_df = pd.concat([existing_df, pd.DataFrame(data)], ignore_index=True)
        # Write the updated data to the Excel file
        updated_df.to_excel('encrypted_images.xlsx', index=False)
    else:
        # Write the data to a new Excel file
        pd.DataFrame(data).to_excel('encrypted_images.xlsx', index=False)

    # Code to decrypt the image
    # Load the key from the file
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
        
    # Load the encrypted image from the binary file
    with open(bin_name, 'rb') as file:
        encrypted_image = file.read()


    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, Fernet(key))

    # Save the decrypted image to a file
    dest_name="decrypted_image/"+str(i)+".jpg"
    with open(dest_name, 'wb') as file:
        file.write(decrypted_image)
    print("done")






key = Fernet.generate_key()

# Save the key to a file
with open("key.key", "wb") as key_file:
    key_file.write(key)

# Create the Fernet object
f = Fernet(key)
for i in range(1,56):
# Get the image path from user input
    path = "images/"+str(i)+".jpg"
    enc(path,i)
print("code done")