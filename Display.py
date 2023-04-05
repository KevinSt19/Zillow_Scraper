# Trying different display methods from https://discuss.dizzycoding.com/generate-a-heatmap-in-matplotlib-using-a-scatter-data-set/

import pandas as pd
import matplotlib.pyplot as plt

import math

df = pd.read_csv('df.csv')

# Display as scatter plot
# argument 'c' is color

def showScatter():
    plt.scatter('longitude','latitude',c='price', data = df)
    plt.colorbar()
    plt.show()
    return
    
# Display using numpy's histogram2d function

def showHisto2d():
    import numpy as np
    x = df['longitude']
    y = df['latitude']
    heatmap, xedges, yedges = np.histogram2d(x,y,bins=50)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin = 'lower')
    plt.show()
    return
    
# Display a smoothed heatmap using np.histogram2d and a gaussian filter

def showSmoothed():
    import numpy as np
    import matplotlib.cm as cm
    from scipy.ndimage.filters import gaussian_filter
    def myplot(x,y,s,bins=1000):
        heatmap, xedges, yedges = np.histogram2d(x,y,bins=bins)
        heatmap = gaussian_filter(heatmap, sigma = s)
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
        return heatmap.T, extent
    fig, axs = plt.subplots(2,2)
    x = df['longitude']
    y = df['latitude']
    sigmas = [0,16,32,64]
    for ax, s in zip(axs.flatten(), sigmas):
        if s == 0:
            ax.plot(x,y,'k.',markersize=5)
            ax.set_title("Scatter plot")
        else:
            img, extent = myplot(x,y,s)
            ax.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
            ax.set_title("Smoothing with $sigma$ = %d" % s)
    plt.show()
    return
   
    
if __name__ == "__main__":
    #showScatter()
    showSmoothed()