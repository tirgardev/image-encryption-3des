# image-encryption-3des
Mini Project: Image Encryption using Triple DES in Python 


```markdown
# 🔐 Image Encryption using Triple DES (3DES)

This mini project demonstrates how to encrypt and decrypt image files using the **Triple DES (3DES)** encryption algorithm in Python. It supports all image types (JPG, PNG, BMP, etc.) and any file size.

---

## 📁 Project Structure

```
image-encryption-3des/
│
├── input_image.jpg           # Original image (any type: PNG/JPG)
├── encrypted_image.jpg       # Encrypted image (looks corrupted)
├── decrypted_image.jpg       # Decrypted image (matches original)
├── image_encryptor.py        # Main Python script
└── README.md                 # This file
```

---

## ⚙️ How It Works

1. The image is read as raw binary data.
2. Data is encrypted using Triple DES (3DES) with a 24-byte key.
3. Encrypted data is saved as `encrypted_image.jpg`.
4. The script decrypts that encrypted file.
5. Output is saved as `decrypted_image.jpg`.

✅ The decrypted image should look **exactly like the original.**

---

## 🔧 Requirements

Install Python packages with:

```bash
pip install pillow pyDes
```

---

## 🛠️ How to Run

1. Place your input image as `input_image.jpg` in the project folder.
2. Open terminal and run the script:

```bash
python image_encryptor.py
```

---

## 🔐 Encryption Details

- **Algorithm**: Triple DES (3DES)
- **Mode**: CBC (Cipher Block Chaining)
- **Padding**: PKCS5
- **Key Size**: 24 bytes (168 bits)
- **IV Size**: 8 bytes

We use the `pyDes` Python module to perform encryption and decryption.

---

## 📸 Output

- `encrypted_image.jpg`: Cannot be opened as a normal image (it's encrypted).
- `decrypted_image.jpg`: Should open and look exactly like your original image.

---

## 👨‍💻 Author

- **Name**: [Tirgar Dev Sureshbhai]
- **College**: [Madhuben and Bhanubhai Patel Institute Of Technology (MBIT)]
- **Course**: Information and Network Security (INS)
- **Mini Project Title**: Image Encryption Using Triple DES

---

## 🧾 License

This project is created for educational use only. You are free to use and modify it for your learning purposes.

---

