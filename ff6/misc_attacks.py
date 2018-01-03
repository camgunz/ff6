from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

MiscAttacks = (
    ArrayField(
        name='misc_attacks',
        count=counts.MiscAttacks,
        offset=offsets.MiscAttackData,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('misc_attack'),
    ),
    ArrayField(
        name='misc_attacks',
        count=counts.MiscAttacks,
        offset=offsets.MiscAttackNames,
        element_size=sizes.MiscAttackName,
        element_field=StructField(
            name='misc_attack',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.MiscAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
)
