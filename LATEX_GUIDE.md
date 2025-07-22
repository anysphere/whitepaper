# LaTeX Guide for Anysphere Whitepaper

This guide covers LaTeX-specific aspects of working with the Anysphere whitepaper.

## Document Class and Setup

The document uses a custom article setup with specific formatting:

```latex
\documentclass{article}
\usepackage[margin=1.7in]{geometry}
\pagenumbering{arabic}
```

### Key Packages Used

- **geometry**: Page layout and margins
- **cryptocode**: Cryptographic protocols and notation
- **clrscode4e**: Algorithm formatting (CLRS textbook style)
- **biblatex**: Modern bibliography management
- **amsmath, amsfonts, amssymb**: Mathematical notation
- **tikz**: Diagrams and figures
- **xcolor**: Color support for annotations

## Custom Commands and Macros

### Author Annotations

```latex
\stzh{comment}    % Blue comment from stzh
```

### Mathematical Notation

The document defines many custom commands in `latexdefs.tex`. Key examples:

```latex
% Cryptographic primitives
\newcommand{\enc}[1]{\texttt{Enc}(#1)}
\newcommand{\dec}[1]{\texttt{Dec}(#1)}
\newcommand{\hash}[1]{\texttt{H}(#1)}

% Protocol notation
\newcommand{\alice}{\texttt{Alice}}
\newcommand{\bob}{\texttt{Bob}}
\newcommand{\server}{\texttt{Server}}

% Mathematical operators
\newcommand{\concat}{\mathbin{\|}}
\newcommand{\xor}{\oplus}
```

## Writing Cryptographic Protocols

### Using cryptocode Package

The `cryptocode` package provides excellent support for cryptographic protocols:

```latex
\begin{protocol}
\textbf{Key Exchange Protocol}
\begin{enumerate}
\item $\alice$ generates random $r_A \leftarrow \{0,1\}^{256}$
\item $\alice \to \bob$: $g^{r_A}$
\item $\bob$ generates random $r_B \leftarrow \{0,1\}^{256}$
\item $\bob \to \alice$: $g^{r_B}$
\item Both compute shared key $k = g^{r_A \cdot r_B}$
\end{enumerate}
\end{protocol}
```

### Algorithm Formatting

Use the `clrscode4e` package for algorithms:

```latex
\begin{codebox}
\Procname{$\proc{PIR-Query}(index, database)$}
\li $query \gets \proc{Generate-Query}(index)$
\li $response \gets \proc{Server-Process}(query, database)$
\li $result \gets \proc{Extract-Result}(response, index)$
\li \Return $result$
\end{codebox}
```

## Mathematical Typesetting

### Security Definitions

Format security definitions clearly:

```latex
\begin{definition}[Metadata Privacy]
A communication system provides \emph{metadata privacy} if an adversary 
cannot distinguish between:
\begin{itemize}
\item Communication patterns $(A_1 \leftrightarrow B_1, \ldots, A_n \leftrightarrow B_n)$
\item Random communication patterns of the same size
\end{itemize}
with probability better than $\frac{1}{2} + \text{negl}(\lambda)$.
\end{definition}
```

### Probability Notation

Use consistent probability notation:

```latex
\Pr[\text{event}]           % Probability of event
\Pr[X = x]                  % Probability X equals x
\mathbb{E}[X]              % Expected value
X \sim \mathcal{D}         % X is distributed according to D
```

## Citations and References

### Bibliography Management

The document uses `biblatex` with `biber` backend:

```latex
% In preamble.tex
\usepackage[backend=biber,style=alphabetic]{biblatex}
\addbibresource{bib.bib}

% In main.tex
\printbibliography
```

### Citation Styles

```latex
\cite{key}                  % Basic citation [ABC21]
\textcite{key}             % Textual: "Smith et al. [ABC21]"
\parencite{key}            % Parenthetical: (Smith et al., 2021)
\cite[p.~42]{key}          % With page number
\cite{key1,key2,key3}      % Multiple citations
```

### Adding Bibliography Entries

In `bib.bib`:

