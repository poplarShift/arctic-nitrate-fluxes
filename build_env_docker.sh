#!/bin/bash

source activate nitrateflux

tmpdir=_tmp_repo2docker
tmpdir_envfile=_tmp

rm -rf $tmpdir $tmpdir_envfile
git clone . $tmpdir
mkdir $tmpdir_envfile
cp $tmpdir/binder/environment.yml $tmpdir_envfile/

pushd $tmpdir_envfile
repo2docker --no-run --image-name=nitrateflux_env .
popd
rm -rf $tmpdir $tmpdir_envfile

source deactivate
