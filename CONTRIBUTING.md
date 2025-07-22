# Contributing to Anysphere Whitepaper

Thank you for your interest in contributing to the Anysphere security whitepaper! This document provides guidelines for contributors.

## Getting Started

### Prerequisites

1. **LaTeX Environment**
   - Install a complete LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
   - Ensure `pdflatex`, `biber`, and `latexmk` are available
   - See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for installation help

2. **Development Tools**
   - Git for version control
   - Text editor with LaTeX support (VS Code with LaTeX Workshop, TeXstudio, etc.)
   - Make utility for build automation

3. **Repository Setup**
   ```bash
   git clone [repository-url]
   cd anysphere-whitepaper
   make once  # Test build
   ```

## Contribution Types

### Content Contributions

#### Technical Content
- Protocol descriptions and improvements
- Security analysis and proofs
- Mathematical formulations
- Algorithm specifications

#### Documentation
- Clarifying explanations
- Additional examples
- Improved notation
- Cross-references and citations

#### Review and Editing
- Proofreading for grammar and clarity
- Technical accuracy verification
- Consistency checks
- Citation verification

### Technical Contributions

#### LaTeX Infrastructure
- Custom commands and macros
- Document formatting improvements
- Build system enhancements
- Figure and diagram creation

#### Tooling
- Scripts for automation
- CI/CD improvements
- Documentation generation
- Quality assurance tools

## Contribution Process

### 1. Planning Your Contribution

Before starting work:

1. **Check existing issues** for related work
2. **Open an issue** to discuss significant changes
3. **Review recent commits** to avoid conflicts
4. **Understand the scope** of your proposed changes

### 2. Making Changes

#### Branch Management
```bash
# Create a feature branch
git checkout -b feature/your-contribution-name

# Keep your branch updated
git fetch origin
git rebase origin/main
```

#### Content Guidelines

**Writing Style:**
- Use clear, precise technical language
- Follow established notation conventions
- Maintain consistency with existing content
- Include proper citations for all references

**Mathematical Notation:**
- Use custom commands from `latexdefs.tex`
- Follow established conventions (see [API_REFERENCE.md](API_REFERENCE.md))
- Ensure all math is properly formatted
- Include clear variable definitions

**Protocol Descriptions:**
- Start with clear setup and assumptions
- Number steps consistently
- Specify inputs and outputs explicitly
- Include security analysis

#### Technical Guidelines

**LaTeX Best Practices:**
- Use semantic markup over formatting commands
- Define reusable commands for repeated elements
- Maintain consistent indentation and structure
- Comment complex LaTeX constructions

**File Organization:**
- Keep related content in appropriate `.tex` files
- Update `main.tex` if adding new sections
- Place figures in the root directory
- Update bibliography in `bib.bib`

### 3. Testing Your Changes

#### Build Testing
```bash
# Clean build test
make clean
make once

# Continuous build test
make  # Uses latexmk for continuous compilation

# Check for warnings
grep -i warning main.log
```

#### Content Review
- Spell-check all content
- Verify all citations resolve correctly
- Check figure references and captions
- Ensure cross-references work properly
- Review mathematical notation for consistency

#### Technical Validation
- Test all custom LaTeX commands
- Verify bibliography compilation
- Check PDF output quality
- Validate against style guidelines

### 4. Submitting Your Contribution

#### Commit Guidelines

**Commit Messages:**
```
type(scope): brief description

Longer explanation if needed.

- Bullet points for multiple changes
- Reference issues: Fixes #123
```

**Commit Types:**
- `content`: Changes to whitepaper content
- `docs`: Documentation updates
- `latex`: LaTeX infrastructure changes
- `build`: Build system modifications
- `fix`: Bug fixes
- `style`: Formatting and style changes

**Examples:**
```bash
git commit -m "content(protocol): add formal security proof for PIR construction"
git commit -m "docs(api): expand cryptographic primitives reference"
git commit -m "latex: add command for protocol message notation"
```

#### Pull Request Process

1. **Prepare your PR:**
   - Ensure all commits are clean and well-documented
   - Rebase against the latest main branch
   - Test the final build thoroughly

