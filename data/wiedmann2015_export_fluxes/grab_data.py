# USAGE: call grab(), mark points, then exit and call export(ref), where ref is a string that will define the filename

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import pandas as pd

global coords
coords=[]
def grab():
    img = imread('Wiedmann-Figure2.png')
    fig, ax = plt.subplots()
    plt.imshow(img)

    coords = []

    def onclick(event):
        global ix, iy
        ix, iy = event.xdata, event.ydata
        print(f'({ix}, {iy})')

        global coords
        coords.append((ix, iy))

        # if event.key_press_event:
        #     fig.canvas.mpl_disconnect(cid)

        return coords
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

def export(ref):
    global coords
    df = pd.DataFrame(coords, columns=['x', 'y'])
    df = df.assign(ref=ref)
    df.to_csv(f'nb_data/wiedmann_fig2/{ref}.csv')
    plt.close()
    coords=[]
