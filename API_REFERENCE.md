# API Reference

This document provides a comprehensive reference for all LaTeX commands, macros, and environments defined in the Anysphere whitepaper.

## Custom Commands

### Author Annotations

Commands for adding author-specific comments and annotations:

```latex
\stzh{comment}          % Blue comment from stzh
\arvid{comment}         % Comment from arvid  
\sualeh{comment}        % Comment from sualeh
```

**Usage Example:**
```latex
This protocol ensures security \stzh{need to verify this claim}.
```

### Mathematical Notation

#### Cryptographic Primitives

```latex
\enc{plaintext}         % Encryption function: Enc(plaintext)
\dec{ciphertext}        % Decryption function: Dec(ciphertext)  
\hash{input}            % Hash function: H(input)
\sign{message}          % Digital signature: Sign(message)
\verify{signature}      % Signature verification: Verify(signature)
```

#### Protocol Participants

```latex
\alice                  % Alice (party A)
\bob                    % Bob (party B)
\server                 % Server entity
\adversary              % Adversary/attacker
```

#### Mathematical Operators

```latex
\concat                 % Concatenation operator (||)
\xor                    % XOR operation (⊕)
\assign                 % Assignment operator
\sample                 % Random sampling operator
\negligible             % Negligible function notation
```

#### Set Theory and Probability

```latex
\prob{event}            % Probability notation: Pr[event]
\expect{variable}       % Expected value: E[variable]
\uniform{set}           % Uniform distribution over set
\poly{variable}         % Polynomial function
\negl{variable}         % Negligible function
```

### Protocol Notation

#### Message Exchange

```latex
\send{sender}{receiver}{message}     % Message sending notation
\receive{receiver}{message}          % Message receiving notation
\broadcast{sender}{message}          % Broadcast message
```

#### Cryptographic Operations

```latex
\keygen                 % Key generation algorithm
\keyexchange            % Key exchange protocol
\commitment{value}      % Cryptographic commitment
\reveal{commitment}     % Commitment revelation
```

### Security Definitions

```latex
\indcpa                 % IND-CPA security
\indcca                 % IND-CCA security
\semantic              % Semantic security
\computational         % Computational security
\information           % Information-theoretic security
```

## Environments

### Protocol Descriptions

#### `protocol` Environment

For describing cryptographic protocols:

```latex
\begin{protocol}[Protocol Name]
\item Setup: Description of setup phase
\item Round 1: First round of communication
\item Round 2: Second round of communication
\item Output: Final output or result
\end{protocol}
```

#### `construction` Environment

For formal constructions:

```latex
\begin{construction}[Construction Name]
\item Input: Required inputs
\item Algorithm: Step-by-step algorithm
\item Output: Generated output
\end{construction}
```

#### `definition` Environment

For security definitions and formal definitions:

```latex
\begin{definition}[Definition Name]
A formal definition of a security property or cryptographic primitive.
\end{definition}
```

#### `theorem` Environment

For formal theorems and proofs:

```latex
\begin{theorem}[Theorem Name]
Statement of the theorem.
\end{theorem}

\begin{proof}
Proof of the theorem.
\end{proof}
```

### Algorithm Formatting

The document uses the `clrscode4e` package for algorithm formatting:

```latex
\begin{codebox}
\Procname{$\proc{Algorithm-Name}(input)$}
\li \Return output
\end{codebox}
```

**Advanced Algorithm Example:**
```latex
\begin{codebox}
\Procname{$\proc{PIR-Query}(database, index)$}
\li $query \gets \proc{Generate-Query}(index)$
\li $response \gets \proc{Server-Process}(database, query)$ 
\li $result \gets \proc{Extract-Result}(response, index)$
\li \Return $result$
\end{codebox}
```

## Figure and Diagram Commands

### TikZ Integration

Commands for creating protocol diagrams and figures:

```latex
\protocoldiagram{participants}{messages}    % Protocol flow diagram
\systemarchitecture{components}             % System architecture diagram
\threatmodel{adversaries}{capabilities}     % Threat model visualization
```

### PDF Figures

For including external PDF figures:

```latex
\includefigure{filename}{caption}{label}    % Include PDF figure
\referencefigure{label}                     % Reference to figure
```

## Bibliography and Citations

### Citation Commands

```latex
\cite{key}              % Basic citation
\citep{key}             % Parenthetical citation
\citet{key}             % Textual citation
\citeauthor{key}        % Author name only
\citeyear{key}          % Year only
```

### Bibliography Entries

The document uses `biblatex` with the following entry types:

- `@article` - Journal articles
- `@inproceedings` - Conference papers  
- `@book` - Books and monographs
- `@techreport` - Technical reports
- `@misc` - Miscellaneous sources

## Document Structure Commands

### Section Organization

```latex
\mainsection{title}     % Main section with special formatting
\subsectionref{label}   % Reference to subsection
\appendixsection{title} % Appendix section formatting
```

### Cross-References

```latex
\sectionref{label}      % Reference to section
\figureref{label}       % Reference to figure  
\tableref{label}        % Reference to table
\algorithmref{label}    % Reference to algorithm
\protocolref{label}     % Reference to protocol
```

## Compilation Notes

### Required Packages

Ensure these packages are installed:
- `cryptocode` - Cryptographic notation
- `clrscode4e` - Algorithm formatting
- `biblatex` - Bibliography management
- `tikz` - Diagrams and figures
- `amsmath` - Mathematical notation

### Build Process

1. `pdflatex main.tex` - Initial compilation
2. `biber main` - Bibliography processing  
3. `pdflatex main.tex` - Resolve citations
4. `pdflatex main.tex` - Final formatting

### Common Issues

- **Missing packages**: Install via `tlmgr install package-name`
- **Bibliography errors**: Ensure `biber` is installed and run
- **Figure issues**: Check PDF figure paths and permissions
- **Macro conflicts**: Check for duplicate command definitions

## Style Guidelines

### Notation Consistency

- Use `\alice` and `\bob` for protocol participants
- Use `\server` for server entities
- Use `\adversary` for attackers
- Use `\concat` for concatenation, not `||`
- Use `\xor` for XOR operations, not `\oplus`

### Mathematical Formatting

- Enclose all mathematical expressions in `$...$` or `\[...\]`
- Use `\text{}` for text within math mode
- Use `\texttt{}` for protocol names and algorithms
- Use `\emph{}` for emphasis, not `\textit{}`

### Protocol Descriptions

- Start each protocol with a clear setup phase
- Number communication rounds consistently  
- Clearly specify inputs and outputs
- Include security analysis after each protocol

This API reference covers the main commands and conventions used throughout the Anysphere whitepaper. For additional LaTeX guidance, see [LATEX_GUIDE.md](LATEX_GUIDE.md).