# Architecture Documentation

This document explains the technical architecture, design decisions, and organizational structure of the Anysphere whitepaper repository.

## Document Architecture

### High-Level Structure

The Anysphere whitepaper follows a modular LaTeX architecture designed for maintainability, collaboration, and academic rigor:

```
main.tex                    # Master document - orchestrates all components
├── preamble.tex           # Package imports and document configuration
├── latexdefs.tex          # Custom commands and mathematical notation
├── abs.tex                # Abstract
├── introduction.tex       # Introduction and motivation
├── securitycontext.tex    # Security assumptions and threat model
├── coreprotocol.tex       # Core PIR protocol specification
├── trustestablishment.tex # Trust establishment mechanisms
├── practicalsecurity.tex  # Implementation considerations
├── relatedresearch.tex    # Related work and comparisons
├── futureexperiments.tex  # Future research directions
└── bib.bib               # Bibliography database
```

### Design Principles

#### 1. Separation of Concerns

**Content vs. Presentation:**
- Content files (`.tex`) focus purely on technical content
- Formatting and styling centralized in `preamble.tex` and `latexdefs.tex`
- Custom commands abstract complex notation from content

**Modular Organization:**
- Each major section in its own file for parallel development
- Clear dependencies between sections
- Minimal coupling between content modules

#### 2. Consistency and Maintainability

**Standardized Notation:**
- All mathematical notation defined in `latexdefs.tex`
- Consistent command naming conventions
- Reusable abstractions for common patterns

**Version Control Friendly:**
- Small, focused files reduce merge conflicts
- Clear file boundaries enable parallel editing
- Meaningful commit granularity

#### 3. Academic Standards

**Citation Management:**
- Centralized bibliography in `bib.bib`
- Consistent citation styles via `biblatex`
- Automated cross-reference resolution

**Professional Formatting:**
- Academic paper layout and typography
- Proper mathematical typesetting
- Figure and table management

## Technical Components

### Core LaTeX Infrastructure

#### Document Class and Packages

```latex
\documentclass{article}                    % Standard academic article format
\usepackage[margin=1.7in]{geometry}       % Page layout
\usepackage{amsmath,amsthm}               % Mathematical typesetting
\usepackage{cryptocode}                   % Cryptographic protocol notation
\usepackage{biblatex}                     % Modern bibliography management
```

**Key Package Choices:**

- **`cryptocode`**: Specialized package for cryptographic protocols and security games
- **`biblatex`**: Modern replacement for BibTeX with better Unicode and customization
- **`cleveref`**: Intelligent cross-referencing with automatic type detection
- **`tikz`**: Vector graphics for protocol diagrams and figures

#### Custom Command System

The `latexdefs.tex` file implements a hierarchical command structure:

**Mathematical Foundations:**
```latex
\newcommand{\F}{\mathbb{F}}              % Finite fields
\newcommand{\G}{\mathbb{G}}              % Groups (typically elliptic curves)
\DeclareMathOperator*{\E}{\textrm{E}}    % Expected value operator
```

**Cryptographic Primitives:**
```latex
\newcommand{\Enc}{\mathsf{Enc}}          % Encryption function
\newcommand{\Dec}{\mathsf{Dec}}          % Decryption function
\newcommand{\Hash}{\mathsf{Hash}}        % Hash function
```

**Protocol Notation:**
```latex
\newcommand{\alice}{\mathsf{Alice}}      % Protocol participant
\newcommand{\bob}{\mathsf{Bob}}          % Protocol participant
\newcommand{\server}{\mathsf{Server}}    % Server entity
```

### Build System Architecture

#### Makefile Structure

```makefile
# Default target - continuous compilation
make:
    latexmk -pdf -pvc main.tex

# Single build
once:
    latexmk -pdf main.tex

# Clean build artifacts
clean:
    latexmk -c
```

**Build Process:**
1. **Initial Compilation**: `pdflatex main.tex` → generates `.aux` and `.bcf` files
2. **Bibliography Processing**: `biber main` → processes citations and generates `.bbl`
3. **Reference Resolution**: `pdflatex main.tex` → resolves cross-references and citations
4. **Final Pass**: `pdflatex main.tex` → finalizes formatting and page breaks

#### Dependency Management

```
main.pdf depends on:
├── main.tex (master file)
├── preamble.tex (configuration)
├── latexdefs.tex (commands)
├── *.tex (content files)
├── bib.bib (bibliography)
├── *.pdf (figures)
└── LaTeX packages (external dependencies)
```

## Content Architecture

### Section Organization

#### 1. Abstract (`abs.tex`)
- **Purpose**: Executive summary of contributions
- **Dependencies**: None (self-contained)
- **Length**: ~150-200 words

#### 2. Introduction (`introduction.tex`)
- **Purpose**: Motivation, problem statement, and overview
- **Dependencies**: References to later sections
- **Key Elements**: Threat model overview, contribution summary

#### 3. Security Context (`securitycontext.tex`)
- **Purpose**: Formal threat model and security assumptions
- **Dependencies**: Mathematical notation from `latexdefs.tex`
- **Key Elements**: Adversary capabilities, trust assumptions

#### 4. Core Protocol (`coreprotocol.tex`)
- **Purpose**: Technical specification of PIR protocol
- **Dependencies**: Heavy use of cryptographic notation
- **Key Elements**: Protocol description, security analysis, efficiency analysis

#### 5. Trust Establishment (`trustestablishment.tex`)
- **Purpose**: Key exchange and authentication mechanisms
- **Dependencies**: References to core protocol
- **Key Elements**: Key agreement protocols, identity verification

#### 6. Practical Security (`practicalsecurity.tex`)
- **Purpose**: Implementation considerations and real-world deployment
- **Dependencies**: References to theoretical protocols
- **Key Elements**: Performance analysis, deployment scenarios

