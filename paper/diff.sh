#!/bin/bash

export articlefile='paper'

tmpdir=_tmp_manuscript_diff

# set only if not already defined
: "${bib:=bibliographyfull.bib}"

git clone -b v0.1.1 .. $tmpdir

# parse papers both in old and new versions

# old
cd $tmpdir/paper
./parse_articlefile.sh
old=$tmpdir/paper/${articlefile}_static.md
cd ../..
# new
./parse_articlefile.sh
new=${articlefile}_static.md

tracked=${articlefile}_trackchanges

pandiff $old $new -o $tracked.html --bibliography $bib --filter pandoc-crossref  --filter pandoc-citeproc

# append stylesheet
echo '
<style>
del {
  color: #b31d28;
  background-color: #ffeef0;
  text-decoration: line-through;
}
ins {
  color: #22863a;
  background-color: #f0fff4;
  text-decoration: underline;
}
img {
  max-width: 100%;
  min-width: 60%;
}
</style>
' >> $tracked.html

rm -rf $tmpdir
