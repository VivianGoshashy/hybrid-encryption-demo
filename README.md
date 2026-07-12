cd ~/Desktop/Coursera/PQC

cat > README.md << 'EOF'
# 🔐 Hybrid Encryption Demo: Post-Quantum Cryptography Workflow

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/VivianGoshashy/hybrid-encryption-demo)

A practical demonstration of **hybrid encryption** combining symmetric (AES/Fernet) and asymmetric (RSA) cryptography. This project implements a realistic secure file sharing workflow inspired by the Coursera Post-Quantum Cryptography course.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Why Hybrid Encryption?](#-why-hybrid-encryption)
- [How It Works](#-how-it-works)
- [Visual Workflow](#-visual-workflow)
- [Installation](#-installation)
- [Usage](#-usage)
- [Directory Structure](#-directory-structure)
- [Security Features](#-security-features)
- [Technical Details](#-technical-details)
- [What I Learned](#-what-i-learned)
- [Post-Quantum Context](#-post-quantum-context)
- [References](#-references)
- [License](#-license)

---

## 🚀 Overview

This project demonstrates the **hybrid encryption** approach used in real-world systems like HTTPS, PGP, and secure messaging apps. It combines:

- **Symmetric Encryption (AES/Fernet):** Fast, efficient encryption for large files
- **Asymmetric Encryption (RSA):** Secure key exchange without sharing secrets
- **Integrity Verification (SHA-256):** Ensures files haven't been tampered with

### The Challenge
- **Symmetric encryption (AES)** is fast but has a key exchange problem — how do you securely share the key?
- **Asymmetric encryption (RSA)** solves key exchange but is too slow for large files

### The Solution: Hybrid Encryption
1. Encrypt the file with AES (fast!)
2. Encrypt the AES key with RSA (secure key exchange!)
3. Send both to the recipient
4. Recipient decrypts the AES key with RSA private key
5. Recipient decrypts the file with AES

---

## 🔧 Why Hybrid Encryption?

| Method | Pros | Cons |
|--------|------|------|
| **AES (Symmetric)** | ✅ Fast, efficient for large data | ❌ Key exchange problem |
| **RSA (Asymmetric)** | ✅ No key exchange needed | ❌ Very slow for large data |
| **Hybrid (AES + RSA)** | ✅ Fast + Secure key exchange | ⚠️ Slightly more complex |

### Real-World Applications
- **HTTPS/SSL/TLS** — Secures web traffic
- **PGP/GPG** — Email encryption
- **Secure Messaging** — Signal, WhatsApp
- **Cloud Storage** — Zero-knowledge encryption
- **VPNs** — Secure connections

---

## 📊 How It Works

### Encryption Flow (Sender)
1. Generate RSA key pair (public + private key)
2. Generate a unique AES key for the file
3. Encrypt the file using AES (fast!)
4. Encrypt the AES key using RSA public key
5. Send both encrypted file + encrypted key

### Decryption Flow (Recipient)
1. Decrypt the AES key using RSA private key
2. Decrypt the file using the recovered AES key
3. Verify integrity with SHA-256 hashing

---

## 🎨 Visual Workflow
