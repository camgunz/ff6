from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

Dances = (
    ArrayField(
        name='dances',
        count=counts.Dances,
        offset=offsets.DanceNames,
        element_size=sizes.DanceName,
        element_field=StrField(
            name='name',
            size=sizes.DanceName,
            translation=(TO_DTE_BATTLE, DTE_BATTLE),
            offset=0
        ),
    ),
)

DanceAttacks = (
    ArrayField(
        name='dance_attacks',
        count=counts.DanceAttacks,
        offset=offsets.DanceAttackData,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('dance'),
    ),
    ArrayField(
        name='dance_attacks',
        count=counts.DanceAttacks,
        offset=offsets.DanceAttackNames,
        element_size=sizes.DanceAttackName,
        element_field=StructField(
            name='dance_attack',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.DanceAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
)
