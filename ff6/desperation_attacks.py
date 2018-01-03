from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

DesperationAttacks = (
    ArrayField(
        name='desperation_attacks',
        count=counts.DesperationAttacks,
        offset=offsets.DesperationAttackData,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('desperation'),
    ),
    ArrayField(
        name='desperation_attacks',
        count=counts.DesperationAttacks,
        offset=offsets.DesperationAttackNames,
        element_size=sizes.DesperationAttackName,
        element_field=StructField(
            name='desperation_attack',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.DesperationAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
)
