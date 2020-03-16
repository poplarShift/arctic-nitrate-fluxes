#!/bin/bash

# convert figures for frontiers in...
pushd nb_fig
for f in *.png; do convert "$f" "${f%%.*}.tiff"; done
popd
pushd fig
for f in *.png; do convert "$f" "${f%%.*}.tiff"; done
popd

export cslfile='frontiers.csl'
export articlefile='paper'
export bib='bibliography.bib'
export bib_full='bibliographyfull.bib'

cd paper # ./paper

./parse_articlefile.sh

# preferably use full bib file, but if unavailable (e.g. in exported docker or
# public repo) then use the reduced file (exported with bibexport)
if [ -f $bib_full ]; then
  ./export_bibliography.sh
  bib=$bib_full
fi

echo Using bibfile: $bib

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
pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl $cslfile --self-contained --resource-path=.:../nb_fig/:../fig --mathjax -o ${articlefile}_static.html ${articlefile}_static.md

# --- compile interactive paper
pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl $cslfile  --self-contained --resource-path=.:../nb_fig/:../fig --mathjaxn -o ${articlefile}_interactive.html ${articlefile}_interactive.md


# make version with tracked changes
./diff.sh

# clean up
rm ${articlefile}_static.md ${articlefile}_interactive.md

cd .. # ./
