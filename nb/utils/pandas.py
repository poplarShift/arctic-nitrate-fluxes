import numpy as np
import pandas as pd
# import functools
from shapely.geometry import Point
import geopandas as gpd
from fiona.crs import from_epsg

def df_to_gdf(df, lon='lon', lat='lat'):
    """
    Turn pandas dataframe with latitude, longitude columns into GeoDataFrame with according Point geometry.

    Parameters
    ----------
    df : pandas dataframe
    lon, lat : names of lon, lat columns

    Returns
    -------
    geopandas geodataframe

    License
    -------
    GNU-GPLv3, (C) A. R.
    (https://github.com/poplarShift/python-data-science-utils)
    """
    df = gpd.GeoDataFrame(df).copy()
    df['geometry'] = [Point(x, y) for x, y in zip(df[lon], df[lat])]
    df.crs = from_epsg(4326)
    return df

def pandas_df_to_markdown_table(df):
    """
    Modeled on https://stackoverflow.com/a/33869154

    License
    -------
    GNU-GPLv3, (C) A. R.
    (https://github.com/poplarShift/python-data-science-utils)
    """
    fmt = ['---' for i in range(len(df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=df.columns)
    df_formatted = pd.concat([df_fmt, df])
    return df_formatted.to_csv(sep="|", index=False)
