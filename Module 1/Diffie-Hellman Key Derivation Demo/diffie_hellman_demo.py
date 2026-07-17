# Senario

# Two cloud-based enterprise systems must securely establish a shared secret over a public network without directly transmitting the secret itself.
# The engineer demostrates the Diffie-Hellman key excahneg process, where both systems independely derive the same shared secret using exchange public values.
# The workflow also highlights how the security of Diffie-Helman depends on the computational difficulty of solving the discrete logarithm problem.

# Objective
# 1. Generate Diffie-Hellma public parameters and exchange values
# 2. Derive a shared communication secret between two systems
# 3. Encrypt and decrypt enterprise sychronization data securely

# importing Libraries
from pathlib import Path
from tabulate import tabulate
from cryptography.fernet import Fernet
from datetime import datetime
import hashlib
import base64


# 1. Creating communication workspace
main_dir = Path(__file__).parent
docs_dir = main_dir / "encrypted file"
print(f"Communication workspace created: {docs_dir}\n")

# 2. System prepares confidential sync request
sync_request = """
ENTERPRISE ANALYTICS SYNCHRONIZATION
------------------------------------------
Region: Asia-Pacific
Replication Status: Enabled
Data Classification: Confidential
Sync Window: {timezone.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}
------------------------------------------
This synchronization request contains sensitive enterprise data.
Secure key exchange is required before transmission.
"""

# Creating confidential sync request inside doc_dir directory
request_file = docs_dir / "enterprise_sync_request.txt"
request_file.write_text(sync_request)
print("Confidential sync request created")
print(sync_request)

# 3. Public Diffie-Hellman parameters
# public value
p = int(input("\nInput a public Prime Modulus (p): ")) # modulus
g = int(input("Input a public Genrator value (g): ")) # Base

parameter_table = [
    ["Prime Modulus (p)", p],
    ["Generator (g)", g]
]
print("\n PUBLIC PARAMETERS")
print(tabulate(parameter_table, headers=["Parameter", "Value"], tablefmt="grid"))

#  4. Enterprise Analytics server generates secrets
print("\n" + "="*60)
print("ENTERPRISE ANALYTICS SERVER")
print("="*60)
analytic_private = int(input("Input the Sender Private value: "))
analytic_public = pow(g, analytic_private, p)

analytic_table = [
    ["Private Secret", analytic_private],
    ["Public Exchange Value", analytic_public]
]

print("\nENTERPRISE ANALYTICS SERVER KEYS:")
print(tabulate(analytic_table, headers=["Key", "Value"], tablefmt="grid"))


# 5. Disaster Recovery Server generates secrets
print("\n" + "="*60)
print("DISASTER RECOVERY SERVER")
print("="*60)
recovery_private = int(input("Input the Receiver Private Value: "))
recovery_public = pow(g, recovery_private, p)

recovery_table = [

    ["Private Secret", recovery_private],
    ["Public Exchange Value", recovery_public]
]

print("\nDISASTER RECOVERY SERVER KEYS:")
print(tabulate(recovery_table, headers=["Key", "Value"], tablefmt="grid"))


# 6. Exchange public values over network
print("\n" + "="*60)
print("EXCHANGING PUBLIC VALUES OVER NETWORK")
print("="*60)
print("Enterprise Analytics sends public value to Disaster Recovery")
print("Disaster Recovery sends public value to Enterprise Analytics")

exchange_table = [
    ["Enterprise Analyitics Server", analytic_table],
    ["Disaster Recovery Server", recovery_table]
]

# 7. Systems Independelty derive shared secret
# Sender (Enterprise Analytics)
analytics_shared_secret = pow(recovery_public, analytic_private, p)

# Receiver (Disaster Recovery)
recovery_shared_secret = pow(analytic_public, recovery_private, p)

print(f"\n Derived Shared Secret: {recovery_shared_secret}")

# 8. Validating shared secret agreement
print("\n" + "="*60)
print("DERIVED SHARED SECRETS")
print("="*60)

validation_table = [
    ["Analytics Server Secret", analytics_shared_secret],
    ["Recovery Server Secret", recovery_shared_secret]
]

print(tabulate(
    validation_table,
    headers=["System", "Derived Shared Secret"],
    tablefmt="grid"
))

if analytics_shared_secret == recovery_shared_secret:
    print("\nShared secret successfully established")
else:
    print("\nShared secret mismatch detected")

# 9. Build encrypted communication session
shared_secret_bytes = str(analytics_shared_secret).encode()

# Derive session key using SHA-256
session_key = hashlib.sha256(shared_secret_bytes).digest()
session_key = base64.urlsafe_b64encode(session_key)

# Create Fernet cipher
cipher = Fernet(session_key)


# Encrypt the sync request (convert string to bytes)
sync_request_bytes = sync_request.encode('utf-8')
encrypted_payload = cipher.encrypt(sync_request_bytes)


# Save encrypted payload
encrypted_file = docs_dir / "encrypted_sync_payload.txt"
encrypted_file.write_bytes(encrypted_payload)
print(f"\nEncrypted payload saved to: {encrypted_file}")
print(f"   Encrypted payload (first 50 bytes): {encrypted_payload[:50]}...")


# 10. Recovery server decrypts payload
recovered_payload = cipher.decrypt(encrypted_payload)

recovered_file = docs_dir / "recovered_sync_request.txt"
recovered_file.write_bytes(recovered_payload)

print(f"\nDecrypted payload saved to: {recovered_file}")

# Display recovered content
print("\nRECOVERED SYNCHRONIZATION REQUEST:")
print("-"*50)
print(recovered_payload.decode('utf-8'))
print("-"*50)

# 11. External observer interception attempt
print("\n" + "="*60)
print("EXTERNAL OBSERVER (EAVESDROPPER) VIEW")
print("="*60)
print("An attacker can only see these public values:")

observer_table = [
    ["Prime Modulus (p)", p],
    ["Generator (g)", g],
    ["Analytics Public Value (A)", analytic_public],
    ["Recovery Public Value (B)", recovery_public],
    ["Can derive shared secret?", "NO - Discrete Log Problem"]
]

print(tabulate(
    observer_table,
    headers=["Observed Public Information", "Value"],
    tablefmt="grid"
))

print("\nKEY TAKEAWAYS")
print("="*60)
print("• The shared secret was never transmitted over the network")
print("• Both systems independently derived the same secret")
print("• An eavesdropper cannot derive the secret without knowing private keys")
print("• Security depends on the Discrete Logarithm Problem (DLP)")
print("• The shared secret was used to encrypt/decrypt enterprise data")
print("• This is how real-world systems like HTTPS and VPNs work")
print("="*60)

print(f"\nWorkspace contents:")
for item in docs_dir.iterdir():
    print(f"   ├── {item.name}")