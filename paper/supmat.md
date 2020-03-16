---
title: Supplementary Material: Pan-Arctic Ocean primary production constrained by turbulent nitrate fluxes
tblPrefix: Table
geometry: margin=1in
numbersections: true
---
[comment]: # (This document is just typeset for Frontiers because they would not want it in the main article; it is not part of the standard compilation pipeline and is still included in the interactive and static article file paper*.html. Compiled using `$ pandoc -V geometry:margin=1in --bibliography bibliographyfull.bib --pdf-engine=xelatex --filter pandoc-crossref --filter pandoc-citeproc --csl frontiers.csl --mathjax --number-sections -o supmat.pdf supmat.md`)


$$\textrm{\Large Appendix: }$$
$$\textrm{\Large Pan-Arctic Ocean primary production }$$
$$\textrm{\Large constrained by turbulent nitrate fluxes }$$


**Achim Randelhoff**$^1$$^2$\*, **Johnna Holding**$^3$$^4$, **Markus Janout**$^5$, **Mikael Kristian Sejr**$^3$$^4$, **Marcel Babin$^1$$^2$**, **Jean-Éric Tremblay**$^1$$^2$, **Matthew B. Alkire**$^6$$^7$

$^1$ Takuvik Joint International Laboratory, Université Laval (QC, Canada) and CNRS (France)

$^2$ Département de biologie and Québec-Océan, Université Laval (QC, Canada)

$^3$ Arctic Research Centre, Aarhus University, Ny Munkegade 114, bldg. 1540, 8000 Aarhus C, Denmark

$^4$ Department of Bioscience, Aarhus University, Vejlsøvej 25, 8600, Silkeborg, Denmark

$^5$ Alfred-Wegener-Institute Helmholtz Center for Polar and Marine Research, Am Handelshafen 12, D-27570 Bremerhaven, Germany

$^6$ Applied Physics Laboratory, University of Washington, Seattle, WA USA

$^7$ Now at: School of Oceanography, University of Washington, Seattle, WA USA

\* **Correspondance**:

Achim Randelhoff, achim.randelhoff@takuvik.ulaval.ca

# Introduction

