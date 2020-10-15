from ff6 import counts, offsets, sizes

from ff6.struct import *

MorphPackages = (
    ArrayField(
        name='morph_packages',
        count=counts.MorphPackages,
        element_size=sizes.MorphPackage,
        offset=offsets.MorphPackages,
        element_field=StructField(
            name='morph_package',
            offset=0,
            fields=(
                U8Field('item1', 0),
                U8Field('item2', 1),
                U8Field('item3', 2),
                U8Field('item4', 3),
            )
        )
    ),
)
