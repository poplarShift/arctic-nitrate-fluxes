import numpy as np
# import xarray as xr
import pandas as pd

def get_unique(x, axis=0):
    """
    Return unique non-nan value along specified xarray axis.
    Use this to squeeze out dimensions with length>1.

    Raises
    ------
    ValueError: if there are more than one non-nan values

    Usage
    -----
    ds.reduce(get_unique, dim=some_dim)

    License
    -------
    GNU-GPLv3, (C) A. Randelhoff
    (https://github.com/poplarShift/python-data-science-utils)
    """
    is_dt = np.issubdtype(x.dtype, np.datetime64)
    x_ = np.moveaxis(x, source=axis, destination=-1)
    iteridx = x_.shape[:-1]
    u = np.zeros(iteridx, dtype=x.dtype) if is_dt else np.nan*np.zeros(iteridx)
    if not isinstance(u, np.ndarray):
        # if iteridx was empty tuple
        u = np.array(u)

    for i in np.ndindex(iteridx):
        u_1dim = np.unique(x_[i])
        nan_nat = pd.isnull(u_1dim)
        u_non_null = u_1dim[~nan_nat]
        if len(u_non_null)==1:
            u[i] = u_non_null[0]
        elif pd.isnull(u_1dim[0]):
            if is_dt:
                u[i] = np.datetime64('NaT')
            else:
                u[i] = np.nan
        else:
            raise ValueError('Non-unique slices encountered!')
    return u
