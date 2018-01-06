from ff6 import counts, offsets, sizes

from ff6.dte import DTE_BATTLE, TO_DTE_BATTLE
from ff6.data import *
from ff6.magic import get_magic_data_struct
from ff6.struct import *

BattleDialogues1 = (
    ArrayField(
        name='battle_dialogues1',
        count=counts.BattleDialogues1,
        offset=offsets.BattleDialoguePointers1,
        element_size=2,
        element_field=StructField(
            name='battle_dialogue',
            offset=0,
            fields=(
                PointerField(
                    name='contents',
                    offset=0,
                    base=offsets.BattleDialogues1,
                    pointer_field=U16Field(name='pointer', offset=0),
                    target_field=StrField(
                        name='contents',
                        terminator=b'\x00',
                        offset=0,
                        translation=(TO_DTE_BATTLE, DTE_BATTLE)
                    ),
                ),
            )
        )
    ),
)

BattleDialogues2 = (
    ArrayField(
        name='battle_dialogues2',
        count=counts.BattleDialogues2,
        offset=offsets.BattleDialoguePointers2,
        element_size=2,
        element_field=StructField(
            name='battle_dialogue',
            offset=0,
            fields=(
                PointerField(
                    name='contents',
                    offset=0,
                    base=offsets.BattleDialogues2,
                    pointer_field=U16Field(name='pointer', offset=0),
                    target_field=StrField(
                        name='contents',
                        terminator=b'\x00',
                        offset=0,
                        translation=(TO_DTE_BATTLE, DTE_BATTLE)
                    ),
                ),
            )
        )
    ),
)

BattleMessages = (
    ArrayField(
        name='battle_messages',
        count=counts.BattleMessages,
        offset=offsets.BattleMessagePointers,
        element_size=2,
        element_field=StructField(
            name='battle_dialogue',
            offset=0,
            fields=(
                PointerField(
                    name='contents',
                    offset=0,
                    base=offsets.BattleMessages,
                    pointer_field=U16Field(name='pointer', offset=0),
                    target_field=StrField(
                        name='contents',
                        terminator=b'\x00',
                        offset=0,
                        translation=(TO_DTE_BATTLE, DTE_BATTLE)
                    ),
                ),
            )
        )
    ),
)
