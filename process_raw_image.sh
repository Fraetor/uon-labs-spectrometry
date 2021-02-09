#! /usr/bin/env bash

OUT_FILE=$(basename -s .JPG $1).png

convert "$1" -rotate -9.5 -shear 8x0 -crop 357x1110+2420+820 -grayscale Average "$OUT_FILE"

