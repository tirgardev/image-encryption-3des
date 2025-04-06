import os
import time
import mimetypes
from PIL import Image
import pyDes

# Function to read image as binary
def image_to_binary(image_path):
    with open(image_path, 'rb') as file:
        return file.read()

# Function to write binary to an image file
def binary_to_image(binary_data, output_path):
    with open(output_path, 'wb') as file:
        file.write(binary_data)

# Get file extension and validate image type
def get_file_extension(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type and mime_type.startswith("image/"):
        return os.path.splitext(file_path)[1]
    else:
        raise ValueError("Unsupported or non-image file.")

# Set your input image file here
input_image = "input_image.jpg"  # Make sure the image exists in the same folder

# Validate and get extension
image_ext = get_file_extension(input_image)

# Triple DES Key and IV Setup
key = b"1234567890abcdef12345678"   # 24-byte key
iv = b"\0\0\0\0\0\0\0\0"            # 8-byte IV
cipher = pyDes.triple_des(key, pyDes.CBC, iv, padmode=pyDes.PAD_PKCS5)

# Encrypt and Decrypt process
start = time.time()
print("Reading original image...")
original_data = image_to_binary(input_image)

print("Encrypting...")
encrypted_data = cipher.encrypt(original_data)
encrypted_file = "encrypted_image" + image_ext
binary_to_image(encrypted_data, encrypted_file)
print("Encrypted image saved as:", encrypted_file)

print("Decrypting...")
decrypted_data = cipher.decrypt(encrypted_data)
decrypted_file = "decrypted_image" + image_ext
binary_to_image(decrypted_data, decrypted_file)
print("Decrypted image saved as:", decrypted_file)

elapsed = time.time() - start
print("Total time taken: %.2f seconds" % elapsed)

# Optional: show images using default viewer
try:
    img1 = Image.open(input_image)
    img1.show(title="Original Image")

    img2 = Image.open(decrypted_file)
    img2.show(title="Decrypted Image")
except Exception as e:
    print("Image preview not supported:", e)
