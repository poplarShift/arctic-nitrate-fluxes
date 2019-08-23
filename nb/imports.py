# -*- coding: utf-8 -*-

import os
import itertools
import datetime as dt
from collections import OrderedDict

from IPython.display import Markdown, display, HTML
from scipy.io import loadmat

# --- DATA HANDLING

import numpy as np
from skimage import exposure
import pandas as pd
import dask.dataframe as dd
import xarray as xr
import gsw

# --- GEO

import geopandas as gpd
import shapely as shp
from shapely.geometry import Point, MultiPoint, LineString, Polygon, box
from shapely.ops import unary_union
from fiona.crs import from_epsg # look up EPSG codes here: http://spatialreference.org
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
from cartopy import crs as ccrs

# --- VIZ

import matplotlib as mpl
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import cmocean
import colorcet

from bokeh.models import (
    PrintfTickFormatter, LogTickFormatter, LogTicker,
    ColorBar, # Title
)
from bokeh.models.mappers import LinearColorMapper, LogColorMapper
from bokeh.io import export_svgs, curdoc, show as bshow

import holoviews as hv
import geoviews as gv
import geoviews.feature as gf
hv.extension('bokeh', 'matplotlib')

import datashader.reductions as dsr
from geoviews import opts
from holoviews import dim, streams
from holoviews.operation.datashader import datashade, rasterize, dynspread
from holoviews.operation.stats import bivariate_kde
from holoviews.core.io import Unpickler, Pickler
from holoviews.plotting.links import DataLink
import hvplot.pandas
import hvplot.xarray
import panel as pn

default_cmap = 'bgy_r'




# --- UTILS

import utils.holoviews as hvu
# from utils.holoviews import flatten
from utils.holoviews.export_multisvg import save_bokeh_svg, save_bokeh_svg_multipanel
from utils.holoviews.switch_backend import (
    translate_options,
    bokeh2mpl,
    add_backend_to_opts,
)
from utils.holoviews.style_link import StyleLink
from utils.holoviews.operation import lowess, sm_lowess, bin_average
from utils.holoviews.faceted_bokeh_legend import faceted_legend, faceted_legend_opts

from utils.mpl import cmap_to_list, circumpolar_axis, squeeze_axis_upward
from utils.xarray import get_unique
from utils.geometry import smoothen
from utils.pandas import df_to_gdf, pandas_df_to_markdown_table
import utils.ctd as ctdut

# --- THEMING , STYLING, ETC.

# bokeh theme

from bokeh.themes import Theme
theme = Theme(json={
'attrs' : {
    'Figure' : {
        'outline_line_color': 'black',
        'outline_line_alpha': 0,
    },
    'Axis' : {
        'axis_line_width': 2,
        'major_tick_line_width': 2,
        'major_tick_in': 0,
        'major_tick_out': 8,
        'minor_tick_out': 0,
        'axis_label_standoff': 12,
        'axis_label_text_color': 'black',
        'axis_label_text_font_size': '15pt',
        'major_label_text_font_size': '13pt',
        'axis_label_text_font_style': 'normal',
    },
    'CategoricalAxis' : {
        'separator_line_width': 0,
    },
    'Ticker': {
        # 'desired_num_ticks': 4,
    },
    'Legend': {
        'label_text_font_size': '13pt'
    },
    'Grid': {
        'grid_line_dash': [6, 4],
        'grid_line_alpha': .9,
    },
    'Title': {
        'text_font_size': '15pt',
    },
    'ColorBar': {
        'major_tick_in': 0,
        'major_tick_out': 6,
        'major_tick_line_width': 1,
        'title_text_align': 'right',
        'label_standoff': 4,
        'title_text_font_style': 'normal',
        # 'major_label_text_font_size': '14pt',
    }
}})
hv.renderer('bokeh').theme = theme
gv.renderer('bokeh').theme = theme

# --- holoviews options

