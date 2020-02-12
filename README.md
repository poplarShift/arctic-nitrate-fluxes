[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/poplarShift/arctic-nitrate-fluxes/master)

# Welcome!

This repository contains code, figures, data, and other supplemental material for the study "Pan-Arctic Ocean primary production constrained by turbulent nitrate fluxes". Our findings are written down in [this interactive html document](paper/paper_interactive.html).

# Contents

The main effort is concentrated in the following notebooks:
1. Database of hydrography and seawater nitrate concentrations:
  - [Collecting and merging](nb/A1_compile_nitrate.ipynb)
  - [Analysis](nb/A2_analyze_nitrate.ipynb)
2. Compilation of nitrate fluxes
  - [New nitrate flux estimates/calculations not previously published](nb/B0_new_estimates.ipynb)
  - [Compiling nitrate fluxes](nb/B1_compile_fluxes.ipynb)
  - [Analyzing that compilation](nb/B2_analyze_fluxes.ipynb)
3. [Comparison of nitrate stocks and fluxes with primary production](nb/C_primary_production.ipynb)

Figures are located in [nb_fig](nb_fig). In addition, there are two **interactive visualizations** in particular that allow for exploration of the rather vast nitrate database.

One, to explore seasonal cycles of nitrate concentrations, works as a [standalone html file](nb_fig/FIGURE_NO3-COMP_chart_seasonal_cycle.html). You can view it on its own, or as part of the [interactive article file](paper/paper_interactive.html) by downloading the html file and opening it in your browser.

The second one is more data-intensive and needs a live python server. It can be launched using the command line:
> `cd nb && panel serve --show A3_app_explore_nitrate.ipynb`

provided you have all packages installed (see below) and you've run notebook `nb/A1_compile_nitrate.ipynb`.

# Usage

There are many ways to explore this study!

- If you would just like to take a look around, the easiest way is probably to [follow this link](https://mybinder.org/v2/gh/poplarShift/arctic-nitrate-fluxes/master) or click on the "Binder" badge in the top of this document. This will launch an interactive environment in the cloud where you can run, modify, and re-run all the code.

- If you would like a local copy, you can create one by cloning this repository using:
> `git clone https://github.com/poplarShift/arctic-nitrate-fluxes.git .`

Then you can [create a conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) on your machine containing all necessary dependencies using
> `$ conda env create -f binder/environment.yml`

- If there is interest, I can also provide a pre-compiled [Docker](https://www.docker.com) image, which gives access to the entire computing environment with all the dependencies.