The complete supplemental material, accessible at [https://github.com/poplarShift/arctic-nitrate-fluxes](https://github.com/poplarShift/arctic-nitrate-fluxes) [@randelhoff2020software], contains:

- The python code necessary to reproduce all analyses and figures, licensed under GNU GPL3.
- The data, as plotted in all figures, in machine-readable formats.
- An interactive version of the article and this supplementary material where figures can be zoomed, panned, and selectively highlighted (as appropriate) leveraging the [Bokeh library](http://bokeh.pydata.org) [@bokehdevelopmentteam2018bokeh].

# The marine nitrogen cycle

Discussions of ocean surface nitrogen budgets center around the marine nitrogen cycle. @Fig:ncycle shows a simplified version adapted to Arctic conditions. The main component is the cycling between inorganic nitrate and particulate organic nitrogen (PON). Upward transport of NO$_3^-$ compensates nitrate uptake by algae into PON [@dugdale1967uptake] and subsequent sinking of this organic matter. The loop is closed by remineralization into nitrate at depth. When nitrogen is scarce in the surface layer, there is also intense recycling of nitrogen that has already been assimilated into organic matter, which is called regenerated production.

Additional complexity arises from a number of sources, sinks, and recycling processes not accounted for in this simplistic view. One of the conclusions of the present study is that we do not need to invoke those processes to understand Arctic surface layer budgets on a Pan-Arctic scale. Riverine inputs of nitrate are thought to be sufficiently small to be neglected at larger-than-regional scales [see e.g. @tank2012processing]. Some of the produced PON is also harvested e.g. by higher trophic levels or fisheries [e.g. @valiela2015marine], although the latter process is likely only regionally important, e.g. in the Barents Sea. Other factors may be important depending on the regional scope. Advection, upwelling, and mesoscale mixing have already been discussed in the main text. Nitrification, denitrification, and nitrogen fixation are in general not well constrained in the Arctic Ocean [@tremblay2008vertical; @blais2012nitrogen; @sipler2017preliminary]. @randelhoff2015seasonal, for instance, argued that winter vertical turbulent nitrate fluxes in areas with deep mixing are likely much larger than nitrification, but did so based on sparse data. A complete assessment of all these factors is beyond the scope of this paper.

# The vertical layering of Arctic Ocean nitrate

Fluxes are easiest to measure across strong gradients. A given vertical profile of nitrate concentrations in the Arctic Ocean can schematically be vertically divided by two nitraclines ([@Fig:ncycle]A): First, a seasonal one, which marks the transition from surface waters, modulated by seasonal freshwater from ice melt or terrestrial runoff and algal growth, to the remnant winter mixed layer. Second, and mostly present in the deep basins of the Arctic Ocean, one that we dub "perennial" as it is not eroded and re-established on an annual basis.

The seasonal nitracline may be completely mixed during winter ([@Fig:ncycle]B), rendering fluxes hard to estimate using the "diffusivity times gradient" formula. Across the perennial nitracline, fluxes can be estimated year-round stipulating the seasonal variations in nitracline dissipation are minor, a method exploited by @randelhoff2016regional to estimate Pan-Arctic patterns of upward nitrate supply in the deep basin. In practice, the two nitraclines are often not clearly delineated. The distinctive characteristics of the two nitraclines are most easily seen in the Eurasian Basin, where deep winter mixed layers are clearly separated from underlying Atlantic Waters. In the Canadian Basin, strong stratification prevents winter mixing from penetrating deep into the nitracline [@peralta-ferriz2015seasonal], leading to relatively small seasonal excursions in surface nutrient concentrations and a less distinct winter remnant mixed layer ([@Fig:ncycle]C).

Consequently, we classified the seasonality of all vertical nitrate flux estimates discussed in this paper in terms of whether the water column mixes deeply ("overturns") in winter or not (in which case stratification is dubbed "perennial"). We used the published literature for each location as well as the data set corresponding to the flux estimate, if available. Importantly, our classification is generally well-founded but occasionally ad-hoc and tentative due to sparse data. An illustrative example are three summertime flux estimates north of the Barents sea polar front [@sundfjord2007observations; @wiedmann2017upward]. For instance, @loeng1991features indicates a weak but persistent salinity stratification in the Arctic water mass throughout winter, but the few vertical nitrate profiles available in our compiled data set indicate a seasonal cycle of surface nitrate in line with what is seen south of the Polar Front. These three fluxes were hence classified as being in a location where the water column overturns in winter because we focused on the vertical structure of nitrate profiles. Either way, because all three fluxes were based on a small sample size, not too much weight was given to them in the overall analysis.


# Measuring vertical nitrate fluxes

Barring regionally important processes such as upwelling and eddy pumping [@carmack2003wind; @kampf2016upwelling; @randelhoff2018short], the most prevalent form of the upward transport of nitrate in the ocean is turbulent diffusion [@lewis1986vertical]. Such diffusion mixes the spent surface waters with deeper, more nutrient-rich waters, thereby replenishing their nitrate reservoir. A vertical turbulent nitrate flux is, by definition, the product of a so-called "diapycnal eddy diffusivity" with the vertical gradient of nitrate. This is completely analogous to any other tracer such as temperature or salinity. The interested reader is referred to the vast literature on turbulent flows.

To estimate both those quantities, one has to measure the turbulence and a vertical profile of nitrate concentrations at the same time and location. Determining nitrate concentrations is comparatively uncomplicated because only the non-turbulent background is needed; one can use either bottle samples or, preferably, optical nitrate sensors to achieve a better vertical resolution [@alkire2010sensorbased; @randelhoff2016vertical]. Both of these options are easily integrated into standard sampling with a CTD rosette. While care should be taken to calibrate the absolute concentrations of optical sensors against water samples, such biases are usually depth-independent and hence do not matter for the calculation of the gradients [see Appendix of @randelhoff2016vertical]. Measuring turbulence is more challenging because it requires either measurements with sophisticated instruments, requiring dedicated ship time and personnel, or parameterizations that add layers of uncertainty [e.g. @garrett1975space; @guthrie2013revisiting].

## Measuring turbulence

The most direct way of determining a nitrate flux is measuring the so-called "dissipation of turbulent kinetic energy" ($\epsilon$) traditionally using free-falling microstructure profilers [@lueck2002oceanic]. $\epsilon$ can also be estimated from finescale current shear (i.e. current profiles) or strain visible in CTD profiles [@guthrie2013revisiting]. Once $\epsilon$ is determined, its accuracy usually cited as being within a factor of two [@moum1995comparison], the vertical turbulent diffusivity can be calculated, following @osborn1980estimates, as

$$K_\rho = \Gamma\frac{\epsilon}{N^2}$$ {#eq:osborn}

where $N^2$ is the Brunt-Väisälä buoyancy frequency and $\Gamma\approx 0.2$ is the mixing coefficient that reflects how much of $\epsilon$ is available for adiabatic mixing. @Eq:osborn has a number of known issues, a major one being that $\Gamma$ is not constant. A variety of different parameterizations have been proposed [e.g. @shih2005parameterization; @bouffard2013diapycnal], with no clear alternative emerging. @Eq:osborn is hence the de facto standard [@gregg2018mixing], and in fact all turbulence-based estimates of the vertical nitrate flux compiled for this paper are based on it. Most often, $\Gamma=0.2$ is used, but e.g. @sundfjord2007observations used $\Gamma=0.12$ following recommendations in the literature consistent with their dataset (see references therein).

## Using the inorganic nitrate drawdown as an indicator of nitrate flux

Another method to determine vertical nitrate fluxes, less direct, uses a set of nitrate profiles through fall and winter [@randelhoff2015seasonal]. It has been employed to calculate two of the fluxes presented in this study. Vertically integrating the successive differences between them, one essentially reverses the calculation of net community production by the nitrate drawdown between winter and summer [@codispoti2013synthesis]. @randelhoff2015seasonal provided a brief overview over potentially interfering processes such as nitrogen fixation [@blais2012nitrogen] and concluded they were likely not significantly disturbing the annual budgets, but it has to be acknowledged that data is sparse. While this method may be robust in the pelagic, one can doubt its effectiveness in waters where nitrogen cycling is heavily affected by other processes, such as benthic processes in shallow waters, or coastal effects.


# New estimates of nitrate fluxes and new production in Young Sound, NE Greenland

## Methods

Sampling in the Young Sound/Tyrolerfjord system was conducted during three weeks in August 2015 from the Daneborg research station as part of the Danish MarineBasis program in Zackenberg ([@Fig:FN-NEW_YOUNGSOUND]A).

Water column nutrient samples were taken at 5 stations using a manually operated Niskin bottle from depths of 1, 5, 10, 20, 30, 40, 50, and 100 m. They were filtered with Whatman GF/F filters before being stored in previously acid-washed 30 mL high-density polyethylene (HDPE) plastic bottles and frozen until analysis (-18 °C). Nitrite (NO2) and nitrate (NO$_3^-$) concentrations in each sample were measured on a Smartchem200 (AMS Alliance) autoanalyzer.

An MSS-90L (Sea and Sun Technology, Germany) free-falling microstructure profiler was deployed at a total of 37 stations, many of them repeat stations, to measure vertical profiles of the dissipation of turbulent kinetic energy. At the same stations, we deployed a SUNA (Satlantic) nitrate spectrophotometer to collect co-located vertical profiles of nitrate concentration. SUNA profiles were post-processed following [@randelhoff2016vertical] and calibrated using a constant bias determined from comparison with the nutrient water samples.

New and regenerated production were investigated at a subset of five stations. They were measured in two parallel incubations, labelled with ca. 10% ambient concentration of  $^{15}$NO$_3^-$ and $^{15}$NH$_4^+$ respectively. Water samples were incubated in triplicate 500 ml polycarbonate bottles in situ.  Additionally ca. 10% ambient concentration of $^{13}$C-bicarbonate was added to both sets of incubations to follow the incorporation of inorganic carbon into biomass. Samples were taken for  NO$_2^-$+NO$_3^-$ , $^{15}$NO$_3^-$ and $^{15}$NH$_4^+$  before and after addition of tracers by  filtering through a syringe filter (Whatman GF/C) into 10 ml polystyrene vials which were frozen (-18 °C) until analysis. After the incubation the particulate matter from each incubation vessel was filtered onto pre-combusted GF/F filters and later the $^{15}$N and $^{13}$C content of the particles on the filters was determined by mass spectrometry. Before filtration a third set of samples for NO$_2^-$+NO$_3^-$, $^{15}$NO$_3^-$ and $^{15}$NH$_4^+$ were taken. NO$_2^-$+NO$_3^-$ was determined photometrically following @schnetger2014determination. $^{15}$NH$_4^+$ was determined based on @risgaard1995combined. $^{15}$NO$_3^-$ was determined as in @kalvelage2011oxygen. New and regenerated production were calculated as the ratio of nitrate or ammonium to total N-uptake in each incubation respectively multiplied by the total C-uptake in each incubation.

In total, we collected 43 profiles of co-located SBE25+SUNA profiles, 103 MSS casts, 40 nutrient bottle samples and 20x3 triplicates of new and regenerated production incubations.

## Results

A freshwater layer was present throughout the fjord, but most prominent in the innermost parts ([@Fig:FN-NEW_YOUNGSOUND]B-D). Nitrate was depleted throughout the upper 40 m, below which concentrations steeply rose to about 4 µM. The fjord was remarkably quiescient in terms of turbulent dissipation rates, but mixing was significantly elevated over the sills. Vertical nitrate fluxes, computed for each station of co-located MSS and SUNA measurements, ranged from 0.012 to 13.26 mmol N m$^{-2}$ d$^{-1}$, with some of the values in the fjord interior being the lowest observed across this entire study. Median upward fluxes were 0.036 and 0.33 mmol N m$^{-2}$ d$^{-1}$ in the fjord interior and over the sills, respectively. Incubations, although only available at two depths (5 and 20 m), indicated new production rates on the order of 0.1 to 1 mmol N m$^{-2}$ d$^{-1}$ ([@Fig:FN-NEW_YOUNGSOUND]E).

# Nitrate flux estimate in the Laptev Sea

## Data description

Microstructure and nutrient measurements from the Laptev Sea were collected under the framework of the German-Russian “Laptev Sea System”-partnership in winter 2008 and the summers of 2011, 2014, and 2018 ([@Fig:FN-NEW_LAPTEV]B). The 2008 profile was averaged from measurements collected during the helicopter-supported “Transdrift 13” winter expedition (6 April to 10 May 2008) to the southeastern Laptev shelf. The summer nitrate profile was averaged from profiles collected during the “Transdrift 19” expedition on board the RV Jakov Smirnitsky in September 2011 [@bauch2018physical].

In 2014 microstructure turbulence profiles were collected on 19 September 2014 during the Transdrift 22-expedition aboard the RV Viktor Buinitsky (see Janout et al., to be submitted to this issue). The dissipation rates of turbulent kinetic energy ($\epsilon$) were derived from shear variance measured with a freely falling MSS-90L microstructure profiler manufactured by Sea and Sun Technology (SST, Germany). Vertical profiles of epsilon were calculated from the isotropic formula and spectral analysis of 1-s segments and subsequently averaged into 1-m bins. Turbulent vertical fluxes are based on a diapycnal eddy diffusivity with a constant mixing efficiency taken to be 0.2 [@osborn1980estimates]. For statistical robustness, the 2014 MSS profile shown in this paper was averaged from a series of five casts.

In 2018 a joint German-US-Russian expedition to the Eurasian Arctic was carried out aboard the RV Akademik Tryoshnikov from 18 August to 30 September 2018. The expedition combined the German-Russian CATS (Changing Arctic Transpolar System) and the US-Russian NABOS (Nansen Amundsen Basin Observing System) programs. The dissipation profile was again generated with a MSS-90L, while the nitrate profile was recorded with a Deep SUNA V2 nitrate profiler (Seabird Scientific) attached to the shipboard CTD/rosette.
These data files were then processed using a program (ISUSDataProcessor) developed by Ken Johnson (MBARI) that corrects the spectral data for temperature effects on the bromide absorption and applies a linear baseline correction to account for absorption by colored dissolved organic matter [@sakamoto2009improved]. SUNA nitrate concentrations were then compared with nitrate concentrations measured from discrete seawater samples collected at various depths above 20 and below 300 m depth where concentrations were sufficiently constant with depth. The full description of the methods is distributed with the data [@alkire2019ocean].

## Nitrate fluxes

Two representative profiles were selected to compute nitrate fluxes ([@Fig:FN-NEW_LAPTEV]A): Cast 59 and a co-located MSS profile, both sampled in 2018, and the 2014 MSS profiles and cast 62, also co-located but from separate years. For both profiles, we visually determined the nitracline, averaged $\epsilon$ over that interval, and computed the average nitrate and density gradients by a linear regression. The resulting nitrate fluxes were 0.014 and 0.017 mmol N m$^{-2}$ d$^{-1}$, and hence we entered the average value of 0.015 mmol N m$^{-2}$ d$^{-1}$ for the Laptev Sea into the nitrate fluxes compilation.

Even though we have a winter and a summer vertical profile of nitrate concentrations, we cannot calculate a winter flux using the integrated drawdown [@codispoti2013synthesis; @randelhoff2015seasonal] because comparison of the winter and summer profiles does not indicate any reliable vertical structure in the drawdown. This may indicate that winter fluxes might be too small to make a noticeable difference between the summer and winter profiles. More importantly, in such a shallow shelf sea, other factors (such as benthic nitrogen cycling or riverine freshwater) may also play a role as detailed above.

# Nitrate flux estimate in Baffin Bay

Three biogeochemical Argo floats, part of the NAOS project, overwintered in Baffin Bay from July 2017 to July 2018, described in detail by Randelhoff et al. (2020, in prep.).

Nitrate concentration was observed by the Satlantic Submersible Ultraviolet Nitrate Analyzer (SUNA). Each sensor's offset, taken to be constant and depth-independent [@randelhoff2016vertical], was corrected based on nitrate concentration profiles sampled during deployment of the floats. Mixed layer depth was defined as the shallowest depth where density rose more than 0.1 kg m$^{-3}$ above the surface density.

Integrating the nitrate deficit $\Delta$ [NO$_3^-$]$\equiv$[NO$_3^-$] (60 m) - [NO$_3^-$] (z) over the upper 60 meters for each station shows that over the course of four months (from November to March), a deficit of 200 mmol N m$^{-2}$ was replenished, approximately equivalent to an upward nitrate flux of 1.66 mmol N m$^{-2}$ d$^{-1}$ ([@Fig:FN-NEW_BAFFIN]). Although each float was drifting during the course of the winter, which may have introduced advective changes, the floats were well dispersed across Baffin Bay and should give a representative picture of winter mixed layer evolution. Details are deferred to the aforementioned manuscript (Randelhoff et al., in prep.). The usual caveats about neglecting mixed-layer regeneration and consumption of nutrients apply, and so this calculation makes the same kind of assumptions as have been detailed by @randelhoff2015seasonal.

# Figures

![A simplified marine nitrogen cycle and idealized Arctic hydrography. (A) General schematic of a vertical profile of nitrate concentration, along with the respective portion of the nitrogen cycle that takes place in each layer. In this idealized case, there is a clear separation between the seasonal variations in nitrate concentrations in the surface layer which give rise to the seasonal nitracline, and the underlying perennial nitracline. (B) In areas with deep overturning into the waters of maximum nitrate concentration, the deep nitracline ceases to be meaningful. Instead, nitrate fluxes tap into high-nutrient water every winter. (C) Highly stratified areas do not see large seasonal excursions in surface layer nitrate concentrations or mixing depths.](../fig/ncycle.png){#fig:ncycle height=80%}

![Young Sound data. (A) Bathymetry and coast data courtesy T. Vang and J. Bendtsen (@rysgaard2003physical; not included in the supplemental material). Transect starting in the inner end of the fjord, going over two sills and out into the Greenland Sea, demonstrating (B) low salinity due to ice sheet runoff, (C) nitrate depletion in the upper 30-40 meters, and (D) a quiescent fjord interior with vigorous mixing over the two sills. (E) Upward nitrate fluxes observed in Young Sound (shaded areas represent kernel density estimates) and observed values of new production, integrated over 0-20 meters (black bars). Note that new production estimates are based on only two measurement depths; see methods.](../nb_fig/FIGURE_FN-NEW_YOUNGSOUND.png){#fig:FN-NEW_YOUNGSOUND height=70%}

![Laptev Sea data. (A) Vertical profiles of salinity, nitrate concentration and dissipation of turbulent kinetic energy ($\epsilon$) in the Laptev Sea. (B) Measurement locations in the Laptev Sea.](../nb_fig/FIGURE_FN-NEW_LAPTEV.png){#fig:FN-NEW_LAPTEV}

![Seasonal cycle of nitrate concentrations in Baffin Bay alongside mixed layer depth (A) and the 0-60 m vertically integrated nitrate deficit $\Delta$ [NO$_3^-$]=[NO$_3^-$] (60 m) - [NO$_3^-$] (z) (B).](../nb_fig/FIGURE_FN-NEW_BAFFIN.png){#fig:FN-NEW_BAFFIN}

\pagebreak
\pagebreak
\pagebreak

# References
