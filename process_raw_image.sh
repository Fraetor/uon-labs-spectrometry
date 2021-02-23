#! /usr/bin/env bash

OUT_FILE=$(basename -s .JPG $1).png

# Cut out and straighten relavent section of spectra, then greyscale.
convert "$1" -rotate -9.5 -shear 8x0 -crop 357x1110+2420+820 -grayscale Average "$OUT_FILE"

# Make graph from processed image.
python3 graph_spectra.py "$OUT_FILE"

#clear up processed image.
rm "$OUT_FILE"
