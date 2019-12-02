import numpy as np
from shapely.geometry import Polygon

def smoothen(g):
    """
    Insert new points along Polygon boundary.
    This will lead to smoother Polygons if reprojected.

    License
    -------
    GNU-GPLv3, (C) A. R.
    (https://github.com/poplarShift/python-data-science-utils)
    """
    newcoords = []
    for c in g.exterior.coords.xy:
        newc = []
        for c1, c2 in zip(c[:-1], c[1:]):
            newc += list(np.linspace(c1, c2, 50)[:-1])
        newcoords.append(newc)

    newcoords = [(x,y) for x, y in zip(*newcoords)]
    return Polygon(newcoords)