#### 7. Related Research (`relatedresearch.tex`)
- **Purpose**: Comparison with existing work
- **Dependencies**: Extensive bibliography references
- **Key Elements**: Comparative analysis, positioning

#### 8. Future Work (`futureexperiments.tex`)
- **Purpose**: Research directions and open problems
- **Dependencies**: References to current work
- **Key Elements**: Experimental plans, theoretical questions

### Mathematical Notation System

#### Hierarchical Organization

**Level 1 - Basic Structures:**
- Number systems: `\N`, `\Z`, `\Q`, `\R`, `\C`
- Algebraic structures: `\F`, `\G`, `\T`

**Level 2 - Cryptographic Primitives:**
- Symmetric operations: `\Enc`, `\Dec`, `\Hash`
- Asymmetric operations: `\DH`, `\gen`

**Level 3 - Protocol Elements:**
- Participants: `\alice`, `\bob`, `\server`, `\adversary`
- Operations: `\send`, `\receive`, `\broadcast`

**Level 4 - Security Definitions:**
- Security notions: `\indcpa`, `\indcca`, `\semantic`
- Complexity classes: `\poly`, `\negl`, `\negligible`

#### Consistency Rules

1. **Naming Conventions:**
   - Mathematical objects: CamelCase (`\Enc`, `\Hash`)
   - Protocol participants: lowercase (`\alice`, `\bob`)
   - Operators: descriptive names (`\concat`, `\xor`)

2. **Semantic Markup:**
   - Use `\mathsf{}` for functions and algorithms
   - Use `\mathbb{}` for number systems and algebraic structures
   - Use `\mathcal{}` for sets and collections

3. **Parameter Handling:**
   - Commands with parameters use descriptive argument names
   - Optional parameters documented in comments
   - Consistent parameter ordering across related commands

## Figure and Diagram Architecture

### PDF Figure Management

**Storage Strategy:**
- All figures stored as PDF files in root directory
- Vector graphics preferred for scalability
- Consistent naming: `descriptive-name.pdf`

**Integration Method:**
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{protocol-diagram.pdf}
\caption{Protocol message flow}
\label{fig:protocol}
\end{figure}
```

### TikZ Integration

**For Simple Diagrams:**
- Protocol flow charts
- System architecture diagrams
- Mathematical illustrations

**Advantages:**
- Version control friendly (text-based)
- Consistent with document typography
- Programmatic generation possible

## Bibliography Architecture

### Citation Management

**File Structure:**
```bibtex
@article{key2023,
    author = {Author Name},
    title = {Paper Title},
    journal = {Journal Name},
    year = {2023},
    volume = {1},
    pages = {1--10}
}
```

**Citation Types:**
- `@article`: Journal papers
- `@inproceedings`: Conference papers
- `@book`: Books and monographs
- `@techreport`: Technical reports
- `@misc`: Web resources and preprints

**Style Configuration:**
```latex
\usepackage[style=alphabetic,backend=bibtex]{biblatex}
\addbibresource{bib.bib}
```

### Cross-Reference System

**Automatic Labeling:**
```latex
\section{Protocol}\label{sec:protocol}
\begin{figure}...\label{fig:diagram}
\begin{theorem}...\label{thm:security}
```

**Smart References:**
```latex
\cref{sec:protocol}    % → "Section 3"
\cref{fig:diagram}     % → "Figure 2" 
\cref{thm:security}    % → "Theorem 1"
```

## Quality Assurance Architecture

### Automated Checks

**Build Verification:**
- Continuous integration ensures document compiles
- Dependency tracking prevents broken builds
- Automated testing of all build targets

**Content Validation:**
- Citation resolution verification
- Cross-reference integrity checks
- Mathematical notation consistency

**Style Enforcement:**
- LaTeX linting for common errors
- Bibliography format validation
- Consistent formatting verification

### Manual Review Process

**Content Review:**
1. Technical accuracy verification
2. Mathematical rigor assessment
3. Clarity and readability evaluation
4. Citation completeness check

**Technical Review:**
1. LaTeX code quality assessment
2. Build system reliability check
3. Documentation completeness verification
4. Version control best practices

## Extensibility Design

### Adding New Sections

1. **Create Content File:**
   ```bash
   touch newsection.tex
   ```

2. **Update Master Document:**
   ```latex
   \input{newsection}  % Add to main.tex
   ```

3. **Define Required Commands:**
   ```latex
   % Add to latexdefs.tex if needed
   \newcommand{\newconcept}{\mathsf{NewConcept}}
   ```

### Adding New Notation

1. **Categorize the Command:**
   - Basic mathematical structure?
   - Cryptographic primitive?
   - Protocol element?
   - Security definition?

2. **Follow Naming Conventions:**
   ```latex
   \newcommand{\newcommmand}{\mathsf{NewCommand}}  % Functions
   \newcommand{\newset}{\mathcal{S}}               % Sets
   \newcommand{\newfield}{\mathbb{F}}              % Fields
   ```

3. **Document Usage:**
   - Add to API_REFERENCE.md
   - Include usage examples
   - Specify any dependencies

### Customization Points

**Document Layout:**
- Page margins: `geometry` package options
- Font choices: `fontspec` configuration
- Color scheme: `xcolor` definitions

**Mathematical Style:**
- Theorem environments: `amsthm` customization
- Equation formatting: `amsmath` options
- Symbol choices: Custom command definitions

**Citation Style:**
- Bibliography format: `biblatex` style options
- Citation appearance: Style file modifications
- Reference formatting: `cleveref` customization

This architecture supports the whitepaper's goals of technical rigor, collaborative development, and professional presentation while maintaining flexibility for future enhancements.