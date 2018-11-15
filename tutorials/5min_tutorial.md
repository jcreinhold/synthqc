# Quick Tutorial

## Overview

1) `synth-quality` - given truth and synthesized images, generate a plot that looks at the synthesis quality
2) `directory-view` - create figures of views of all images in a directory

## synth-quality example

From the command line call:

```bash
synth-quality -s zs/ -t train/t1/ -o . -v
```

and a series of radar plots with three metrics (normalized cross correlation, (entropy normalized) mutual information,
and mean structural similarity (SSIM)). In this case the plots will have the same name and be output in the current directory.

## directory-view example

From the command line call:

```bash
directory-view -i train/t1/ -v --slices 90 110 --axis 2
```

and slices 90 and 110 on the third axis (count of axis starts from 0)
from the image will be plotted into unique images in the directory `train/t1`
with the same name as the image with the slice number appended.
