FILE=main

all: $(FILE).pdf

$(FILE).pdf:
	latexmk -lualatex -pdf $(FILE).tex

clean:
	rm -f *~ *.aux *.log *.out *.blg *.bbl *.makefile *.auxlock *.figlist *.toc \
		src/figs/tmp_tikz/* *.fdb_latexmk *.fls *.lof *.lot *.synctex.gz \
		*.vrb *.snm *.nav

.PHONY: $(FILE).pdf clean