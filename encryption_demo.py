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

