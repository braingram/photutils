# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Tests for the photutils PSF converters.
"""

import contextlib

import asdf
import pytest
from numpy.testing import assert_array_equal

from photutils.converters import _ASDF_ASTROPY_INSTALLED


def test_psf_converters(tmp_path, airy_disk_psf):
    """
    Test that the PSF converters can round-trip a PSF object.
    """

    if _ASDF_ASTROPY_INSTALLED:
        ctx = contextlib.nullcontext()
    else:
        pytest.raises(ImportError, match='asdf-astropy must be installed')
    psf, pars = airy_disk_psf

    af = asdf.AsdfFile()
    af['psf'] = psf
    with ctx:
        af.write_to(tmp_path / 'psf.asdf')

        with asdf.open(tmp_path / 'psf.asdf') as af:
            psf2 = af['psf']
            for parameter in pars:
                assert_array_equal(getattr(psf, parameter),
                                   getattr(psf2, parameter))
