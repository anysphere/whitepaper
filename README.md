# Anysphere: Private Communication in Practice

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains the security whitepaper for **Anysphere**, a metadata-private communication system deployed in the real world. The paper describes a novel approach to private messaging that protects all conversation metadata using private information retrieval (PIR) based on homomorphic encryption.

**Key Features:**
- 🔒 **Complete Metadata Privacy**: Protects who talks to whom, when, and how often
- 🛡️ **Strong Threat Model**: Secure even if all servers are compromised
- 🌐 **Real-world Deployment**: Not just theoretical - actually implemented and deployed
- 🔐 **Homomorphic Encryption**: Uses advanced cryptographic techniques for privacy

## Abstract

We describe Anysphere, a metadata-private communication system deployed in the real world. Using private information retrieval based on homomorphic encryption, our system guarantees metadata privacy even if all of our servers are compromised and any number of the users and network observers are malicious. In this whitepaper, we precisely define our threat model, and show how we achieve security against it both in theory and in practice.

## Paper Details

- **Title**: Anysphere: Private Communication in Practice
- **Subtitle**: Security Whitepaper  
- **Authors**: Arvid Lunnemark, Shengtong Zhang, Sualeh Asif
- **Contact**: {arvid, stzh1555, sualeh}@anysphere.co
- **Date**: July 6, 2022 (with updates)
- **Published Version**: [anysphere-messaging.com/anysphere-whitepaper.pdf](https://anysphere-messaging.com/anysphere-whitepaper.pdf)

## Repository Structure

```
├── main.tex              # Main LaTeX document
├── abs.tex               # Abstract
├── introduction.tex      # Introduction section
├── securitycontext.tex   # Security context and assumptions
├── coreprotocol.tex      # Core protocol description
├── trustestablishment.tex # Trust establishment mechanisms
├── practicalsecurity.tex # Practical security considerations
├── relatedresearch.tex   # Related work
├── futureexperiments.tex # Future experiments and work
├── bib.bib              # Bibliography
├── latexdefs.tex        # LaTeX definitions and macros
├── preamble.tex         # Document preamble
├── *.pdf                # Generated PDFs and figures
├── *.sty *.cls          # LaTeX style files
├── Makefile             # Build configuration
└── README.md            # This file
```

## Building the Paper

### Prerequisites

You need a LaTeX distribution installed on your system:
- **Linux**: Install `texlive-full`
- **macOS**: Install MacTeX
- **Windows**: Install MiKTeX or TeX Live

### Build Commands

```bash
# Build the PDF (with continuous compilation)
make main.pdf

# Build once without watching for changes
make once

# Clean build artifacts
make clean
```

The compiled PDF will be generated as `main.pdf`.

### Build Details

The build process uses `latexmk` with the following features:
- PDF output format
- Halt on errors for debugging
- File-line error reporting
- Non-interactive mode
- SyncTeX support for editor integration

## Security Guarantee

> **Anysphere protects all information about a conversation between A and B, against any attacker, as long as the attacker does not have access to A's or B's computers.**

This represents a significant advance in practical privacy, going beyond content encryption to protect:
- Communication patterns
- Timing information  
- Frequency of messages
- Participant identities
- Social graphs

## Key Technical Contributions

1. **Practical PIR Implementation**: Real-world deployment of private information retrieval
2. **Homomorphic Encryption**: Advanced cryptographic techniques for metadata privacy
3. **Comprehensive Threat Model**: Precise security definitions and guarantees
4. **Production System**: Not just academic theory - actually deployed and used

## Development Tools

This repository includes configuration for:
- **Linting**: `.markdownlint.yaml` for Markdown formatting
- **Git**: Comprehensive `.gitignore` for LaTeX projects
- **VS Code**: Editor configuration in `.vscode/`
- **Trunk**: Code quality tools in `.trunk/`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this work in your research, please cite:

```bibtex
@misc{anysphere2022,
  title={Anysphere: Private Communication in Practice},
  author={Lunnemark, Arvid and Zhang, Shengtong and Asif, Sualeh},
  year={2022},
  howpublished={Security Whitepaper},
  url={https://anysphere-messaging.com/anysphere-whitepaper.pdf}
}
```

## Contact

For questions about this research or the Anysphere system:
- **Email**: {arvid, stzh1555, sualeh}@anysphere.co
- **Website**: [anysphere-messaging.com](https://anysphere-messaging.com)

---

*This whitepaper represents cutting-edge research in practical privacy-preserving communication systems. The techniques described here are implemented in the real-world Anysphere messaging platform.*