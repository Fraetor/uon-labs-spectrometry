#! /usr/bin/env python3

# Imports
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import sys


# Functions
def mean_horizontal_brightness(image):
    """
    Returns a list of the mean brightness of each horizontal strip in the image.
    Requires a PIL image object to be passes as an argument.
    """
    brightnesses = []
    for y in range(image.height):
        brightness = 0
        for x in range(image.width):
            brightness = +image.getpixel((x, y))
        mean_brightness = brightness / (image.width+1)
        brightnesses.append(mean_brightness)
    return brightnesses


# Configuration
input_file = sys.argv[1]


# Code
spectra = im.open(input_file, "r")
intensity = mean_horizontal_brightness(spectra)

wavelength = np.linspace(400, 660, len(intensity))

N = 50
smoothed_intensity = np.convolve(intensity, np.ones(N)/N, mode='valid')
wavelength2 = np.linspace(400, 660, len(smoothed_intensity))

# Blue is at the top of the image and thus is first in the list.
plt.plot(wavelength, intensity, "-", label="Raw data")
plt.plot(wavelength2, smoothed_intensity, "r-", label="Smoothed data")
plt.legend()
plt.xlabel("Wavelength, λ / nm")
plt.ylabel("Intensity / Arbitrary units")
plt.title("Graph of intensity against wavelength of a spectra.")
plt.savefig(input_file+".pdf",  dpi=300)
