# Anysphere Security Whitepaper

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#building-the-document)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Latest PDF](https://img.shields.io/badge/PDF-latest-red.svg)](https://anysphere-messaging.com/anysphere-whitepaper.pdf)

**📄 Latest PDF: https://anysphere-messaging.com/anysphere-whitepaper.pdf**

This repository contains the LaTeX source code for the Anysphere security whitepaper, a comprehensive technical document describing our threat model, cryptographic protocols, and security guarantees for private communication.

## 🔒 Overview

Anysphere enables truly private communication by protecting **all information** about conversations between parties A and B against any attacker who does not have direct access to A's or B's devices. Our system provides **metadata privacy** - hiding not just message content, but also communication patterns, timing, frequency, and participant identities.

### Key Innovations

- **🛡️ No Needless Trust**: Minimal trust assumptions - only local devices and communication partners
- **👤 Metadata Privacy**: Complete protection of communication patterns and participant identities  
- **🔍 Private Information Retrieval**: Novel PIR-based protocol for anonymous message delivery
- **⚡ Practical Security**: Real-world deployment considerations and performance analysis
- **🔐 Formal Security**: Rigorous cryptographic proofs and security analysis

### Security Guarantees

Our protocol provides security against adversaries with the following capabilities:
- **Global network monitoring** (ISPs, nation-states, etc.)
- **Server compromise** (messaging platforms, infrastructure providers)
- **Traffic analysis** (timing, volume, pattern analysis)
- **Large-scale surveillance** (mass data collection and correlation)

We do **NOT** protect against adversaries who compromise user devices or coerce users directly.

## Repository Structure

```
├── main.tex              # Main document file
├── abs.tex               # Abstract
├── introduction.tex      # Introduction and motivation
├── securitycontext.tex   # Security context and assumptions
├── coreprotocol.tex      # Core protocol description
├── trustestablishment.tex # Trust establishment mechanisms
├── practicalsecurity.tex # Practical security considerations
├── relatedresearch.tex   # Related work
├── futureexperiments.tex # Future experiments and research
├── threatmodel.tex       # Threat model specification
├── bib.bib              # Bibliography
├── latexdefs.tex        # LaTeX definitions and macros
├── preamble.tex         # Document preamble
└── *.pdf                # Generated PDFs and figures
```

## 🚀 Quick Start

### Prerequisites

- **LaTeX Distribution**: TeX Live (Linux), MiKTeX (Windows), or MacTeX (macOS)
- **Build Tools**: `latexmk`, `biber`, and `make`
- **Required Packages**: See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for installation help

### One-Command Setup

```bash
# Clone the repository
git clone [repository-url]
cd anysphere-whitepaper

# Build the PDF (this will install missing packages automatically on most systems)
make once
```

### Build Commands

| Command | Purpose |
|---------|---------|
| `make` | Continuous compilation (rebuilds on file changes) |
| `make once` | Single build (recommended for first-time users) |
| `make clean` | Remove build artifacts |

### Manual Build Process

For fine-grained control or troubleshooting:
```bash
pdflatex main.tex     # Initial compilation
biber main            # Process bibliography  
pdflatex main.tex     # Resolve citations
pdflatex main.tex     # Final formatting
```

**💡 Tip**: If you encounter build errors, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for solutions to common issues.

## 📖 Document Sections

| Section | Content | Key Topics |
|---------|---------|------------|
| **Abstract** | High-level overview | System goals, key contributions |
| **Introduction** | Motivation and principles | Problem statement, approach overview |
| **Security Context** | Threat model and assumptions | Adversary capabilities, trust model |
| **Core Protocol** | Technical protocol specification | PIR construction, security analysis |
| **Trust Establishment** | Key exchange and authentication | Identity verification, key agreement |
| **Practical Security** | Real-world considerations | Performance, deployment, implementation |
| **Related Research** | Comparison with existing work | Prior art, improvements, positioning |
| **Future Experiments** | Research directions | Open problems, planned extensions |

## 📚 Documentation

### For Users
- **[README.md](README.md)** - This file, project overview and quick start
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Solutions to common build issues
- **[EXAMPLES.md](EXAMPLES.md)** - Practical examples and use cases

### For Contributors  
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines and workflow
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - Development environment setup
- **[LATEX_GUIDE.md](LATEX_GUIDE.md)** - LaTeX-specific guidance

### For Maintainers
- **[API_REFERENCE.md](API_REFERENCE.md)** - Complete LaTeX command reference
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Technical architecture and design decisions
- **[SECURITY_CONCEPTS.md](SECURITY_CONCEPTS.md)** - Security concepts and terminology
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Publication and distribution guidelines

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Quick Contribution Guide

1. **🍴 Fork** the repository
2. **🔧 Setup** your development environment: `make once` 
3. **🌿 Create** a feature branch: `git checkout -b feature/your-contribution`
4. **✏️ Make** your changes (see [EXAMPLES.md](EXAMPLES.md) for patterns)
5. **🧪 Test** your changes: `make clean && make once`
6. **📝 Commit** with clear messages: `git commit -m "content(section): describe changes"`
7. **🚀 Submit** a pull request

### Contribution Types

- **📄 Content**: Protocol improvements, security analysis, proofs
- **📖 Documentation**: Clarifications, examples, guides  
- **🔧 Technical**: LaTeX improvements, build system enhancements
- **🐛 Fixes**: Error corrections, citation updates, formatting

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines, code review process, and style requirements.

## 🏗️ Development Status

- ✅ **Core Protocol**: Complete with formal security analysis
- ✅ **Trust Establishment**: Key exchange protocols specified
- ✅ **Security Analysis**: Comprehensive threat model and proofs
- 🔄 **Performance Analysis**: Ongoing benchmarking and optimization
- 🔄 **Implementation**: Reference implementation in development
- 📋 **Future Work**: Extensions and research directions identified

## 📄 License

This work is licensed under [MIT License](LICENSE). By contributing, you agree that your contributions will be licensed under the same license.

## 📞 Contact & Support

### Academic Inquiries
- **Authors**: Arvid Lunnemark, Shengtong Zhang, Sualeh Asif
- **Email**: {arvid, stzh1555, sualeh}@anysphere.co
- **Affiliation**: Anysphere Inc.

### Technical Support
- **Issues**: [GitHub Issues](../../issues) for bug reports and feature requests
- **Discussions**: [GitHub Discussions](../../discussions) for questions and ideas
- **Security**: For security-related concerns, please email privately

### Project Links
- **🌐 Website**: https://anysphere-messaging.com/
- **📄 Latest PDF**: https://anysphere-messaging.com/anysphere-whitepaper.pdf
- **💻 Implementation**: [Coming Soon]
- **📊 Benchmarks**: [Coming Soon]

---

<div align="center">

**🔒 Secure • 🚀 Practical • 🔬 Rigorous**

*Building the future of private communication*

</div>
