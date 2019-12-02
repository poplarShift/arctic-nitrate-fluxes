#!/bin/bash

source activate nitrateflux


### clone git archive to make sure we only get files into the docker that are part of the repo
tmpdir=_tmp_repo2docker
rm -rf $tmpdir
git clone . $tmpdir

### export bibliography
pushd paper
file='paper'
tmp='_tmp_bibexport'
bib='bibliography.bib'
bib_full='bibliographyfull.bib'

# generate standalone tex file
pandoc --bibliography $bib_full --filter pandoc-crossref --filter pandoc-citeproc --natbib --csl markdown_template/frontiers.csl -s -o $tmp.tex $file.md
# generate latex aux file
lualatex $tmp.tex
bibtex $tmp
bibexport -o $bib $tmp.aux
# move exported bib file into tmp dir
cp $bib ../$tmpdir/paper
# clean up
rm $tmp.*
rm $bib-save*
rm texput.log

popd


### enter archive and create docker image
pushd $tmpdir
repo2docker --no-run --image-name=nitrateflux .
popd
rm -rf $tmpdir

source deactivate
