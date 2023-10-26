from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

# Load Student B's public key from the PEM file
public_key_file = "public_key_studentB.pem"
with open(public_key_file, "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Specify the path to the plaintext file
plaintext_file = "plaintext.txt"

# Read the plaintext data from the file
with open(plaintext_file, "rb") as f:
    plaintext_data = f.read()

# Encrypt the plaintext using Student B's public key
ciphertext = public_key.encrypt(
    plaintext_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Specify the output file path for the encrypted data
encrypted_file = "encrypted_text.enc"

# Write the encrypted data to the output file
with open(encrypted_file, "wb") as f:
    f.write(ciphertext)

print(f"Text file encrypted and saved as '{encrypted_file}'.")