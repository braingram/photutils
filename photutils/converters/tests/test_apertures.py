# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Tests for the photutils aperture converters.
"""

import contextlib

import asdf
import numpy as np
import pytest

from photutils.aperture import CircularAperture
from photutils.converters import _ASDF_ASTROPY_INSTALLED

apertures = [
    CircularAperture(positions=[(1, 2), (3, 4)], r=5),
    CircularAperture(positions=(5, 6), r=7),
]


@pytest.mark.parametrize('aperture', apertures)
def test_aperture_converters(tmp_path, aperture):
    """
    Test that the aperture converters can round-trip an aperture object.
    """
    if _ASDF_ASTROPY_INSTALLED:
        ctx = contextlib.nullcontext()
    else:
        pytest.raises(ImportError, match='asdf-astropy must be installed')

    af = asdf.AsdfFile()
    af['aperture'] = aperture
    with ctx:
        af.write_to(tmp_path / 'aperture.asdf')

        with asdf.open(tmp_path / 'aperture.asdf') as af:
            aperture2 = af['aperture']

            assert np.all(aperture.positions == aperture2.positions)
            assert aperture.r == aperture2.r
