# Anysphere: Private Communication in Practice

**Security Whitepaper**

**Published Version: https://anysphere-messaging.com/anysphere-whitepaper.pdf**

## Overview

This whitepaper describes Anysphere, a metadata-private communication system deployed in the real world. Using private information retrieval based on homomorphic encryption, our system guarantees metadata privacy even if all of our servers are compromised and any number of the users and network observers are malicious.

In short, Anysphere protects all information about a conversation between A and B, against any attacker, as long as the attacker does not have access to A's or B's computers.

## Authors

- Arvid Lunnemark (arvid@anysphere.co)
- Shengtong Zhang (stzh1555@anysphere.co)  
- Sualeh Asif (sualeh@anysphere.co)

## Document Structure

The whitepaper is organized into the following sections:

- **Abstract** (`abs.tex`) - Overview of the Anysphere system
- **Introduction** (`introduction.tex`) - Background and motivation
- **Security Context** (`securitycontext.tex`) - Security assumptions and context
- **Core Protocol** (`coreprotocol.tex`) - Technical details of the protocol
- **Trust Establishment** (`trustestablishment.tex`) - How trust is established in the system
- **Practical Security** (`practicalsecurity.tex`) - Real-world security considerations
- **Related Research** (`relatedresearch.tex`) - Comparison with existing work
- **Future Experiments** (`futureexperiments.tex`) - Planned improvements and experiments
- **Threat Model** (`threatmodel.tex`) - Detailed threat analysis

## Building the Document

### Prerequisites

- LaTeX distribution (e.g., TeX Live, MiKTeX)
- `latexmk` for automated building
- Required packages (automatically handled by most LaTeX distributions)

### Build Commands

To build the PDF with continuous compilation (watches for file changes):
```bash
make
```

To build the PDF once:
```bash
make once
```

To clean build artifacts:
```bash
make clean
```

The compiled PDF will be generated as `main.pdf`.

## Files

- `main.tex` - Main LaTeX document
- `*.tex` - Individual section files
- `bib.bib` - Bibliography
- `*.cls`, `*.sty` - LaTeX style files and packages
- `*.pdf` - Figures and diagrams
- `Makefile` - Build automation

## License

See `LICENSE` file for licensing information.
