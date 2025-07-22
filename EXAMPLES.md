# Examples and Use Cases

This document provides practical examples of working with the Anysphere whitepaper, including common LaTeX patterns, mathematical notation, and development workflows.

## Getting Started Examples

### Basic Build Workflow

```bash
# Clone and setup
git clone [repository-url]
cd anysphere-whitepaper

# Test build
make once

# Development with auto-rebuild
make

# Clean rebuild
make clean && make once
```

### First Contribution Workflow

```bash
# Create feature branch
git checkout -b add-security-proof

# Make changes to content
vim coreprotocol.tex

# Test changes
make once

# Commit and push
git add coreprotocol.tex
git commit -m "content(protocol): add formal security proof"
git push origin add-security-proof
```

## LaTeX Examples

### Mathematical Notation

#### Basic Cryptographic Operations

```latex
% Protocol participants
\alice generates a key pair $(pk, sk)$.
\bob receives the public key $pk$ from \alice.
The \adversary cannot distinguish between encryptions.

% Cryptographic functions
Let $c = \enc_{pk}(m)$ be the encryption of message $m$.
The decryption yields $m' = \dec_{sk}(c)$.
We require that $m = m'$ with overwhelming probability.

% Hash functions and random oracles
The hash function $\Hash: \{0,1\}^* \to \{0,1\}^{256}$ is modeled as a random oracle.
```

#### Advanced Mathematical Structures

```latex
% Finite fields and groups
Let $\F_p$ be a finite field of prime order $p$.
Consider the elliptic curve group $\G$ over $\F_p$.
The discrete logarithm problem in $\G$ is assumed to be hard.

% Probability and expectations
The probability that the adversary succeeds is $\Pr[A \text{ wins}] \leq \negl(\lambda)$.
The expected running time is $\E[T] = \poly(\lambda)$.
```

### Protocol Descriptions

#### Simple Protocol Example

```latex
\begin{protocol}[Key Exchange]
\item \textbf{Setup:} \alice and \bob agree on group $\G$ and generator $g$.
\item \textbf{Round 1:} 
  \begin{itemize}
  \item \alice samples $a \leftarrow \Z_p$ and sends $A = g^a$ to \bob
  \item \bob samples $b \leftarrow \Z_p$ and sends $B = g^b$ to \alice
  \end{itemize}
\item \textbf{Key Derivation:} Both parties compute $K = \Hash(g^{ab})$
\item \textbf{Output:} Shared secret key $K$
\end{protocol}
```

#### Complex Protocol with Security Analysis

```latex
\begin{protocol}[Private Information Retrieval]
\item \textbf{Setup:} Server holds database $D = (d_1, \ldots, d_n)$
\item \textbf{Query Generation:} Client wants $d_i$ without revealing $i$
  \begin{enumerate}
  \item Generate random polynomial $p(x)$ with $p(i) = 1$, $p(j) = 0$ for $j \neq i$
  \item Send evaluations $(p(1), p(2), \ldots, p(n))$ to server
  \end{enumerate}
\item \textbf{Response:} Server computes $\sum_{j=1}^n p(j) \cdot d_j$ and returns result
\item \textbf{Security:} The polynomial evaluations are information-theoretically private
\end{protocol}
```

### Figure Integration

#### Including PDF Figures

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{protocol-diagram.pdf}
\caption{Message flow in the Anysphere protocol showing the interaction between 
         client, server, and PIR database.}
\label{fig:protocol-flow}
\end{figure}

% Reference the figure
As illustrated in \cref{fig:protocol-flow}, the client never reveals which 
database entry it is requesting.
```

#### Creating TikZ Diagrams

```latex
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[node distance=3cm, auto]
  % Nodes
  \node (client) [rectangle, draw] {Client};
  \node (server) [rectangle, draw, right of=client] {Server};
  \node (database) [rectangle, draw, below of=server] {Database};
  
  % Arrows
  \draw[->] (client) -- node {Query} (server);
  \draw[->] (server) -- node {Lookup} (database);
  \draw[->] (database) -- node {Response} (server);
  \draw[->] (server) -- node {Result} (client);
\end{tikzpicture}
\caption{System architecture overview}
\label{fig:system-arch}
\end{figure}
```

### Bibliography Examples

#### Adding Citations

```latex
% In bib.bib
@inproceedings{chor1995private,
  title={Private information retrieval},
  author={Chor, Benny and Goldreich, Oded and Kushilevitz, Eyal and Sudan, Madhu},
  booktitle={Proceedings of the 36th Annual Symposium on Foundations of Computer Science},
  pages={41--50},
  year={1995},
  organization={IEEE}
}

% In LaTeX content
The concept of Private Information Retrieval was introduced by 
\citet{chor1995private}. As shown in~\cite{chor1995private}, 
information-theoretic PIR requires multiple servers.
```

#### Different Citation Styles

```latex
% Textual citations
\citet{author2023} showed that the protocol is secure.

% Parenthetical citations  
The protocol is secure~\citep{author2023}.

% Multiple citations
Several works have addressed this problem~\citep{author2023,other2024,third2023}.

