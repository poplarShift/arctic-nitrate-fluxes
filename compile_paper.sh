#!/bin/bash

# convert figures for frontiers in...
pushd nb_fig
for f in *.png; do convert "$f" "${f%%.*}.tiff"; done
popd
pushd fig
for f in *.png; do convert "$f" "${f%%.*}.tiff"; done
popd

cslfile='frontiers.csl'
articlefile='paper'
bib='bibliography.bib'
bib_full='bibliographyfull.bib'

pushd paper # ./paper

# preferably use full bib file, but if unavailable (e.g. in exported docker or
# public repo) then use the reduced file (exported with bibexport during the
# build of the full docker)
if [ -f $bib_full ]; then
  bib=$bib_full
fi

echo Using bibfile: $bib

# create static version from master
# here, we used CriticMarkup to use a syntax that's already used by at least someone
# First insert newlines after closing brackets so the regex matching becomes easier (otherwise, lumps together all bracket expressions per line).
perl -0777 -pe 's/~~}/~~}\n/g' $articlefile.md > ${articlefile}_tmp.md
# the first option refers to the static version (e.g. png figures), the second to the interactive one (html figures)
perl -0777 -pe 's/{~~(.*)~>(.*)~~}\n/\1/g' ${articlefile}_tmp.md > ${articlefile}_static.md
perl -0777 -pe 's/{~~(.*)~>(.*)~~}\n/\2/g' ${articlefile}_tmp.md > ${articlefile}_interactive.md
rm ${articlefile}_tmp.md

# include height of each HTML element in markdown
# should find a better solution than Selenium+PhantomJS (deprecation warning)
python add_html_heights_to_interactive_markdown.py ${articlefile}_interactive.md

# --- compile Frontiers draft
# -docx
pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl $cslfile --reference-doc reference.docx --mathjax -o ${articlefile}.docx ${articlefile}_static.md

# now that Frontiers draft is done, move figures up into text
python move_figures_into_text.py ${articlefile}_static.md
python move_figures_into_text.py ${articlefile}_interactive.md
# --- static paper
# -html
pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl $cslfile --mathjax --self-contained --resource-path=.:../nb_fig/:../fig -o ${articlefile}_static.html ${articlefile}_static.md

# # -pdf
# pandoc --bibliography $bib --pdf-engine=xelatex --filter pandoc-crossref --filter pandoc-citeproc --csl markdown_template/frontiers.csl --mathjax -o ${articlefile}.pdf ${articlefile}_static.md

# --- compile interactive paper
pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl $cslfile  --self-contained --resource-path=.:../nb_fig/:../fig -o ${articlefile}_interactive.html ${articlefile}_interactive.md

# clean up
rm ${articlefile}_static.md ${articlefile}_interactive.md

popd # ./
