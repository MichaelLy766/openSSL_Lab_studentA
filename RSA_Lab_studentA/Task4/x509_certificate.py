from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Load the certificate from file
with open('server-cert.pem', 'rb') as cert_file:
    cert_data = cert_file.read()

cert = x509.load_pem_x509_certificate(cert_data, default_backend())

# Display certificate details
print("Certificate Subject: ", cert.subject)
print("Issuer: ", cert.issuer)
print("Serial Number: ", cert.serial_number)
print("Valid From: ", cert.not_valid_before)
print("Valid Until: ", cert.not_valid_after)

# Check certificate expiration
from datetime import datetime

current_time = datetime.utcnow()
if current_time > cert.not_valid_after:
    print("Certificate has expired.")
else:
    print("Certificate is still valid.")
