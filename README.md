# Anysphere Whitepaper

**Link: https://anysphere-messaging.com/anysphere-whitepaper.pdf**

## Overview

This is the security whitepaper for **Anysphere**, a metadata-private communication system deployed in the real world. Using private information retrieval (PIR) based on homomorphic encryption, Anysphere guarantees metadata privacy even if all servers are compromised and any number of users and network observers are malicious.

## What is Anysphere?

Anysphere is a messaging system that protects **both the content and metadata** of conversations. While end-to-end encryption protects *what* is being said, Anysphere also protects *who* is talking to whom, *when* they're talking, and *how often* — information that is currently leaked at scale even by the most secure communication platforms.

**Core Principle: No Needless Trust**

Anysphere operates on the principle of *no needless trust*. Even if all servers are compromised, everyone's communication history and patterns remain secure. The system only trusts:
- The user's local device
- The user's contacts' devices

## Threat Model

This whitepaper precisely defines Anysphere's threat model, which assumes:

1. **All servers may be compromised** — Full control over all servers
2. **The entire internet may be controlled** — Global adversary can observe and manipulate all network traffic
3. **Strangers may be malicious** — Attacker controls all clients that are not contacts
4. **Contacts are trusted** — Attacker cannot compromise a user's contacts
5. **User's computer is trusted** — Assumes correct implementation running locally
6. **Standard cryptography holds** — Security of cryptographic primitives (Libsodium AEAD, Microsoft SEAL homomorphic encryption)

## What's in This Whitepaper?

The whitepaper covers:

- **Introduction** — Motivation and problem statement
- **Security Context** — Threat model and security definitions
- **Core Protocol** — How private information retrieval works
- **Trust Establishment** — How users connect securely
- **Practical Security** — Real-world security considerations
- **Related Research** — Comparison with other systems
- **Future Experiments** — Planned improvements

## Key Security Guarantee

**Anysphere protects all information about a conversation between A and B, against any attacker, as long as the attacker does not have access to A's or B's computers.**

## Code

The Anysphere client code is open source and available at: https://github.com/anysphere/client
