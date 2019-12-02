#!/bin/bash
doc="# environment_versions.yml file that contains exact version numbers of what is currently installed. We take the pip installs from the original environment file, though, as conda env export does apparently not keep track of the specific source of pip wheel installs. That being said, this is only to keep track of what is installed locally. Due to differences in software availability across operating systems, we will have to resort to building Docker images from the manually built environment.yml file to ensure reproducibility."

echo $doc > binder/environment_versions.yml
conda env export --no-builds | sed '/- pip:/,$d' >> binder/environment_versions.yml
cat binder/environment.yml | sed -n '/- pip:/,$p' | grep -v '^#' >> binder/environment_versions.yml
