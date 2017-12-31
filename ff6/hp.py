from ff6 import counts, offsets

from ff6.struct import *

HPPerLevel = (
    ArrayField(
        name='hp_per_level',
        count=counts.HPLevels,
        element_size=1,
        offset=offsets.HPGainData,
        element_field=U8Field('hp_gain', 0)
    ),
)
