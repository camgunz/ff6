from ff6 import offsets

from ff6.struct import *

HPPerLevel = (
    ArrayField(
        name='hp_per_level',
        count=98,
        element_size=1,
        offset=offsets.HPGainData,
        element_field=U8Field('hp_gain', 0)
    ),
)
