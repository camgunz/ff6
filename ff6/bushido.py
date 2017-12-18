from ff6 import offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.struct import *

BushidoNames = (
    ArrayField(
        name='bushido_names',
        count=8,
        element_size=sizes.BushidoName,
        offset=offsets.BushidoNames,
        element_field=StrField(
            name='name',
            size=sizes.BushidoName,
            translation=(TO_DTE_BATTLE, DTE_BATTLE),
            offset=0
        )
    ),
)
