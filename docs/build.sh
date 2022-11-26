#!/usr/bin/env bash
name="technique_report"
pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=. $name.tex
bibtex $name.aux
pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=. $name.tex
pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=. $name.tex

rm $name.blg
rm $name.log
rm $name.out
rm *.aux
rm $name.bbl
rm $name.synctex.gz
