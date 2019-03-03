from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

my_file = fits.open('wow.fits')
print(my_file.info())
