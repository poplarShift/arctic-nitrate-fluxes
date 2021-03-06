#!/bin/bash

tmp='_tmp_bibexport'
infile=${articlefile}_static

# generate standalone tex file
pandoc --bibliography $bib_full --filter pandoc-crossref --filter pandoc-citeproc --natbib --csl frontiers.csl -s -o $tmp.tex $infile.md
# generate latex aux file
lualatex $tmp.tex
bibtex $tmp
bibexport -o $bib $tmp.aux
# clean up
rm $tmp.*
rm $bib-save*
rm texput.log
