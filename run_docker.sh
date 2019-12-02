#!/bin/bash

docker run -it -p 8888:8888 -v $HOME/papers/nitrateflux:/home/doppler nitrateflux_env /srv/conda/envs/notebook/bin/jupyter-lab --ip=0.0.0.0 --port=8888
