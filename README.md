# Anysphere: Private Communication in Practice
**Security Whitepaper**

[![PDF](https://img.shields.io/badge/PDF-Download-red.svg)](https://anysphere-messaging.com/anysphere-whitepaper.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

This repository contains the source code for the Anysphere security whitepaper, which describes a metadata-private communication system deployed in the real world. The whitepaper presents our exact threat model and demonstrates how we achieve security against threats within that model.

**Key Security Guarantee**: Anysphere protects all information about conversations between users A and B against any attacker, as long as the attacker does not have access to A's or B's computers.

## Abstract

We describe Anysphere, a metadata-private communication system deployed in the real world. Using private information retrieval based on homomorphic encryption, our system guarantees metadata privacy even if all of our servers are compromised and any number of the users and network observers are malicious. In this whitepaper, we precisely define our threat model, and show how we achieve security against it both in theory and in practice.

## Contents

The whitepaper covers the following topics:

- **Introduction**: Motivation and principles behind Anysphere
- **Security Context**: Detailed threat model and security assumptions
- **Core Protocol**: Technical description of the private communication protocol
- **Trust Establishment**: How users establish secure connections
- **Practical Security**: Real-world implementation considerations
- **Related Research**: Comparison with existing approaches
- **Future Experiments**: Planned improvements and research directions

## Building the PDF

### Requirements

- LaTeX distribution (e.g., TeX Live, MiKTeX)
- `latexmk` (usually included with LaTeX distributions)

### Build Commands

To build the PDF with continuous compilation (watches for changes):
```bash
make
```

To build once:
```bash
make once
```

To clean build artifacts:
```bash
make clean
```

The generated PDF will be `main.pdf`.

## Repository Structure

- `main.tex` - Main LaTeX document
- `*.tex` - Individual sections of the whitepaper
- `*.pdf` - Figures and diagrams
- `bib.bib` - Bibliography
- `*.sty`, `*.cls` - LaTeX style files and document class
- `Makefile` - Build configuration

## Authors

- **Arvid Lunnemark** - arvid@anysphere.co
- **Shengtong Zhang** - stzh1555@anysphere.co  
- **Sualeh Asif** - sualeh@anysphere.co

*Originally published: July 6, 2022*

## License

This work is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Links

- **Published Whitepaper**: https://anysphere-messaging.com/anysphere-whitepaper.pdf
- **Anysphere Website**: https://anysphere.co

---

*For questions about the whitepaper content or technical implementation, please contact the authors directly.*
