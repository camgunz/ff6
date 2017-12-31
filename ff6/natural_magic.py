from ff6 import counts, offsets, sizes

from ff6.struct import *

TerraNaturalMagic = (
    ArrayField(
        name='terra_natural_magic',
        count=counts.NaturalMagic,
        element_size=sizes.NaturalMagic,
        offset=offsets.TerraNaturalMagic,
        element_field=StructField(
            name='natural_magic',
            offset=0,
            fields=(
                U8Field('spell', 0),
                U8Field('level', 1),
            )
        )
    ),
)

CelesNaturalMagic = (
    ArrayField(
        name='celes_natural_magic',
        count=counts.NaturalMagic,
        element_size=sizes.NaturalMagic,
        offset=offsets.CelesNaturalMagic,
        element_field=StructField(
            name='natural_magic',
            offset=0,
            fields=(
                U8Field('spell', 0),
                U8Field('level', 1),
            )
        )
    ),
)
