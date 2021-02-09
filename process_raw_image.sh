#! /usr/bin/env bash

OUT_FILE = $(basename $1 .JPG).png

convert $1 -rotate -9.5 -shear -5.1 -crop 357x1110+2190+806 -grayscale Aveerage $OUT_FILE
