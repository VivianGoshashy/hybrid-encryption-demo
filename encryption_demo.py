# Scenario

# A Finance department must securely transfer a confidential acquisition report to the organization's legal review team.
# Because the document contains sensitive business information the security engineer implements a hybrid cryptographic workflow.
# AES symmetric encryption protects the report contents, while RSA asymmetric encryption securely protects the AES session key during transmission.
# The workflow simulate how secure enterprise communication systems protect confidentisl business data.

# Objective
# 1. Create and securely encrypt a confidential enterprise document using AES symmetric encryption.
# 2. Generate RSA public/private keys and use them to securely protect and recover the AES encryption key.
# 3. Decrypt and validate the original document while producing terminal-ready encryption workflow outputs.


# importing libraries
from cryptography.fernet import Fernet # encrypt and decrypt with the same key
from cryptography.hazmat.primitives.asymmetric import rsa, padding 
from cryptography.hazmat.primitives import hashes # provides cryptographic hash functions
from tabulate import tabulate # creates formatted tables for output display
from pathlib import Path # file system paths
import hashlib # built-in hashing algorithms
from datetime import datetime


# creating a working directory inside PQC
base_dir = Path(__file__).parent # current directory (PQC)
docs_dir = base_dir / "encrypted_docs"

# creating confidential finance report inside doc_dir directory
report = docs_dir / "finance_report.txt"

# writing report content
report_content = """
CONFIDENTIAL FINANCE REPORT
----------------------------------------
Target Company:Quantum Analytics
Established Acquisition Value: $24 Million
Legal Review Status: Pending
Internal Classification: Restricted
Date: {date}
----------------------------------------
This document contains privileged and confidential 
information. Unauthorized disclosure is prohibited.
"""

# Format with current date
report_content = report_content.format(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# write the report
report.write_text(report_content)

# Encrypting the document using AES symmetric encryption key
# Generating AES symmetric encrypted key
aes_key = Fernet.generate_key()
aes_cipher = Fernet(aes_key)

# Encrypting Finance report using AES key generated
original_data = report.read_bytes() # reads the report as a bytes
encrypted_report = aes_cipher.encrypt(original_data) # encrypts the report using AES encryption
encrypted_report_path = base_dir / "finance_report.encrypted" # creates a path where to save the encrypted file
encrypted_report_path.write_bytes(encrypted_report) # saves the encrypted report to a file

# Now that the document is encryoted, it needs to be transfered to the legal team.
# However, we need to encrypt the AES symmetric encryption key using RSA asymmetric encryption dueing transmission
# Generate RSA public/private key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048) # generates a private key for RSA asymmetric encryption
public_key = private_key.public_key() # extracts the public key from the private key

# Encrypt AES key using RSA pubilc key
encrypted_aes_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
) # encrypts the AES key using the RSA public key

encrypted_key_path = base_dir / "aes_key.secure" # creates a file path for storing the encrypted AES key
encrypted_key_path.write_bytes(encrypted_aes_key) # saves the encrypted AES key to a file

# Recover AES key using RSA private key
recovered_aes_key = private_key.decrypt(
    encrypted_aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# For the legal team to read the report, they need correct key.
recovered_cipher = Fernet(recovered_aes_key)
decrypt_report = recovered_cipher.decrypt(encrypted_report)

decrypt_report_path = base_dir / "finance_report_recovered.txt"
decrypt_report_path.write_bytes(decrypt_report)

print(decrypt_report.decode())

# Validating report integrity
original_hash = hashlib.sha256(original_data).hexdigest()
recovered_hash = hashlib.sha256(decrypt_report).hexdigest()

validation = [
    ["Original Report Hash", original_hash],
    ["Recovered Report Hash", recovered_hash]
]



print(tabulate(
    validation,
    headers=["Artifact", "SHA-256 Hash"],
    tablefmt = "grid"
))