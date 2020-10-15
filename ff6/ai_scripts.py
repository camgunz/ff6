from ff6.struct import *

AttackUsingOneOf = StructField(
    name='attack_using_one_of',
    offset=0,
    fields=(
        StaticField('command_byte', 0xF0, 0),
        ArrayField(
            name='attacks',
            count=3,
            element_size=1,
            offset=1,
            element_field=U8Field('attack', 0)
        )
    )
)
