#!/bin/bash

tmpdir=_tmp_manuscript_diff

cslfile='frontiers.csl'
export articlefile='paper'
bib='bibliography.bib'

git clone -b v0.1.1 .. $tmpdir

# pandiff $tmpdir/paper/paper_static.md paper/paper_static.md -o paper/paper_trackchanges.docx

# parse papers both in old and new versions

# old
cd $tmpdir/paper
./parse_articlefile.sh
cd ../..
# new
./parse_articlefile.sh

wdiff $tmpdir/paper/${articlefile}_static.md ${articlefile}_static.md | ./markdown-format-wdiff > ${articlefile}_trackchanges.md

pandoc --bibliography $bib --filter pandoc-crossref --filter pandoc-citeproc --csl $cslfile --self-contained --resource-path=.:../nb_fig/:../fig -o ${articlefile}_trackchanges.html ${articlefile}_trackchanges.md

rm -rf $tmpdir
