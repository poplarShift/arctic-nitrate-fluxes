import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import numpy as np
from matplotlib.transforms import Bbox
from matplotlib.path import Path

def cmap_to_list(cm, N=None, out='rgba'):
    """
    Turns a MPL colour map into a list of colors.

    Parameters
    ----------
        N: number of colors to sample (equal steps across entire cmap)
        out: 'rgba' or 'hex'

    License
    -------
    GNU-GPLv3, (C) A. R.
    (https://github.com/poplarShift/python-data-science-utils)
    """
    if N is None:
        N = cm.N
    if out == 'rgba':
        cm2clr = lambda i: cm(i)
    elif out == 'hex':
        cm2clr = lambda i: mpl.colors.to_hex(cm(i))

    return [cm2clr(i) for i in np.linspace(0, 1, N)]

def set_cartopy_grid(ax, lons, lats, label_opts=None, grid_opts=None, **kwargs):
    """
    Add graticules to cartopy GeoAxes and label them.

    NB: This grid assumes that the grid has latitude and longitudes
    arranged somewhat rectangularly. For circumpolar maps, see circumpolar_axis
    further below.

    License
    -------
    GNU-GPLv3, (C) A. R.
    (https://github.com/poplarShift/python-data-science-utils)
    """
    if label_opts is None:
        label_opts = {}
    if grid_opts is None:
        grid_opts = {}
    label_offset = kwargs.pop('label_offset', 1e-4)

    proj = ax.projection
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=False,
                      linewidth=1, color='gray', alpha=0.5, linestyle='--',
                      **grid_opts)

    gl.xlocator = mticker.FixedLocator(lons)
    gl.ylocator = mticker.FixedLocator(lats)

    # W, E, S, N
    map_extent = ax.get_extent()

    # LATITUDE LABELS
    x0,_ = ax.get_xlim()
    some_lons = np.arange(gl.xlocator.locs.min(), gl.xlocator.locs.max(), 1)
    for lat in gl.ylocator.locs:
        # interpolate latitude circle to map boundary
        xyz_projected = proj.transform_points(
            ccrs.PlateCarree(), some_lons, lat*np.ones_like(some_lons)
        )
        x = xyz_projected[:, 0]
        y = xyz_projected[:, 1]
        y0 = np.interp(x0, x ,y)
        if map_extent[2]<y0<map_extent[3]:
            ax.text(
                x0-label_offset, y0, LATITUDE_FORMATTER(lat),
                horizontalalignment = 'right',
                verticalalignment='center',
                **label_opts
            )

    # LONGITUDE LABELS / COMPLETELY ANALOGOUS TO ABOVE
    y0,_ = ax.get_ylim()
    some_lats = np.arange(gl.ylocator.locs.min(), gl.ylocator.locs.max(), 1)
    for lon in gl.xlocator.locs:
        xyz_projected = proj.transform_points(
            ccrs.PlateCarree(), lon*np.ones_like(some_lats), some_lats
        )
        x = xyz_projected[:, 0]
        y = xyz_projected[:, 1]

        x0 = np.interp(y0, y, x)
        if map_extent[0]<x0<map_extent[1]:
            ax.text(
                x0, y0-label_offset, LONGITUDE_FORMATTER(lon),
                horizontalalignment = 'center',
                verticalalignment='top',
                **label_opts
            )


def circumpolar_axis(ax):
    """
    Draw a circumpolar grid of longitudes around a map at latitude 62 degrees N

    License
    -------
    GNU-GPLv3, (C) A. R.
    (https://github.com/poplarShift/python-data-science-utils)
    """
    circle = Path.circle(radius=3e6)
    proj = ax.projection
    ax.set_boundary(circle, transform=proj)
    # collections are only clipped when added after this point, so re-add them
    for c in ax.collections:
        c.remove()
        ax.add_collection(c)

    lat = 62
    def rotation(lon):
        if abs(lon)<=90:
            return lon
        else:
            return lon-180

    for lon in np.arange(-180, 180, 60):
        lon_text = '{:3d}$^\circ${}'.format(
                        abs(lon),
                        {True: 'E', False: 'W'}[lon>=0]
                    )
        textopts = dict(va='center', ha='center', rotation=rotation(lon))
        ax.text(*proj.transform_point(lon, lat, ccrs.PlateCarree()), lon_text, **textopts)

def squeeze_axis_upward(ax, newy=0.5):
    x, y, w, h = ax.get_position().bounds
    ax.set_position((x, newy, w, y+h-newy))
