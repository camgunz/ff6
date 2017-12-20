from ff6 import offsets, sizes

from ff6.data import *
from ff6.struct import *

CharacterStarts = (
    ArrayField(
        name='character_starts',
        offset=offsets.CharacterStartData,
        count=41,
        element_size=sizes.CharacterStart,
        element_field=StructField(
            name='character_start',
            offset=0,
            fields=(
                U8Field('hp', 0),
                U8Field('mp', 1),
                EnumField('battle_command1', BattleCommand, 2),
                EnumField('battle_command2', BattleCommand, 3),
                EnumField('battle_command3', BattleCommand, 4),
                EnumField('battle_command4', BattleCommand, 5),
                U8Field('vigor', 6),
                U8Field('speed', 7),
                U8Field('stamina', 8),
                U8Field('magic_power', 9),
                U8Field('battle_power', 10),
                U8Field('defense', 11),
                U8Field('magic_defense', 12),
                U8Field('evade', 13),
                U8Field('magic_block', 14),
                U8Field('weapon', 15),
                U8Field('shield', 16),
                U8Field('hat', 17),
                U8Field('armor', 18),
                U8Field('relic1', 19),
                U8Field('relic2', 20),
                U8Field('level', 21),
            )
        )
    ),
)
