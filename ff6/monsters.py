from ff6.data import *
from ff6.type_checks import *
from ff6.typed_object import TypedObject, TypedObjectContainer

class Monster(TypedObject):

    NameSize = 10
    DataSize = 32
    TypeName = 'Monster'

    @classmethod
    def _attributes(cls):
        return super()._attributes() + (
            ('number', check_u8),
            ('name', check_str),
            ('strength', check_u8),
            ('speed', check_u8),
            ('hit_rate', check_u8),
            ('evade', check_u8),
            ('magic_block', check_u8),
            ('defense', check_u8),
            ('magic_defense', check_u8),
            ('magic_power', check_u8),
            ('hp', check_u16),
            ('mp', check_u16),
            ('xp', check_u16),
            ('gp', check_u16),
            ('level', check_u8),
            ('morph_package', check_u5),
            ('morph_chance', check_enum_member(MetamorphChance)),
            ('dies_if_mp_exhausted', check_bool),
            ('name_hidden', check_bool),
            ('undead', check_bool),
            ('blocks_run', check_bool),
            ('nullifies_scan', check_bool),
            ('absorbs_fire', check_bool),
            ('absorbs_ice', check_bool),
            ('absorbs_lightning', check_bool),
            ('absorbs_poison', check_bool),
            ('absorbs_wind', check_bool),
            ('absorbs_pearl', check_bool),
            ('absorbs_earth', check_bool),
            ('absorbs_water', check_bool),
            ('nullifies_fire', check_bool),
            ('nullifies_ice', check_bool),
            ('nullifies_lightning', check_bool),
            ('nullifies_poison', check_bool),
            ('nullifies_wind', check_bool),
            ('nullifies_pearl', check_bool),
            ('nullifies_earth', check_bool),
            ('nullifies_water', check_bool),
            ('weak_to_fire', check_bool),
            ('weak_to_ice', check_bool),
            ('weak_to_lightning', check_bool),
            ('weak_to_poison', check_bool),
            ('weak_to_wind', check_bool),
            ('weak_to_pearl', check_bool),
            ('weak_to_earth', check_bool),
            ('weak_to_water', check_bool),
            ('attack_type', check_u8),
            ('immune_to_dark', check_bool),
            ('immune_to_zombie', check_bool),
            ('immune_to_poison', check_bool),
            ('immune_to_magitek', check_bool),
            ('immune_to_vanish', check_bool),
            ('immune_to_imp', check_bool),
            ('immune_to_petrify', check_bool),
            ('immune_to_death', check_bool),
            ('immune_to_condemned', check_bool),
            ('immune_to_kneeling', check_bool),
            ('immune_to_blink', check_bool),
            ('immune_to_silence', check_bool),
            ('immune_to_berserk', check_bool),
            ('immune_to_confusion', check_bool),
            ('immune_to_hp_drain', check_bool),
            ('immune_to_sleep', check_bool),
            ('immune_to_dance_or_float', check_bool),
            ('immune_to_regen', check_bool),
            ('immune_to_slow', check_bool),
            ('immune_to_haste', check_bool),
            ('immune_to_stop', check_bool),
            ('immune_to_shell', check_bool),
            ('immune_to_safe', check_bool),
            ('immune_to_reflect', check_bool),
            ('immune_to_rage', check_bool),
            ('immune_to_frozen', check_bool),
            ('immune_to_protection_from_death', check_bool),
            ('immune_to_morph', check_bool),
            ('immune_to_casting', check_bool),
            ('immune_to_removed', check_bool),
            ('immune_to_defended_by_interceptor', check_bool),
            ('immune_to_float', check_bool),
            ('special_attack_effect',
                    check_enum_member(MonsterSpecialAttackEffect)),
            ('special_attack_causes_no_damage', check_bool)
        )

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.MonsterNamesOffset + name_offset
        name = rom.read_dte_battle_string(name_start, cls.NameSize)
        data_offset = cls.DataSize * number
        data_start = rom.MonsterDataOffset + data_offset
        speed = rom.read_byte(data_start + 0)
        strength = rom.read_byte(data_start + 1)
        hit_rate = rom.read_byte(data_start + 2)
        evade = rom.read_byte(data_start + 3)
        magic_block = rom.read_byte(data_start + 4)
        defense = rom.read_byte(data_start + 5)
        magic_defense = rom.read_byte(data_start + 6)
        magic_power = rom.read_byte(data_start + 7)
        hp = rom.read_short(data_start + 8)
        mp = rom.read_short(data_start + 10)
        xp = rom.read_short(data_start + 12)
        gp = rom.read_short(data_start + 14)
        level = rom.read_byte(data_start + 16)
        morph_chance = rom.read_high_bits(data_start + 17, 3)
        morph_chance = get_enum_member('morph chance', MetamorphChance, morph_chance)
        morph_package = rom.read_low_bits(data_start + 17, 5)
        monster_flags1 = rom.read_byte(data_start + 18)
        monster_flags2 = rom.read_byte(data_start + 19)
        absorbed_elements = rom.read_byte(data_start + 23)
        nullified_elements = rom.read_byte(data_start + 24)
        weak_elements = rom.read_byte(data_start + 25)
        attack_type = rom.read_byte(data_start + 26)
        # attack_type = get_enum_member(
        #     'attack type', MonsterAttackType, attack_type)
        immune_cond1 = rom.read_byte(data_start + 27)
        immune_cond2 = rom.read_byte(data_start + 28)
        immune_cond3 = rom.read_byte(data_start + 29)
        immune_cond4 = rom.read_byte(data_start + 30)
        special_attack_effect = rom.read_low_bits(data_start + 31, 6)
        special_attack_effect = get_enum_member('special attack effect',
                                                MonsterSpecialAttackEffect,
                                                special_attack_effect)
        special_attack_causes_no_damage = rom.read_bit(data_start + 31, 7)
        attributes = {}
        enum_params = [
            ('monster flags 1', monster_flags1, MonsterFlag1),
            ('monster flags 2', monster_flags2, MonsterFlag2),
            ('absorbed elements', absorbed_elements, Element, 'absorbs_'),
            ('nullified elements', nullified_elements, Element, 'nullifies_'),
            ('weak elements', weak_elements, Element, 'weak_to_'),
            ('immune conditions 1', immune_cond1, Condition1, 'immune_to_'),
            ('immune conditions 2', immune_cond2, Condition2, 'immune_to_'),
            ('immune conditions 3', immune_cond3, Condition3, 'immune_to_'),
            ('immune conditions 4', immune_cond4, Condition4, 'immune_to_'),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        attributes['name'] = name
        attributes['number'] = number
        attributes['strength'] = strength
        attributes['speed'] = speed
        attributes['hit_rate'] = hit_rate
        attributes['evade'] = evade
        attributes['magic_block'] = magic_block
        attributes['defense'] = defense
        attributes['magic_defense'] = magic_defense
        attributes['magic_power'] = magic_power
        attributes['hp'] = hp
        attributes['mp'] = mp
        attributes['xp'] = xp
        attributes['gp'] = gp
        attributes['level'] = level
        attributes['morph_package'] = morph_package
        attributes['morph_chance'] = morph_chance
        attributes['attack_type'] = attack_type
        attributes['special_attack_effect'] = special_attack_effect
        attributes['special_attack_causes_no_damage'] = \
            special_attack_causes_no_damage
        return cls(**attributes)

class Monsters(TypedObjectContainer):
    ObjectCount = 256
    ObjectType = Monster
    Name = 'Monsters'
