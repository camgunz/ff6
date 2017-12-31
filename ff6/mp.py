from ff6 import counts, offsets

from ff6.struct import *

MPPerLevel = (
    ArrayField(
        name='mp_per_level',
        count=counts.MPLevels,
        element_size=1,
        offset=offsets.MPGainData,
        element_field=U8Field('mp_gain', 0)
    ),
)
