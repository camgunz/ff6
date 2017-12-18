from ff6 import offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.struct import *

BlitzNames = (
    ArrayField(
        name='blitzes',
        count=8,
        element_size=sizes.BlitzName,
        offset=offsets.BlitzNames,
        element_field=StrField(
            name='name',
            size=sizes.BlitzName,
            translation=(TO_DTE_BATTLE, DTE_BATTLE),
            offset=0
        )
    ),
)
