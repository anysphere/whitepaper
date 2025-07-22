# Development Guide

This document provides detailed information for contributors working on the Anysphere security whitepaper.

## Getting Started

### Environment Setup

1. **Install LaTeX Distribution**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install texlive-full
   
   # macOS with Homebrew
   brew install --cask mactex
   
   # Or install BasicTeX for a smaller footprint
   brew install --cask basictex
   ```

2. **Verify Installation**
   ```bash
   latex --version
   pdflatex --version
   latexmk --version
   ```

3. **Clone and Build**
   ```bash
   git clone [repository-url]
   cd anysphere-whitepaper
   make once
   ```

### Required LaTeX Packages

The document uses several LaTeX packages. If you encounter missing package errors, install them:

```bash
# Common packages that might need manual installation
tlmgr install cryptocode
tlmgr install clrscode4e
tlmgr install acmart
tlmgr install biblatex
tlmgr install biber
```

## Document Structure

### Main Files

- **main.tex**: Document entry point, includes all sections
- **preamble.tex**: Package imports, custom commands, and document setup
- **latexdefs.tex**: Custom LaTeX definitions and macros
- **bib.bib**: Bibliography entries in BibTeX format

### Content Sections

Each section is in its own `.tex` file for better organization:

1. **abs.tex**: Abstract (6 lines)
2. **introduction.tex**: Introduction and motivation (46 lines)
3. **securitycontext.tex**: Security assumptions and context (29 lines)
4. **coreprotocol.tex**: Technical protocol specification (144 lines)
5. **trustestablishment.tex**: Trust mechanisms (138 lines)
6. **practicalsecurity.tex**: Implementation considerations (52 lines)
7. **relatedresearch.tex**: Related work comparison (9 lines)
8. **futureexperiments.tex**: Future research directions (37 lines)
9. **threatmodel.tex**: Threat model specification (52 lines)

### Custom Styles and Packages

- **cryptocode.sty**: Cryptographic notation and algorithms
- **clrscode4e.sty**: Algorithm formatting (CLRS style)
- **acmart.cls**: ACM article class (if needed)

## Writing Guidelines

### LaTeX Best Practices

1. **Use semantic markup**:
   ```latex
   \emph{emphasis} instead of \textit{italic}
   \strong{strong} instead of \textbf{bold}
   ```

2. **Consistent notation**:
   - Use custom commands from `latexdefs.tex`
   - Follow established cryptographic notation
   - Be consistent with variable names

3. **Citations**:
   ```latex
   \cite{key}           % Basic citation
   \cite[p.~42]{key}    % Citation with page
   \citep{key}          # Parenthetical citation
   \citet{key}          # Textual citation
   ```

4. **Cross-references**:
   ```latex
   \label{sec:introduction}
   \ref{sec:introduction}
   \autoref{sec:introduction}  % Preferred
   ```

### Content Guidelines

1. **Security Terminology**:
   - Be precise with security definitions
   - Use established cryptographic terminology
   - Define new terms clearly

2. **Technical Accuracy**:
   - Verify all protocol descriptions
   - Include proper security proofs
   - Reference authoritative sources

3. **Clarity**:
   - Write for both technical and non-technical audiences
   - Use examples to illustrate complex concepts
   - Provide intuitive explanations before technical details

## Building and Testing

### Development Workflow

1. **Continuous Building**:
   ```bash
   make          # Watches for changes and rebuilds automatically
   ```

2. **Single Build**:
   ```bash
   make once     # Build once and exit
   ```

3. **Clean Build**:
   ```bash
   make clean    # Remove all build artifacts
   make once     # Fresh build
   ```

### Troubleshooting Common Issues

1. **Missing Package Errors**:
   ```bash
   tlmgr install [package-name]
   ```

2. **Bibliography Issues**:
   ```bash
   # Full rebuild sequence
   pdflatex main.tex
   biber main        # or bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```

3. **Font Issues**:
   ```bash
   # Update font cache
   fc-cache -fv
   ```

### Quality Checks

1. **Spell Check**:
   ```bash
   aspell --mode=tex --check *.tex
   ```

2. **Style Check**:
   - Use consistent terminology
   - Follow academic writing conventions
   - Check for proper citations

3. **Technical Review**:
   - Verify all protocols and algorithms
   - Check mathematical notation
   - Ensure security claims are supported

## Contributing

### Submission Process

1. **Create Feature Branch**:
   ```bash
   git checkout -b feature/your-improvement
   ```

2. **Make Changes**:
   - Edit relevant `.tex` files
   - Update bibliography if needed
   - Test build locally

3. **Commit Changes**:
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```

4. **Submit Pull Request**:
   - Include description of changes
   - Reference any related issues
   - Ensure builds successfully

### Review Process

All changes go through peer review focusing on:
- Technical accuracy
- Security correctness
- Writing clarity
- LaTeX formatting
- Bibliography completeness

## File Organization

### Keeping Files Organized

- One section per file
- Logical file naming
- Consistent indentation
- Clear section headers
- Proper commenting for complex LaTeX

### Version Control

- Commit frequently with descriptive messages
- Keep commits focused on single changes
- Tag releases appropriately
- Maintain clean commit history

## Resources

### LaTeX Resources

- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [CTAN Package Archive](https://ctan.org/)

### Cryptography Resources

- [Handbook of Applied Cryptography](http://cacr.uwaterloo.ca/hac/)
- [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/)
- [Cryptographic Protocol Notation](https://en.wikipedia.org/wiki/Security_protocol_notation)

### Academic Writing

- [Academic Writing Guidelines](https://writing.wisc.edu/handbook/)
- [Mathematical Writing](http://jmlr.csail.mit.edu/reviewing-papers/knuth_mathematical_writing.pdf)

## Contact

For development questions:
- Create an issue in the repository
- Contact the development team: {arvid, stzh1555, sualeh}@anysphere.co