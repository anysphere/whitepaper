.PHONY: main.pdf once check

main.pdf:
	latexmk -pdf -pvc -latexoption=-halt-on-error \
		-latexoption=-file-line-error \
		-latexoption=-interaction=nonstopmode \
		-latexoption=-synctex=1 main.tex || ! rm -f $@

once:
	latexmk -pdf -latexoption=-halt-on-error \
		-latexoption=-file-line-error \
		-latexoption=-synctex=1 main.tex || ! rm -f $@

check:
	@echo "Checking LaTeX syntax..."
	@pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && echo "Syntax check passed" || echo "Syntax errors found"

.PHONY: clean
clean:
	latexmk -C main
