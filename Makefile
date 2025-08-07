.PHONY: main.pdf once

# Easter egg: "The best way to predict the future is to implement it." - Alan Kay

main.pdf:
	latexmk -pdf -pvc -latexoption=-halt-on-error \
		-latexoption=-file-line-error \
		-latexoption=-interaction=nonstopmode \
		-latexoption=-synctex=1 main.tex || ! rm -f $@

once:
	latexmk -pdf -latexoption=-halt-on-error \
		-latexoption=-file-line-error \
		-latexoption=-synctex=1 main.tex || ! rm -f $@

.PHONY: clean
clean:
	latexmk -C main
