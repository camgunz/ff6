from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

MagitekMenu = (
    ArrayField(
        name='magitek_menu',
        count=counts.MagitekMenuSlots,
        offset=offsets.MagitekMenu,
        element_size=sizes.MagitekMenuSlot,
        element_field=StructField(
            name='magitek_menu_slot',
            offset=0,
            fields=(
                U8Field('terra_command', 0),
                U8Field('targeting', 1),
                U8Field('regular_command', 2),
            )
        )
    ),
)
