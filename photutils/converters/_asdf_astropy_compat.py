# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Compatibility module for handling environments missing asdf-astropy.
"""

try:
    import asdf_astropy  # noqa: F401 -- needed to register the converters
    _ASDF_ASTROPY_INSTALLED = True
except ImportError:
    _ASDF_ASTROPY_INSTALLED = False

if _ASDF_ASTROPY_INSTALLED:
    def raise_if_no_asdf_astropy(class_name):
        pass
else:
    def raise_if_no_asdf_astropy(class_name):
        msg = (
            'asdf-astropy must be installed to serialize'
            f'{class_name} from ASDF. Install it with:\n'
            '    pip install asdf-astropy'
        )
        raise ImportError(msg)
