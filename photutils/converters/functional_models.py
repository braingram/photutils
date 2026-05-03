# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Converters to and from the ASDF format for photutils.psf.functional_models.
"""

from ._asdf_astropy_compat import (_ASDF_ASTROPY_INSTALLED,
                                   raise_if_no_asdf_astropy)

if _ASDF_ASTROPY_INSTALLED:
    from asdf_astropy.converters.transform.core import (TransformConverterBase,
                                                        parameter_to_value)
else:
    # alias Converter as TransformConverterBase to allow the below class
    # definition to work when asdf-astropy is not installed
    from asdf.extension import Converter as TransformConverterBase

__all__ = ['AiryDiskPSFConverter']


class AiryDiskPSFConverter(TransformConverterBase):
    """
    Converter for AiryDiskPSF.
    """

    tags = ('tag:astropy.org:photutils/psf/airy_disk_psf-*',)
    types = ('photutils.psf.AiryDiskPSF',)

    def to_yaml_tree_transform(self, model, tag, ctx):  # noqa: ARG002
        return {
            'flux': parameter_to_value(model.flux),
            'x_0': parameter_to_value(model.x_0),
            'y_0': parameter_to_value(model.y_0),
            'radius': parameter_to_value(model.radius),
            'bbox_factor': model.bbox_factor,
        }

    def from_yaml_tree_transform(self, node, tag, ctx):  # noqa: ARG002
        from photutils.psf import AiryDiskPSF

        return AiryDiskPSF(
            flux=node['flux'],
            x_0=node['x_0'],
            y_0=node['y_0'],
            radius=node['radius'],
            bbox_factor=node['bbox_factor'],
        )

    def to_yaml_tree(self, obj, tag, ctx):  # noqa: ARG002
        raise_if_no_asdf_astropy('AiryDiskPSF')

        return super().to_yaml_tree(obj, tag, ctx)

    def from_yaml_tree(self, node, tag, ctx):  # noqa: ARG002
        raise_if_no_asdf_astropy('AiryDiskPSF')

        return super().from_yaml_tree(node, tag, ctx)
