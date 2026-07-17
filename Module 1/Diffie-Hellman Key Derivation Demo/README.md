# Diffie-Hellman Key Derivation Demo

**Enterprise Scenario: Secure Cloud-to-Cloud Synchronization**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Cryptography](https://img.shields.io/badge/Cryptography-Fernet-purple.svg)](https://cryptography.io/)

A practical demonstration of the Diffie-Hellman key exchange protocol in an enterprise context. Two cloud-based systems securely establish a shared secret over a public network without directly transmitting the secret itself.

---

## Table of Contents

- [Overview](#overview)
- [Scenario](#scenario)
- [How It Works](#how-it-works)
- [Mathematical Foundation](#mathematical-foundation)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Security Features](#security-features)
- [Post-Quantum Context](#post-quantum-context)
- [References](#references)
- [License](#license)

---

## Overview

This project demonstrates how two enterprise systems can securely exchange encryption keys over an insecure network using the Diffie-Hellman key exchange protocol. The workflow shows:

1. **Public parameter generation** - Prime modulus and generator
2. **Private key generation** - Each system generates a secret
3. **Public key exchange** - Systems exchange public values
4. **Shared secret derivation** - Both systems independently derive the same secret
5. **Secure communication** - The shared secret is used for AES encryption

---

## Scenario

Two cloud-based enterprise systems must securely synchronize confidential data:

- **Enterprise Analytics Server** - Sends synchronization requests
- **Disaster Recovery Server** - Receives and processes requests

Both systems need to establish a shared secret over a public network without transmitting the secret itself. The Diffie-Hellman protocol enables this secure key exchange.

### Security Challenge

An external observer (eavesdropper) can see all public values but cannot derive the shared secret due to the computational difficulty of the Discrete Logarithm Problem (DLP).

---

## How It Works

### Key Exchange Process

1. **Public Parameters:** Both systems agree on a prime modulus (p) and generator (g)
2. **Private Keys:** Each system generates a private secret
3. **Public Keys:** Each system computes a public value: `public = g^private mod p`
4. **Exchange:** Systems exchange public values over the network
5. **Shared Secret:** Each system computes: `secret = other_public^private mod p`
6. **Result:** Both systems now have the same shared secret!

---

## Mathematical Foundation

### The Diffie-Hellman Protocol

The Diffie-Hellman key exchange is based on the mathematical properties of modular exponentiation and the Discrete Logarithm Problem.

### Step 1: Public Parameters

Both parties agree on public parameters:

| Parameter | Description | Mathematical Notation |
|-----------|-------------|----------------------|
| **p** | A large prime number | $p$ |
| **g** | A primitive root modulo p | $g$ |

### Step 2: Private Keys

Each party generates a private key:

| Party | Private Key | Public Key |
|-------|-------------|------------|
| **Alice** (Enterprise) | $a$ (secret) | $A = g^a \mod p$ |
| **Bob** (Disaster Recovery) | $b$ (secret) | $B = g^b \mod p$ |

### Step 3: Public Key Exchange

Alice and Bob exchange their public keys:

$$A \xrightarrow{\text{over network}} B$$

$$B \xrightarrow{\text{over network}} A$$

### Step 4: Shared Secret Derivation

Each party independently derives the same shared secret:

**Alice computes:**

$$s = B^a \mod p$$

Since $B = g^b \mod p$:

$$s = (g^b)^a \mod p$$

$$s = g^{ab} \mod p$$

**Bob computes:**

$$s = A^b \mod p$$

Since $A = g^a \mod p$:

$$s = (g^a)^b \mod p$$

$$s = g^{ab} \mod p$$

### Step 5: Result

Both parties now have the same shared secret:

$$s = g^{ab} \mod p$$

### Example with Small Numbers

Let's trace through a concrete example:

**Public Parameters:**
- Prime modulus: $p = 19$
- Generator: $g = 2$

**Alice's Keys:**
- Private key: $a = 8$
- Public key: $A = 2^8 \mod 19 = 9$

**Bob's Keys:**
- Private key: $b = 15$
- Public key: $B = 2^{15} \mod 19 = 19$

**Key Exchange:**
- Alice sends $A = 9$ to Bob
- Bob sends $B = 12$ to Alice

**Shared Secret Derivation:**

Alice computes:
$$s = B^a \mod p = 12^8 \mod 19 = 11$$

Bob computes:
$$s = A^b \mod p = 9^{15} \mod 19 = 11$$

**Result:** Both parties derive $s = 11$ ✓

---

## The Discrete Logarithm Problem (DLP)

The security of Diffie-Hellman relies on the computational difficulty of the Discrete Logarithm Problem.

### Definition

Given:
- A prime modulus $p$
- A generator $g$
- A value $A = g^a \mod p$

Find the exponent $a$.

### Why It's Hard

For large primes (2048+ bits), finding $a$ given $g$, $p$, and $A$ is computationally infeasible with current computers.

### Mathematical Notation

The discrete logarithm is written as:

$$a = \log_g(A) \mod p$$

### Security Strength

| Key Size | Security Level | Status |
|----------|---------------|--------|
| 512-bit | 40-bit | Broken |
| 1024-bit | 80-bit | Weak |
| **2048-bit** | **112-bit** | **Secure** |
| 3072-bit | 128-bit | Strong |
| 4096-bit | 128-bit+ | Very Strong |

### Mathematical Explanation

The discrete logarithm problem is considered computationally hard because:

1. **Modular Exponentiation is a One-Way Function:**
   - Easy to compute: $A = g^a \mod p$
   - Hard to invert: $a = \log_g(A) \mod p$

2. **No Known Efficient Algorithm:**
   - The best known algorithms (e.g., Index Calculus, Pollard's Rho) run in sub-exponential time
   - For 2048-bit primes, these algorithms are computationally infeasible

3. **Quantum Threat:**
   - **Shor's Algorithm** can solve DLP in polynomial time on a quantum computer
   - This is why post-quantum cryptography is needed

---

