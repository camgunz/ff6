from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

SlotAttacks = (
    ArrayField(
        name='slot_attacks',
        count=counts.SlotAttacks,
        offset=offsets.SlotAttackData,
        element_size=sizes.MagicData,
        element_field=get_magic_data_struct('slot'),
    ),
    ArrayField(
        name='slot_attacks',
        count=counts.SlotAttacks,
        offset=offsets.SlotAttackNames,
        element_size=sizes.SlotAttackName,
        element_field=StructField(
            name='slot_attack',
            offset=0,
            fields=(
                StrField(
                    name='name',
                    size=sizes.SlotAttackName,
                    translation=(TO_DTE_BATTLE, DTE_BATTLE),
                    offset=0
                ),
            )
        )
    ),
)
