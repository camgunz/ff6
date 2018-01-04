from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

MagitekMenu = (
    ArrayField(
        name='magitek_menu',
        count=counts.MagitekMenuSlots,
        offset=offsets.MagitekMenuTargeting,
        element_size=1,
        element_field=StructField(
            name='magitek_menu_slot',
            offset=0,
            fields=(
                FlagsField('targeting', Targeting, 0),
                # U8Field('targeting', 0),
            )
        )
    ),
    ArrayField(
        name='magitek_menu',
        count=counts.MagitekMenuSlots,
        offset=offsets.MagitekMenuCommands,
        element_size=1,
        element_field=StructField(
            name='magitek_menu_slot',
            offset=0,
            fields=(
                U8Field('commands', 0),
            )
        )
    ),
    ArrayField(
        name='magitek_menu',
        count=counts.MagitekMenuSlots,
        offset=offsets.MagitekMenuTerraCommands,
        element_size=1,
        element_field=StructField(
            name='magitek_menu_slot',
            offset=0,
            fields=(
                U8Field('terra_commands', 0),
            )
        )
    ),
)