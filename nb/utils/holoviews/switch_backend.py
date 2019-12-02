from copy import deepcopy
from collections import OrderedDict
import numpy as np
from holoviews import Options, dim, Cycle

bokeh2mpl_markers = {
    'cross': 'x',
    'square': 's',
    'diamond': 'd',
    'triangle': '<',
    'circle': 'o',
    'asterisk': '*',
}

bokeh2mpl_linestyles = {
    'dotted': ':',
    'dashed': '--',
}

def translate_recursively(x, translator):
    """
    Parameters
    ----------
    x : whatever needs to be translated
    translator: dictionary (such as bokeh2mpl_markers), or function
    """
    if isinstance(x, (str, int, float)) or np.isscalar(x):
        if isinstance(translator, (dict, OrderedDict)):
            return translator.get(x, x)
        elif callable(translator):
            try:
                return translator(x)
            except:
                return x
    elif isinstance(x, Cycle):
        return Cycle([translate_recursively(v, translator)
                      for v in x.values])
    elif isinstance(x, dim):
        xx = deepcopy(x)
        kw = xx.ops[0]['kwargs']
        kw_new = {
            k: {
                kk: translate_recursively(vv, translator)
                for kk, vv in v.items()
            } if isinstance(v, dict)
            else translate_recursively(v, translator)
            for k, v in kw.items()
        }
        xx.ops[0]['kwargs'] = kw_new
        return xx

# each value of this dict has keys for the bokeh option and the corresponding
# mpl option as value. (None means option will be discarded.)
# Tuples have the mpl option name as first entry and the corresponding value as
# second entry
bokeh2mpl = {
    # 'force' is an exception: it has the option as key but the new value of the
    # option in the mpl backend is the corresponding dict value
    'force': {
        'backend': 'matplotlib',
        'hooks': [],
    },
    # apply to all elements
    'all': {
        'height': None,
        'width': None,
        'frame_height': None,
        'frame_width': None,
        'shared_axes': None,
        'shared_datasource': None,
        'tools': None,
        'toolbar': None,
        'legend_position': None,
        'sizing_mode': None,
    },
    'Bars': {
        'line_width': None,
    },
    'Points': {
        'line_color': 'edgecolor',
    },
    'Feature': {
        'fill_color': 'facecolor',
        'line_color': 'edgecolor',
        'line_width': 'linewidth',
    },
    'HexTiles': {
        'cmap': None,
    },
    'Polygons': {
        'fill_color': 'facecolor',
        'line_color': 'edgecolor',
        'line_width': 'linewidth',
    },
    'VLine': {
        'line_color': 'linecolor',
        'line_width': 'linewidth',
    },
    'Labels': {
        'text_align': None,
        'text_color': 'color',
    },
    'Curve': {
        'line_dash': (
            'linestyle',
            lambda x: translate_recursively(x, bokeh2mpl_linestyles)
        ),
    },
    # multiple
    'Scatter,Points,ErrorBars,Shape,Curve': {
        'size': 's',
        'color': 'c',
        'line_color': 'edgecolor',
        'line_width': 'linewidth',
        'line_dash': (
            'linestyle',
            lambda x: translate_recursively(x, bokeh2mpl_linestyles)
        ),
        'fill_color': 'facecolors',
        'marker': (
            'marker', lambda x: translate_recursively(x, bokeh2mpl_markers)
        ),
        'size': (
            's', lambda x: translate_recursively(x, lambda s: 10*s)
        ),
    },
}

def set_new_value(new_value_or_fn, old_value):
    """
    Either replace the old value or transform it using the function.
    """
    if callable(new_value_or_fn):
        return new_value_or_fn(old_value)
    else:
        return new_value_or_fn

def extract_if_key_is_substr(d, key):
    """
    Parameters
    ----------
    d: dict
        where keys can be of the form 'key1,key2,...'
    key: str
        key to match
    """
    return dict(kv
                for k, v in d.items() if key in k.split(',')+['all']
                for kv in v.items()
                )

def parse_translation(lookup, k, v):
    """
    Given a lookup dictionary, translate a key-value pair.

    Parameters
    ----------
    lookup : dict
        {k: k_new} or {k: (k_new, v_new)} or {k: (k_new, lambda x: v_new)} or ...
    k : str
    v : dict value (if tuple, has to be of form (str, _))
    """
    translate_to = lookup[k]
    if translate_to is None:
        # eliminate kwarg
        k_new, v_new = None, None
    elif isinstance(translate_to, str):
        # translate kwarg, keep value
        k_new, v_new = translate_to, v
    elif (
        isinstance(translate_to, tuple)
        and len(translate_to)==2
        and isinstance(translate_to[0], str)
        ):
        # translate kwarg, set new value
        k_new, v_new = translate_to[0], set_new_value(translate_to[1], v)
    else:
        # keep old key, translate only value
        k_new, v_new = k, set_new_value(translate_to, v)
    return k_new, v_new

def update_element(name, kwargs, lookup, force={}):
    """
    For each element 'name', given kwargs, translate its key-value pairs
    using lookup and force them using dict `force`, as applicable.

    Parameters
    ----------
    name : str (e.g. 'Scatter')
    kwargs : dict
    lookup : dict
    force : dict, optional
        directly set entries as key-value pairs
    """
    updates = {}
    for k, v in kwargs.items():
        if k in lookup:
            # needs translation
            k_new, v_new = parse_translation(lookup, k, v)
            if k_new is not None:
                updates[k_new] = v_new
        else:
            updates[k] = v
    for k, v in force.items():
        updates[k] = v
        # k_new, v_new = parse_translation(force, k, v)
        # if k_new is not None:
        #     updates[k_new] = v_new
    return updates

def translate_options(options, dictionaries=None, override={}):
    """
    Translate a list of holoviews options using a given dict of dicts.

    Parameters
    ----------
    options : list
        of `Options` objects
    dictionaries : dict of dicts
        Translations to be applied as needed
    override : dict of dicts
        overrides everything else
    """
    if dictionaries is None:
        dictionaries = bokeh2mpl
    # presets forced on some options across all Element types:
    # 1 -- if the default translation dictionary (such as bokeh2mpl) defines
    #      options that need to be forced
    force1 = dictionaries.get('force', {})
    # 2 -- if the case-specific override dict contains a section pertaining
    #      to all elements
    force2 = override.get('all', {})

    options_new = []
    for o in options:
        name_full = o.key
        name = name_full.split('.')[0]
        # lookup dictionary; look in here for keys to check whether
        # translation for a given kwarg is available
        lookup = {
            **dictionaries['all'],
            **extract_if_key_is_substr(dictionaries, name),
            **extract_if_key_is_substr(dictionaries, name_full)
        }
        # 3 -- complete element-specific override variables
        force3 = {
            **extract_if_key_is_substr(override, name),
            **extract_if_key_is_substr(override, name_full),
        }

        kwargs_new = update_element(
            name_full,
            o.kwargs,
            lookup,
            force={**force1, **force2, **force3}
        )
        o_new = Options(name_full, **kwargs_new)
        options_new.append(o_new)
    return options_new


def add_backend_to_opts(opts, backend):
    for k, o in enumerate(opts):
        opts[k] = Options(o.key, **{**o.kwargs, **{'backend': backend}})
