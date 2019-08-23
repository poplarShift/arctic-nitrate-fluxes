#!/bin/bash

source activate nitrateflux

pushd nb
for file in `ls [A,B,C]*.ipynb`
do
  fname=`echo $file | cut -d'.' -f 1`
  # render to html
  jupyter nbconvert --to html --output=../nb_html/$fname $fname
  # clear outputs
  jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to notebook --output=$fname $fname
done
popd

pushd paper # ./paper

file='paper'
bib='bibliography.bib'

# sed -i '' -e 's/NO3/NO₃/g' $file.md

# rm $bib
# ln -s ~/Documents/library/_MASTER_BIBLIOGRAPHY.bib $bib

jupyter nbconvert --to notebook --output make_paper_interactive.ipynb --execute make_paper_interactive.ipynb
pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl markdown_template/frontiers.csl  --self-contained --resource-path=.:../nb_fig/:../fig -o ${file}_interactive.html ${file}_interactive.md
rm ${file}_interactive.md

pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl markdown_template/frontiers.csl --mathjax -s  --self-contained --resource-path=.:../nb_fig/:../fig -o ${file}.html $file.md

# # export bibliography to local file
# pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl markdown_template/frontiers.csl --mathjax -s  -o ${file}.tex $file.md
#
# # pushd latex # ./paper/latex
# pdflatex $file.tex
# bibexport -o $bib $file.aux
# rm *.out *.aux *.blg *.log *.toc *.fff *.lof *.idx
# # rm latex/$file.tex
# # popd # ./paper

popd # ./

source deactivate

# pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl=template/science.csl -s -o $file.docx $file.md

# pushd markdown_template
#
# # pandoc +RTS -K512m -RTS --to latex --from markdown+autolink_bare_uris+ascii_identifiers+tex_math_single_backslash  --template template.tex --highlight-style tango --pdf-engine pdflatex --filter pandoc-citeproc --output paper.tex ../paper.md
#
# popd

# pandoc -V geometry:margin=1in --number-sections -csl markdown_template/frontiers.csl --bibliography $bib -o paper.pdf paper.md
