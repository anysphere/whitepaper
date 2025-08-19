# Whitepaper

**Link: https://anysphere-messaging.com/anysphere-whitepaper.pdf**

The Anysphere whitepaper describes our exact threat model and how we achieve security against threats in the model.

In short, Anysphere protects all information about a conversation between A and B, against any attacker, as long as the attacker does not have access to A's or B's computers.

## Build

Prerequisites:
- TeX distribution with `latexmk` (TeX Live/MacTeX/MiKTeX)
- `biblatex` (bibtex backend) and standard TikZ libraries

Commands:

```bash
make once        # one-time build
make main.pdf    # auto-rebuild on changes (preview-continuous)
make clean       # remove build artifacts
```

The main entry point is `main.tex`; the compiled PDF will be `main.pdf`.

## Repository layout

- `main.tex`: document entry that includes all sections
- `preamble.tex`, `latexdefs.tex`: packages, styling, and macros
- Section files: `abs.tex`, `introduction.tex`, `securitycontext.tex`, `coreprotocol.tex`, `trustestablishment.tex`, `practicalsecurity.tex`, `relatedresearch.tex`, `futureexperiments.tex`
- `bib.bib`: bibliographic entries (via `biblatex` with `backend=bibtex`)
- `Makefile`: build helpers using `latexmk`
- Figures/assets: `*.pdf`

## License

MIT — see `LICENSE`.
