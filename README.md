# Anysphere Security Whitepaper

**Link: https://anysphere-messaging.com/anysphere-whitepaper.pdf**

## Overview

This repository contains the LaTeX source code for the Anysphere security whitepaper, titled "Anysphere: Private Communication in Practice". The whitepaper describes our exact threat model and how we achieve security against threats in the model.

## Key Security Guarantees

Anysphere protects all information about a conversation between A and B, against any attacker, as long as the attacker does not have access to A's or B's computers. This includes:

- **Metadata Privacy**: Who is talking to whom, when, and how often
- **Content Privacy**: What is being said in the conversation
- **No Needless Trust**: Even if all servers are compromised, communication remains secure

## Technical Overview

The whitepaper covers several key technical areas:

- **Threat Model**: Comprehensive analysis of potential attackers and attack vectors
- **Core Protocol**: Private Information Retrieval (PIR) based on homomorphic encryption
- **Trust Establishment**: Secure key exchange and authentication mechanisms
- **Practical Security**: Real-world implementation considerations and performance
- **Related Research**: Comparison with existing privacy-preserving communication systems

The system uses advanced cryptographic techniques including:
- Homomorphic encryption for private information retrieval
- Zero-knowledge proofs for authentication
- Metadata obfuscation techniques

## Building the Document

### Prerequisites

- LaTeX distribution (TeX Live recommended)
- Required packages: `texlive-latex-base`, `texlive-latex-extra`, `texlive-fonts-recommended`, `texlive-bibtex-extra`, `texlive-fonts-extra`
- `latexmk` for automated building

### Installation (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-bibtex-extra texlive-fonts-extra latexmk
```

### Building

```bash
# Build the PDF once
make once

# Build with continuous monitoring (auto-rebuild on changes)
make main.pdf

# Clean build artifacts
make clean
```

## Project Structure

- `main.tex` - Main document file
- `preamble.tex` - LaTeX packages and configuration
- `*.tex` - Individual sections of the whitepaper
- `bib.bib` - Bibliography database
- `*.pdf` - Figures and diagrams
- `Makefile` - Build automation

## Development Setup

### Recommended Editor

For the best LaTeX editing experience, we recommend:

- **Overleaf** (online): Upload the project files for collaborative editing
- **TeXstudio** (offline): Full-featured LaTeX IDE with syntax highlighting
- **VS Code** with LaTeX Workshop extension: Modern editor with excellent LaTeX support

### File Organization

- Each section of the whitepaper is in its own `.tex` file
- Figures are stored as PDF files in the root directory
- The `preamble.tex` file contains all LaTeX package imports and custom definitions
- Bibliography entries are managed in `bib.bib`

### Common Tasks

```bash
# View the current PDF (if you have a PDF viewer)
xdg-open main.pdf

# Check for LaTeX errors
make once 2>&1 | grep -i error

# Clean and rebuild from scratch
make clean && make once
```

## Contributing

This whitepaper is part of the Anysphere project. When contributing:

1. **Content Changes**: Edit the relevant `.tex` files
2. **Bibliography**: Add new references to `bib.bib`
3. **Figures**: Place new figures as PDF files in the root directory
4. **Testing**: Always run `make once` to ensure the document builds correctly

For questions or major contributions, please refer to the main Anysphere repository.

## License

See LICENSE file for details.
