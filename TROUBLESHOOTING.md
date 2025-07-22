# Troubleshooting Guide

This guide helps resolve common issues when building and working with the Anysphere whitepaper.

## Build Issues

### LaTeX Distribution Problems

#### "pdflatex: command not found"

**Problem:** LaTeX is not installed or not in PATH.

**Solutions:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install texlive-full

# macOS with Homebrew
brew install --cask mactex

# Verify installation
which pdflatex
latex --version
```

#### "Package not found" Errors

**Problem:** Required LaTeX packages are missing.

**Common missing packages:**
```bash
# Install individual packages
tlmgr install cryptocode
tlmgr install clrscode4e  
tlmgr install biblatex
tlmgr install biber
tlmgr install acmart
tlmgr install tikz
tlmgr install xcolor
tlmgr install amsmath
tlmgr install geometry

# Or install collections
tlmgr install collection-latexextra
tlmgr install collection-mathscience
```

### Bibliography Issues

#### "biber: command not found"

**Problem:** Biber (bibliography processor) is not installed.

**Solutions:**
```bash
# Ubuntu/Debian
sudo apt-get install biber

# macOS with Homebrew
brew install biber

# Or install via tlmgr
tlmgr install biber
```

#### Bibliography not appearing or citations showing as "?"

**Problem:** Bibliography compilation sequence is incorrect.

**Solution - Correct build sequence:**
```bash
pdflatex main.tex    # First pass
biber main           # Process bibliography (note: no .tex extension)
pdflatex main.tex    # Second pass - resolve citations
pdflatex main.tex    # Third pass - finalize formatting
```

### Common Log File Patterns

- `! LaTeX Error:` - LaTeX syntax errors
- `Package Warning:` - Package-related issues
- `Overfull \hbox` - Text overflow warnings
- `Undefined control sequence` - Unknown commands

## Getting Help

### Resources

- **LaTeX Documentation:** https://www.latex-project.org/help/documentation/
- **TeX Stack Exchange:** https://tex.stackexchange.com/
- **Package Documentation:** `texdoc packagename`

This troubleshooting guide covers the most common issues. For project-specific problems, also check [DEVELOPMENT.md](DEVELOPMENT.md) and [LATEX_GUIDE.md](LATEX_GUIDE.md).