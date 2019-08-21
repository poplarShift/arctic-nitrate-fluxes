Welcome!

This repository contains code, figures, data, and other supplemental material for XXX.

The main effort is concentrated in the following notebooks:
1. Database of hydrography and seawater nitrate concentrations:
  - [Collecting and merging](nb/A1_compile_nitrate.ipynb)
  - [Analysis](nb/A2_analyze_nitrate.ipynb)
2. Compilation of nitrate fluxes
  - [New nitrate flux estimates/calculations not previously published](nb/B0_new_estimates.ipynb)
  - [Compiling nitrate fluxes](nb/B1_compile_fluxes.ipynb)
  - [Analyzing that compilation](nb/B2_analyze_fluxes.ipynb)
3. [Comparison of nitrate stocks and fluxes with primary production](nb/C_primary_production.ipynb)

In addition, there are two interactive visualizations in particular that allow for exploration of the rather vast nitrate database.

One, to explore seasonal cycles of nitrate concentrations, works as a standalone html file:

![](nb_fig/FIGURE_NO3-COMP_chart_seasonal_cycle.html)

The second one is more data-intensive and needs a live python server. It can be launched using the command line:
> `cd nb && panel serve --show A3_app_explore_nitrate.ipynb`
provided you have all packages installed (see the `environment.yml` file).
