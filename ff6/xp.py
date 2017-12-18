from ff6 import offsets

from ff6.struct import *

XPPerLevel = (
    ArrayField(
        name='xp_per_level',
        count=98,
        element_size=2,
        offset=offsets.XPRequiredData,
        element_field=U16Field(
            name='xp_required',
            offset=0,
            transform_out=lambda x: x // 8,
            transform_in=lambda x: x * 8
        )
    ),
)
