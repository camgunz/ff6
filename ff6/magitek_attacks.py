from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

MagitekAttacks = (
    ArrayField(
        name='magitek_attacks',
        count=counts.MagitekAttacks,
        offset=offsets.MagitekAttackData,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('magitek'),
    ),
    ArrayField(
        name='magitek_attacks',
        count=counts.MagitekAttacks,
        offset=offsets.MagitekAttackNames,
        element_size=sizes.MagitekAttackName,
        element_field=StructField(
            name='magitek_attack',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.MagitekAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
)