```bibtex
@article{key,
  author    = {Author Name and Another Author},
  title     = {Paper Title},
  journal   = {Journal Name},
  year      = {2021},
  volume    = {42},
  pages     = {123--145},
  doi       = {10.1000/182},
  url       = {https://example.com/paper.pdf}
}

@inproceedings{conference-paper,
  author    = {Conference Author},
  title     = {Conference Paper Title},
  booktitle = {Proceedings of Important Conference},
  year      = {2021},
  pages     = {456--789},
  publisher = {ACM},
  doi       = {10.1145/1234567.1234568}
}
```

## Figures and Diagrams

### Including PDF Figures

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{systemdiagram.pdf}
\caption{System architecture overview}
\label{fig:system}
\end{figure}
```

### TikZ Diagrams

For simple diagrams, use TikZ:

```latex
\begin{figure}[htbp]
\centering
\begin{tikzpicture}
\node[draw, rectangle] (alice) at (0,0) {Alice};
\node[draw, rectangle] (server) at (4,0) {Server};
\node[draw, rectangle] (bob) at (8,0) {Bob};

\draw[->] (alice) -- node[above] {Query} (server);
\draw[->] (server) -- node[above] {Response} (bob);
\end{tikzpicture}
\caption{Protocol message flow}
\label{fig:protocol}
\end{figure}
```

## Cross-References

### Section References

```latex
\section{Introduction}
\label{sec:introduction}

% Reference with automatic text
\autoref{sec:introduction}        % "Section 1"
\nameref{sec:introduction}        % "Introduction"
\ref{sec:introduction}            % "1"
```

### Equation References

```latex
\begin{equation}
E = mc^2
\label{eq:einstein}
\end{equation}

% Reference the equation
\autoref{eq:einstein}             % "Equation (1)"
\eqref{eq:einstein}               % "(1)"
```

## Building Best Practices

### Incremental Building

For faster development, use incremental building:

```bash
# Watch mode (rebuilds on file changes)
make

# Single build
make once

# Clean build (when things break)
make clean && make once
```

### Dealing with Build Errors

Common LaTeX errors and solutions:

1. **Undefined control sequence**: Check for typos in command names
2. **Missing $ inserted**: Math mode issues - check for unescaped special characters
3. **Bibliography errors**: Run the full build sequence (pdflatex → biber → pdflatex × 2)
4. **Package not found**: Install missing packages with `tlmgr install package-name`

### Performance Tips

- Use `\includeonly{}` for working on specific sections
- Keep figures in separate files
- Use draft mode during writing: `\documentclass[draft]{article}`
- Comment out time-consuming TikZ diagrams during development

## Code Organization

### File Structure

```
main.tex              # Document root
├── preamble.tex      # Packages and setup
├── latexdefs.tex     # Custom commands
├── abs.tex           # Abstract
├── introduction.tex  # Individual sections
├── ...
├── bib.bib          # Bibliography
└── figures/         # External figures
```

### Section Template

Each section file should follow this pattern:

```latex
\section{Section Title}
\label{sec:sectionname}

Brief introduction to the section...

\subsection{Subsection}
\label{sec:sectionname:subsection}

Content with proper references \cite{key} and cross-references 
\autoref{sec:previous:section}.

% Use consistent notation from latexdefs.tex
The protocol ensures that $\alice$ can communicate with $\bob$ 
through server $\server$ without revealing metadata.
```

## Quality Assurance

### Spell Checking

```bash
# Check individual files
aspell --mode=tex check introduction.tex

# Check all tex files
find . -name "*.tex" -exec aspell --mode=tex check {} \;
```

### Style Consistency

- Use `\emph{}` for emphasis, not `\textit{}`
- Use `\texttt{}` for code/protocol names
- Use consistent mathematical notation
- Follow cryptographic convention for variable names
- Use proper spacing around mathematical operators

### Common LaTeX Pitfalls

1. **Spacing**: Use `\ ` for forced spaces, `~` for non-breaking spaces
2. **Quotes**: Use `` `text' `` or `` ``text'' `` not `"text"`
3. **Dashes**: Use `--` for en-dash, `---` for em-dash
4. **Mathematical mode**: Always use `$...$` or `\(...\)` for inline math
5. **References**: Always use `\autoref{}` instead of manual "Section X" text

This guide should help maintain consistency and quality in the LaTeX source while making the document easier to work with for all contributors.