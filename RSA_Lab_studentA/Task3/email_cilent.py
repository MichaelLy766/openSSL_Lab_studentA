import smtplib
from email.message import EmailMessage
from cryptography.hazmat.primitives import serialization

# Load User A's private key
with open("user_a_private.pem", "rb") as key_file:
    user_a_private_key = serialization.load_pem_private_key(key_file.read(), password=None)

# Create an email message
message = EmailMessage()
message.set_content("This is a secure email message.")
message["Subject"] = "Secure Email"
message["From"] = "user_a@example.com"
message["To"] = "user_b@example.com"

# Sign the email
message.add_alternative("This is a secure email message.", subtype="plain")
message.sign(user_a_private_key)

# Connect to the SMTP server and send the email
with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()  # Use TLS for encryption
    server.login("user_a@example.com", "user_a_password")
    server.send_message(message)

print("Email sent securely from User A to User B.")
