#!/bin/bash

pushd nb
for file in `ls [A,B,C]*.ipynb`
do
  fname=`echo $file | cut -d'.' -f 1`
  # # run notebook
  # jupyter nbconvert --to notebook --execute --output=$fname $fname
  # clear outputs
  jupyter nbconvert --ClearOutputPreprocessor.enabled=True --to notebook --output=$fname $fname
  # render to html
  jupyter nbconvert --to html --output=../nb_html/$fname $fname
done
popd