opts_map_bk = [
    opts.HexTiles(
        colorbar=True, projection=ccrs.NorthPolarStereo(),
        tools=['hover'], width=600, height=500, gridsize=20,
        cmap=default_cmap, clabel='', show_legend=False,
        aggregator=np.mean,
    ),
    opts.Polygons(line_color='k', fill_color=None, line_width=3),
    opts.Feature(line_color='k', line_width=1, scale='110m'),
    opts.Shape(line_width=0.8),
    opts.Points(projection=ccrs.NorthPolarStereo(),)
]

opts_timeseries_bk = [
    opts.Scatter(invert_yaxis=True, s=3, alpha=.4, axiswise=True,
                 color='g', show_legend=False,
                 # fontsize={'xlabel':18, 'ylabel':18, 'ticks':16}
                ),
    opts.ErrorBars(color='k', alpha=.3,),
    opts.Curve(color='k'),
]

override = {
    'all': {'show_title': False},
    'Layout': {
        'vspace': .25,
    },
    'Scatter,Curve,Area': {
        'show_frame': True, 'aspect':'auto',
        'show_grid': False,
    },
    'Scatter': {'s': 80},
    'Feature': {'scale': '110m'}
}


add_backend_to_opts(opts_map_bk, 'bokeh')
add_backend_to_opts(opts_timeseries_bk, 'bokeh')

opts_map_mpl = translate_options(opts_map_bk, bokeh2mpl, override=override)
opts_map = opts_map_bk + opts_map_mpl

opts_timeseries_mpl = translate_options(opts_timeseries_bk, bokeh2mpl, override=override)
opts_timeseries = opts_timeseries_bk + opts_timeseries_mpl


# --- custom definitions and data

import warnings
def mplrender(obj, fname=None, hooks=None):
    with warnings.catch_warnings():
        # catch some recent rcparam deprecation warnings
        warnings.simplefilter('ignore')
        hv.extension('matplotlib')
        fig = hv.render(obj)#, backend='matplotlib')
        hv.extension('bokeh', 'matplotlib')

    fig.subplots_adjust(left=0.25, bottom=0.25)

    if hooks is not None:
        for hook in hooks:
            hook(fig)

    if fname is not None:
        fig.savefig(fname+'.pdf')
        fig.savefig(fname+'.png')
    return fig

def mplrender_map(obj, fname=None, hooks=None):
    def hook_adjust_map(fig):
        fig.set_size_inches((9.5, 6))

        ax = fig.axes[0]
        circumpolar_axis(ax)

        ax = fig.axes[1]
        squeeze_axis_upward(ax)

    if hooks is None:
        hooks = [hook_adjust_map]
    else:
        hooks = [hook_adjust_map] + hooks

    fig = mplrender(obj, fname, hooks)
    return fig


# staple map elements
bathy = gpd.read_file('/Users/doppler/database/IBCAO/IBCAO_1min.shp').set_index('contour').geometry
isobath2000 = gv.Shape(bathy.loc[2000], crs=ccrs.PlateCarree())

land = gf.land *gf.coastline

graticules = gv.Feature(
    cfeature.NaturalEarthFeature(
    category='physical',
    name='graticules_30',
    scale='110m'),
    group='Lines')


# since the bokeh color log mapping has a serious error these days, we have to define our own log transformations:

from bokeh.models import FuncTickFormatter, PrintfTickFormatter, FixedTicker
def logcolor(plot, element, ticks):
    try:
        p = plot.handles['color_colorbar']
    except:
        try:
            p = plot.handles['colorbar']
        except:
            p = plot['colorbar']

    p.ticker = FixedTicker(ticks=np.log10(np.array(ticks)))
    # props to http://blog.magnetiq.com/post/497605344/rounding-to-a-certain-significant-figures-in-javascript
    # (originally by Ateş Göral)
    p.formatter = FuncTickFormatter(code="""
    var n = Math.pow(10, tick)
    var sig = 1
    var mult = Math.pow(10, sig - Math.floor(Math.log(n) / Math.LN10) - 1);
    return Math.round(n * mult) / mult;
    """)
    # another option:
    # p.formatter = PrintfTickFormatter(format='1e%+g')
def logcolor_ticks(ticks):
    return lambda plot, element: logcolor(plot, element, ticks)