2. **Create the pull request:**
   - Use a descriptive title
   - Include a detailed description of changes
   - Reference any related issues
   - Add screenshots for visual changes

3. **PR Description Template:**
   ```markdown
   ## Summary
   Brief description of the changes.

   ## Changes Made
   - Specific change 1
   - Specific change 2

   ## Testing
   - [ ] Document builds successfully
   - [ ] No new warnings or errors
   - [ ] Citations resolve correctly
   - [ ] Figures display properly

   ## Related Issues
   Fixes #123, Related to #456
   ```

## Review Process

### What Reviewers Look For

**Content Review:**
- Technical accuracy and completeness
- Clarity and readability
- Consistency with existing content
- Proper citation and attribution

**Technical Review:**
- LaTeX syntax and best practices
- Build system compatibility
- Documentation completeness
- Code quality and maintainability

### Addressing Review Feedback

1. **Respond promptly** to review comments
2. **Make requested changes** in additional commits
3. **Explain your reasoning** for any disagreements
4. **Test thoroughly** after making changes
5. **Update documentation** if needed

## Style Guidelines

### LaTeX Conventions

#### Document Structure
```latex
% Section organization
\section{Main Topic}
\subsection{Subtopic}
\subsubsection{Detailed Point}

% Use labels for cross-references
\section{Protocol Description}\label{sec:protocol}
See Section~\ref{sec:protocol} for details.
```

#### Mathematical Notation
```latex
% Use custom commands
\alice sends \enc{m} to \bob
\adversary cannot distinguish between $m_0$ and $m_1$

% Avoid direct symbols
% Wrong: Alice sends Enc(m) to Bob
% Right: \alice sends \enc{m} to \bob
```

#### Citations and References
```latex
% Proper citation format
This result was proven by Smith et al.~\cite{smith2023}.
As shown in~\citet{jones2022}, the protocol is secure.

% Figure references
Figure~\ref{fig:protocol} illustrates the message flow.
```

### Content Style

#### Technical Writing
- Use active voice when possible
- Define all technical terms on first use
- Maintain parallel structure in lists
- Use consistent terminology throughout

#### Mathematical Exposition
- Introduce notation before using it
- Explain the intuition behind formal definitions
- Provide examples for complex concepts
- Include security analysis for all protocols

## Quality Assurance

### Pre-submission Checklist

**Content:**
- [ ] All technical claims are accurate
- [ ] Mathematical notation is consistent
- [ ] Citations are complete and correct
- [ ] Figures are properly referenced
- [ ] Cross-references work correctly

**Technical:**
- [ ] Document builds without errors
- [ ] No new warnings introduced
- [ ] LaTeX code follows conventions
- [ ] Custom commands are documented
- [ ] Bibliography compiles correctly

**Documentation:**
- [ ] Changes are documented appropriately
- [ ] API references updated if needed
- [ ] Examples provided for new features
- [ ] Related documentation updated

### Continuous Integration

The repository uses automated checks:
- **Build verification:** Ensures document compiles
- **Style checking:** Validates LaTeX conventions
- **Link verification:** Checks external references
- **Spell checking:** Catches common errors

## Communication

### Getting Help

- **General questions:** Open a GitHub issue
- **Technical problems:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Style questions:** Refer to [LATEX_GUIDE.md](LATEX_GUIDE.md)
- **API documentation:** Check [API_REFERENCE.md](API_REFERENCE.md)

### Community Guidelines

- Be respectful and constructive in all interactions
- Focus on the technical merits of contributions
- Provide specific, actionable feedback
- Acknowledge the work of others
- Help newcomers get started

## Recognition

Contributors are acknowledged in:
- Git commit history
- Acknowledgments section of the whitepaper
- Contributor list in the repository
- Release notes for significant contributions

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project. See [LICENSE](LICENSE) for details.

## Questions?

If you have questions about contributing that aren't covered here:
1. Check existing documentation
2. Search through past issues and PRs
3. Open a new issue with the "question" label
4. Contact the maintainers directly if needed

Thank you for helping improve the Anysphere whitepaper!