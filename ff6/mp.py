from ff6 import offsets

from ff6.struct import *

MPPerLevel = (
    ArrayField(
        name='mp_per_level',
        count=98,
        element_size=1,
        offset=offsets.MPGainData,
        element_field=U8Field('mp_gain', 0)
    ),
)
