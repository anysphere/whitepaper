# Anysphere: Private Communication in Practice

**Security Whitepaper** | *Last updated: July 6, 2022*

## Overview

Anysphere is a metadata-private communication system that guarantees complete privacy even when all servers are compromised and any number of users and network observers are malicious. Using private information retrieval (PIR) based on homomorphic encryption, Anysphere protects all information about conversations between users against any attacker, as long as the attacker does not have access to the users' computers.

## Key Features

### 🔒 **Metadata Privacy**
- Protects who is talking to whom, when, and how often
- Even if all servers are compromised, communication patterns remain secure
- Stronger than traditional end-to-end encryption which only protects message content

### 🛡️ **No Needless Trust**
- Operates on the principle of minimal trust
- Only trusts the local device and your contacts
- No trust required in servers, ISPs, or network infrastructure

### ⚡ **Practical Implementation**
- Real-world deployment with reasonable performance
- Uses FastPIR, one of the fastest cPIR schemes
- Open source client code available

## How It Works

### Core Protocol
1. **Registration**: Each user gets a dedicated outbox on the server
2. **Sending**: Users send exactly 1KB of data every minute (real messages or random data)
3. **Receiving**: Users retrieve messages using Private Information Retrieval (PIR)
4. **Privacy**: Server cannot determine who is communicating with whom

### Technical Details
- **Private Information Retrieval (PIR)**: Uses homomorphic encryption to retrieve data without revealing what's being accessed
- **Constant Rate Transmission**: Sends data at regular intervals to hide communication patterns
- **Chunked Messages**: Large messages are split into 1KB chunks with ACK-based delivery
- **Authentication**: Each user has a unique authentication token for their outbox

## Security Model

### Threat Model
Anysphere protects against:
- ✅ **Compromised servers** - All servers can be controlled by attackers
- ✅ **Network surveillance** - ISPs and governments monitoring traffic
- ✅ **Malicious strangers** - Any number of compromised users
- ✅ **Timing attacks** - Regular transmission schedule prevents correlation

### What We Trust
- **Your computer** - Must run correct implementation
- **Your contacts** - Must not be compromised
- **Cryptography** - Standard primitives (XSalsa20, BFV)

### What We Don't Trust
- ❌ Servers
- ❌ Network infrastructure
- ❌ ISPs or government agencies
- ❌ Other users (except contacts)

## Project Structure

This repository contains the LaTeX source for the Anysphere security whitepaper:

- `main.tex` - Main document with all sections
- `introduction.tex` - Problem motivation and approach
- `securitycontext.tex` - Security goals and threat model
- `coreprotocol.tex` - Detailed protocol description
- `trustestablishment.tex` - How users establish secure connections
- `practicalsecurity.tex` - Real-world security considerations
- `relatedresearch.tex` - Comparison with other approaches
- `futureexperiments.tex` - Planned improvements
- `threatmodel.tex` - Detailed threat model
- `abs.tex` - Abstract
- `bib.bib` - Bibliography
- `Makefile` - Build instructions

## Building the Whitepaper

```bash
# Build PDF with continuous preview
make main.pdf

# Build PDF once
make once

# Clean build artifacts
make clean
```

## Key Statistics

Based on the whitepaper content analysis:
- **37 mentions** of "metadata" across 10 files
- **23 mentions** of "privacy" across 9 files  
- **23 mentions** of "PIR" or "private information retrieval" across 9 files
- **13 mentions** of "threat model" across 7 files
- **5 mentions** of "homomorphic" across 4 files

## Research Context

Anysphere builds on decades of research in metadata-private communication:
- **Mix-nets** (Chaum, 1981) - First approach but requires trusted servers
- **Tor** (2002) - Popular but vulnerable to timing attacks
- **PIR-based systems** - Pung, Addra - Perfect security with reasonable scalability
- **Other approaches** - DC-nets, MPC techniques, but less secure or practical

## License

MIT License - Copyright (c) 2022 Anysphere

## Links

- **Whitepaper PDF**: https://anysphere-messaging.com/anysphere-whitepaper.pdf
- **Client Code**: https://github.com/anysphere/client
- **Core Library**: https://github.com/anysphere/asphr

## Authors

Arvid Lunnemark, Shengtong Zhang, Sualeh Asif  
{arvid, stzh1555, sualeh}@anysphere.co

---

*This whitepaper describes Anysphere's exact threat model and how we achieve security against threats in the model. In short, Anysphere protects all information about a conversation between A and B, against any attacker, as long as the attacker does not have access to A's or B's computers.*