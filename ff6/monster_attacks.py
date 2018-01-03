from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

MonsterAttacks = (
    ArrayField(
        name='monster_attacks',
        count=counts.MonsterAttacks,
        offset=offsets.MonsterAttackData,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('monster'),
    ),
    ArrayField(
        name='monster_attacks',
        count=counts.MonsterAttacks,
        offset=offsets.MonsterAttackNames,
        element_size=sizes.MonsterAttackName,
        element_field=StructField(
            name='monster_attack',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.MonsterAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
)
