import numpy as np
from numba import jit
from matplotlib import pyplot as plt
from matplotlib import colors

@jit
def mandelbrot(z,maxiter,horizon,log_horizon):
    c = z
    for n in range(maxiter):
        az = abs(z)
        if az > horizon:
            return n - np.log(np.log(az))/np.log(2) + log_horizon
        z = z*z + c
    return 0

@jit
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    horizon = 2.0 ** 40
    log_horizon = np.log(np.log(horizon))/np.log(2)
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],maxiter,horizon, log_horizon)
    return (r1,r2,n3)

def mandelbrot_image(xmin,xmax,ymin,ymax,width=10,height=10,maxiter=80):
    dpi = 100
    img_width = dpi * width
    img_height = dpi * height
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)
    return z.T     

COLORMAPS = ['hot', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 
             'cubehelix', 'hsv', 'nipy_spectral', 'gist_ncar']

im1 = mandelbrot_image(-2.0,0.5,-1.25,1.25,maxiter=50,width=20,height=20)
im2 = mandelbrot_image(-0.74877,-0.74872,0.065053,0.065103,maxiter=2048,width=20,height=20)
im3 = mandelbrot_image(-0.75,-0.747,0.063,0.066,maxiter=2048,width=20,height=20)


images = []
images.extend([im1, im2, im3])


for cmap in COLORMAPS:
    for i in range(len(images)):       
        plt.imsave('mandelbrot_images/{}_{}'.format(cmap,i+1), images[i], cmap=cmap)