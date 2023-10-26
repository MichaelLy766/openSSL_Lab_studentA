from cryptography.hazmat.primitives import serialization

# Specify the path to your private key PEM file
private_key_file = "private_key.pem"

# Read the private key from the PEM file
with open(private_key_file, "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Extract the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Specify the output file path for the public key
output_file = "public_key.pem"

# Export the public key to a file
with open(output_file, "wb") as f:
    f.write(public_key_pem)

print(f"Public key extracted from '{private_key_file}' and exported to '{output_file}'.")


