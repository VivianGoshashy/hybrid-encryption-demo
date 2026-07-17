# Hybrid Encryption Demo: Post-Quantum Cryptography Workflow

A practical demonstration of hybrid encryption combining symmetric (AES/Fernet) and asymmetric (RSA) cryptography. This project implements a realistic secure file sharing workflow inspired by the Coursera Post-Quantum Cryptography course.

---

## Overview

This project demonstrates the hybrid encryption approach used in real-world systems like HTTPS, PGP, and secure messaging apps. It combines symmetric encryption for speed, asymmetric encryption for secure key exchange, and integrity verification to ensure files haven't been tampered with.

The main challenge this project addresses is that symmetric encryption like AES is fast but has a key exchange problem — you need a secure way to share the key. Asymmetric encryption like RSA solves key exchange but is too slow for large files. Hybrid encryption solves both problems by using AES for the file and RSA for the key.

The workflow works like this: you encrypt the file with AES, then encrypt the AES key with RSA, send both to the recipient, and the recipient decrypts the AES key with their RSA private key before decrypting the file.

---

## Why Hybrid Encryption

Symmetric encryption is fast and efficient for large data but has a key exchange problem. Asymmetric encryption has no key exchange problem but is very slow for large data. Hybrid encryption combines both approaches to get the benefits of speed and secure key exchange.

This approach is used in real-world applications like HTTPS for web traffic, PGP for email encryption, secure messaging apps like Signal and WhatsApp, cloud storage with zero-knowledge encryption, and VPNs for secure connections.

---

## How It Works

The encryption flow for the sender involves generating an RSA key pair with a public and private key, generating a unique AES key for the file, encrypting the file using AES, encrypting the AES key using the RSA public key, and sending both the encrypted file and encrypted key.

The decryption flow for the recipient involves decrypting the AES key using the RSA private key, decrypting the file using the recovered AES key, and verifying integrity with SHA-256 hashing.

---

## Installation

You need Python 3.8 or higher and pip installed. Install the required libraries with the command pip install cryptography tabulate. You can clone the repository with git clone followed by the repository URL.

---

## Usage

Run the complete demo with python3 encryption_demo.py. This will create the directory structure, generate RSA keys, encrypt a file with AES, encrypt the AES key with RSA, perform decryption, and validate integrity with SHA-256.

You can check the files by viewing the directory structure with ls -la encrypted_docs, viewing the original report, the encrypted report which appears as gibberish, and the decrypted report.

---

## Directory Structure

The project has a main encryption script called encryption_demo.py, a README file, a gitignore file, a requirements file, and a license file. The encrypted_docs folder contains subdirectories for incoming files, processed encrypted files, output decrypted files, and keys. The keys folder stores the RSA private key which must be kept secure, the RSA public key which can be shared, and the encrypted AES key.

---

## Security Features

This implementation uses RSA 2048-bit keys which is the current security standard, OAEP padding which is more secure than PKCS1v15, SHA-256 hashing which is the industry standard for integrity, Fernet which provides AES-128 authenticated encryption, and a hybrid approach that combines speed with secure key exchange.

Security best practices include never exposing the private key, encrypting the AES key with RSA, verifying integrity through hashing, organizing files with clear separation, and never committing keys to Git.

Important security notes are to never share your private key, never commit keys to version control, use strong passwords for key protection, use hardware security modules in production, and rotate keys regularly.

---

## Technical Details

The libraries used include cryptography.fernet.Fernet for symmetric encryption, cryptography.hazmat.primitives.asymmetric.rsa for asymmetric encryption, cryptography.hazmat.primitives.asymmetric.padding for RSA padding, cryptography.hazmat.primitives.hashes for hashing algorithms, tabulate for table formatting, pathlib.Path for file system operations, and hashlib for SHA-256 hashing.

The key parameters are RSA key size of 2048 bits, public exponent of 65537, OAEP padding, SHA-256 hash algorithm, and AES-128 in CBC mode through Fernet.

---

## What I Learned

Key concepts I learned include that hybrid encryption is how real systems like HTTPS, PGP, and Signal work, symmetric encryption is fast while asymmetric encryption solves key exchange, integrity verification is essential for document authenticity, quantum computers threaten current encryption methods, and post-quantum cryptography standards are being finalized by NIST.

Technical skills I gained include working with the cryptography library in Python, understanding RSA key generation and parameters, implementing OAEP padding with SHA-256, creating and validating SHA-256 hashes, organizing code with pathlib, and displaying formatted output with tabulate.

---

## Post-Quantum Context

Current encryption methods like RSA and ECC are vulnerable to quantum computers. Attackers are already collecting encrypted data today with the plan to decrypt it later when quantum computers become powerful enough. This is known as the harvest now, decrypt later threat.

NIST finalized post-quantum cryptography standards in 2024. ML-KEM is a key encapsulation mechanism for key exchange. ML-DSA is a digital signature algorithm. SLH-DSA is a stateless hash-based signature algorithm that serves as a backup.

This matters because hybrid cryptographic models enable a gradual transition to quantum-safe systems. Organizations need to start planning their migration now, and the transition will take years and must be done carefully.

---

## References

The Coursera Post-Quantum Cryptography course provided the foundation for this project. NIST post-quantum cryptography standards provide official documentation. The cryptography.io documentation covers the Python library. The Fernet specification is available through the cryptography documentation. OWASP cryptographic standards provide best practices. NIST SP 800-57 covers key management.

---

## Contributing

Contributions, issues, and feature requests are welcome. To contribute, fork the repository, create a new branch, make your changes, commit them, push to your branch, and open a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

I would like to thank the Coursera Post-Quantum Cryptography course for the foundation, the Python cryptography library developers, the open source community, and NIST for post-quantum cryptography standards.
