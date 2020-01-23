#!/bin/bash

source activate nitrateflux


### clone git archive to make sure we only get files into the docker that are part of the repo
tmpdir=_tmp_repo2docker
rm -rf $tmpdir
git clone . $tmpdir

### export bibliography
pushd paper
./export_bibliography.sh
# move exported bib file into tmp dir
cp $bib ../$tmpdir/paper
popd


### enter archive and create docker image
pushd $tmpdir
repo2docker --no-run --image-name=nitrateflux .
popd
rm -rf $tmpdir

source deactivate
