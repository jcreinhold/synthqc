#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
synthqc.plot.directory_view

create profile view images of all images in a directory

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Jun 20, 2018
"""

__all__ = ['directory_view']

import logging
import os

import matplotlib.pyplot as plt
import nibabel as nib

from ..errors import SynthQCError
from ..util.io import glob_nii, split_filename

logger = logging.getLogger(__name__)


def directory_view(img_dir, out_dir=None, labels=None, figsize=(8,8), outtype='png',
                   slices=None, axis=0, trim=True, dpi=200):
    """
    create images for a directory of nifti files

    Args:
        img_dir (str): path to directory
        out_dir (str): path to save directory
        labels (str): path to directory of corresponding labels (not needed)
        figsize (float): size of output image
        outtype (str): type of file to output (e.g., png, pdf, etc.)
        slices (tuple): plot these slices in axial view (instead of ortho)
        axis (int): axis from which to sample (0<=axis<=2)
        trim (bool): trim blank/white space from image (need to have imagemagick installed)

    Returns:
        None
    """
    img_fns = glob_nii(img_dir)
    if labels is None:
        label_fns = [None] * len(img_fns)
    else:
        label_fns = glob_nii(labels)
        if len(img_fns) != len(label_fns):
            raise SynthQCError('Number of images and labels must be equal')
    if out_dir is None:
        out_dir, _, _ = split_filename(img_fns[0])
    for i, (img_fn, label_fn) in enumerate(zip(img_fns, label_fns), 1):
        _, base, _ = split_filename(img_fn)
        logger.info('Creating view for image: {} ({:d}/{:d})'.format(base, i, len(img_fns)))
        img = nib.load(img_fn).get_data()
        if labels is not None:
            logger.warning('Label/masks are not currently supported')
        slices = (img.shape[axis]//2,) if slices is None else slices
        for slice in slices:
            s = img[slice,:,:] if axis == 0 else \
                img[:,slice,:] if axis == 1 else \
                img[:,:,slice]
            im = s.squeeze()
            _ = plt.figure(figsize=figsize)
            plt.imshow(im, cmap='gray')
            plt.axis('off')
            out_fn = os.path.join(out_dir, base + str(slice) + '.' + outtype)
            plt.savefig(out_fn, dpi=dpi)
    if trim:
        logger.info('trimming blank space from all views')
        from subprocess import call
        try:
            call(['mogrify', '-trim', os.path.join(out_dir,'*.'+outtype)])
        except OSError as e:
            logger.warning('need to have imagemagick installed if trim option on')
            logger.error(e)