% Specific pages
The proof can be found in~\citep[Theorem 3.1]{author2023}.
```

## Development Workflows

### Adding New Mathematical Notation

#### 1. Define the Command

```latex
% In latexdefs.tex
\newcommand{\pir}{\mathsf{PIR}}                    % PIR protocol
\newcommand{\query}[1]{\mathsf{Query}(#1)}        % Query function
\newcommand{\response}[1]{\mathsf{Response}(#1)}  % Response function
```

#### 2. Document the Command

```latex
% Add to API_REFERENCE.md
\pir                    % Private Information Retrieval protocol
\query{index}           % Generate PIR query for given index
\response{database}     % Compute PIR response for database
```

#### 3. Use in Content

```latex
% In protocol description
The \pir protocol allows a client to compute $\query{i}$ such that
the server can return $\response{D}$ without learning $i$.
```

### Adding New Content Sections

#### 1. Create the File

```bash
touch newsection.tex
```

#### 2. Structure the Content

```latex
% newsection.tex
\section{New Section Title}\label{sec:newsection}

\subsection{Introduction}
This section covers...

\subsection{Technical Details}
The main contribution is...

\begin{theorem}[Main Result]\label{thm:main}
Under the assumptions of...
\end{theorem}

\begin{proof}
The proof proceeds by...
\end{proof}

\subsection{Analysis}
The implications of \cref{thm:main} are...
```

#### 3. Integrate into Document

```latex
% In main.tex
\input{introduction}
\input{securitycontext}
\input{coreprotocol}
\input{newsection}        % Add your section
\input{trustestablishment}
% ... rest of sections
```

### Review and Testing Workflow

#### Content Review Checklist

```bash
# Build test
make clean && make once

# Check for warnings
grep -i warning main.log

# Spell check (if aspell is available)
aspell check newsection.tex

# Citation verification
grep -n "cite{" *.tex | grep -v "citep\|citet"  # Find potential issues
```

#### Mathematical Consistency Check

```latex
% Verify notation consistency
% Search for direct usage instead of commands
grep -n "Alice\|Bob" *.tex          # Should use \alice, \bob
grep -n "Enc(\|Dec(" *.tex          # Should use \enc{}, \dec{}
grep -n "||" *.tex                  # Should use \concat
```

## Common Use Cases

### Security Proof Template

```latex
\begin{theorem}[Protocol Security]\label{thm:security}
The protocol satisfies computational privacy against polynomial-time adversaries
under the decisional Diffie-Hellman assumption.
\end{theorem}

\begin{proof}
We prove security via a sequence of games.

\paragraph{Game 0.} This is the original security game where...

\paragraph{Game 1.} We modify the game by replacing...

The advantage difference between consecutive games is negligible by...

\paragraph{Analysis.} In the final game, the adversary's advantage is 0 because...
\end{proof}
```

### Algorithm Description Template

```latex
\begin{algorithm}[H]
\caption{PIR Query Generation}
\label{alg:pir-query}
\begin{algorithmic}[1]
\Procedure{GenerateQuery}{$i, n$}
  \State $\mathcal{P} \gets$ random polynomial with $p(i) = 1$, $p(j) = 0$ for $j \neq i$
  \For{$j = 1$ to $n$}
    \State $q_j \gets p(j)$
  \EndFor
  \State \Return $(q_1, q_2, \ldots, q_n)$
\EndProcedure
\end{algorithmic}
\end{algorithm}
```

### Performance Analysis Template

```latex
\begin{table}[htbp]
\centering
\begin{tabular}{|l|c|c|c|}
\hline
\textbf{Parameter} & \textbf{Client} & \textbf{Server} & \textbf{Communication} \\
\hline
Computation & $O(n)$ & $O(n \cdot |D|)$ & -- \\
Storage & $O(1)$ & $O(n \cdot |D|)$ & -- \\
Bandwidth & -- & -- & $O(n + |D|)$ \\
\hline
\end{tabular}
\caption{Complexity comparison for different PIR schemes}
\label{tab:complexity}
\end{table}
```

## Advanced Examples

### Custom Environment Definition

```latex
% In latexdefs.tex
\newenvironment{construction}[1][Construction]{%
  \begin{framed}%
  \noindent\textbf{#1.}%
}{%
  \end{framed}%
}

% Usage
\begin{construction}[Secure PIR]
\item \textbf{Input:} Database $D$, query index $i$
\item \textbf{Protocol:} 
  \begin{enumerate}
  \item Client generates query $q \gets \query{i}$
  \item Server computes response $r \gets \response{D, q}$
  \item Client extracts $d_i$ from $r$
  \end{enumerate}
\item \textbf{Security:} The server learns nothing about $i$
\end{construction}
```

### Cross-Reference Management

```latex
% Define labels consistently
\section{Core Protocol}\label{sec:core}
\subsection{Security Analysis}\label{subsec:security}
\begin{theorem}[Privacy]\label{thm:privacy}
...
\end{theorem}

% Reference appropriately
As we prove in \cref{thm:privacy}, the protocol satisfies...
The security analysis in \cref{subsec:security} shows...
This builds on the protocol from \cref{sec:core}.
```

### Collaborative Development

#### Branch Management

```bash
# Feature branch for new content
git checkout -b feature/efficiency-analysis
# Make changes
git add -A
git commit -m "content(analysis): add efficiency comparison with existing schemes"

# Review branch for corrections
git checkout -b review/notation-consistency  
# Make corrections
git commit -m "style: standardize notation throughout document"

# Integration branch for major changes
git checkout -b integrate/new-protocol-section
# Integrate multiple features
git merge feature/efficiency-analysis
git merge review/notation-consistency
```

#### Merge Conflict Resolution

```latex
% When conflicts occur in LaTeX files
<<<<<<< HEAD
The protocol achieves $O(n)$ communication complexity.
=======
The protocol achieves $O(\sqrt{n})$ communication complexity.
>>>>>>> feature-branch

% Resolution strategy:
% 1. Understand both versions
% 2. Check which is technically correct
% 3. Maintain consistency with rest of document
% 4. Test build after resolution
```

This examples guide demonstrates practical patterns for working effectively with the Anysphere whitepaper. For more detailed information, see the related documentation files.