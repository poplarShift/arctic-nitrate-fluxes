#!/bin/bash

file='paper_static'
tmp='_tmp_bibexport'
bib='bibliography.bib'
bib_full='bibliographyfull.bib'


# generate standalone tex file
pandoc --bibliography $bib_full --filter pandoc-crossref --filter pandoc-citeproc --natbib --csl frontiers.csl -s -o $tmp.tex $file.md
# generate latex aux file
lualatex $tmp.tex
bibtex $tmp
bibexport -o $bib $tmp.aux
# clean up
rm $tmp.*
rm $bib-save*
rm texput.log
