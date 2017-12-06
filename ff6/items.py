from ff6.data import *
from ff6.type_checks import *
from ff6.typed_object import TypedObject, TypedObjectContainer

class InventoryItem(TypedObject):

    NameSize = 13
    DataSize = 30

    @classmethod
    def _attributes(cls):
        return super()._attributes() + (
            ('number', check_u8),
            ('name', check_str),
            ('type', check_enum_member(InventoryItemType)),
            ('throwable', check_bool),
            ('usable_in_battle', check_bool),
            ('usable_in_field', check_bool),
            ('targets_single_ally_or_enemy', check_bool),
            ('targets_allies_or_enemies_only', check_bool),
            ('targets_all_allies_and_enemies', check_bool),
            ('targets_all_allies_or_all_enemies', check_bool),
            ('targets_only_default_selection', check_bool),
            ('targets_multiple', check_bool),
            ('targets_enemies_by_default', check_bool),
            ('targets_random', check_bool),
            ('price', check_u16)
        )

    def __str__(self):
        return '<%s (%d): %s>' % (self.type.name, self.number, self.name)

class Equipment(InventoryItem):

    @classmethod
    def _attributes(cls):
        return super()._attributes() + (
            ('equippable_by_terra', check_bool),
            ('equippable_by_locke', check_bool),
            ('equippable_by_cyan', check_bool),
            ('equippable_by_shadow', check_bool),
            ('equippable_by_edgar', check_bool),
            ('equippable_by_sabin', check_bool),
            ('equippable_by_celes', check_bool),
            ('equippable_by_strago', check_bool),
            ('equippable_by_relm', check_bool),
            ('equippable_by_setzer', check_bool),
            ('equippable_by_mog', check_bool),
            ('equippable_by_gau', check_bool),
            ('equippable_by_gogo', check_bool),
            ('equippable_by_umaro', check_bool),
            ('equippable_by_imp', check_bool),
            ('spell_learn_rate', check_u8),
            ('spell_learned', check_u8),
            ('reduces_enemy_attacks', check_bool),
            ('prevents_enemy_attacks', check_bool),
            ('doubles_walking_speed', check_bool),
            ('cures_one_hp_per_step', check_bool),
            ('protects_against_dark', check_bool),
            ('protects_against_zombie', check_bool),
            ('protects_against_poison', check_bool),
            ('protects_against_magitek', check_bool),
            ('protects_against_vanish', check_bool),
            ('protects_against_imp', check_bool),
            ('protects_against_petrify', check_bool),
            ('protects_against_death', check_bool),
            ('protects_against_condemned', check_bool),
            ('protects_against_kneeling', check_bool),
            ('protects_against_blink', check_bool),
            ('protects_against_silence', check_bool),
            ('protects_against_berserk', check_bool),
            ('protects_against_confusion', check_bool),
            ('protects_against_hp_drain', check_bool),
            ('protects_against_sleep', check_bool),
            ('raises_attack_damage', check_bool),
            ('raises_magic_damage', check_bool),
            ('raises_hp_one_quarter', check_bool),
            ('raises_hp_one_half', check_bool),
            ('raises_hp_one_eighth', check_bool),
            ('raises_mp_one_quarter', check_bool),
            ('raises_mp_one_half', check_bool),
            ('raises_mp_one_eighth', check_bool),
            ('enables_jump', check_bool),
            ('enables_x_magic', check_bool),
            ('enables_control', check_bool),
            ('enables_gp_rain', check_bool),
            ('enables_capture', check_bool),
            ('forces_continuous_jump', check_bool),
            ('increases_steal_rate', check_bool),
            ('enables_perfect_hit_rate', check_bool),
            ('halves_mp_consumption', check_bool),
            ('sets_mp_consumption_to_one', check_bool),
            ('raises_vigor', check_bool),
            ('enables_x_fight', check_bool),
            ('randomly_counter_attacks', check_bool),
            ('increases_evade_chance', check_bool),
            ('allows_two_hands', check_bool),
            ('allows_dual_wield', check_bool),
            ('enables_heavy_armor', check_bool),
            ('protects_allies', check_bool),
            ('casts_shell_on_low_hp', check_bool),
            ('casts_safe_on_low_hp', check_bool),
            ('casts_reflect_on_low_hp', check_bool),
            ('doubles_experience', check_bool),
            ('doubles_gold', check_bool),
            ('makes_body_cold', check_bool),
            ('fire_elemental', check_bool),
            ('ice_elemental', check_bool),
            ('lightning_elemental', check_bool),
            ('poison_elemental', check_bool),
            ('wind_elemental', check_bool),
            ('pearl_elemental', check_bool),
            ('earth_elemental', check_bool),
            ('water_elemental', check_bool),
            ('vigor', check_s4),
            ('speed', check_s4),
            ('stamina', check_s4),
            ('magic_power', check_s4),
            ('attack_when_used', check_u8),
            ('evade', check_u8),
            ('magic_block', check_u8),
        )

class DefensiveEquipment(Equipment):

    @classmethod
    def _attributes(cls):
        return super()._attributes() + (
            ('causes_float', check_bool),
            ('causes_regen', check_bool),
            ('causes_slow', check_bool),
            ('causes_haste', check_bool),
            ('causes_stop', check_bool),
            ('causes_shell', check_bool),
            ('causes_safe', check_bool),
            ('causes_reflect', check_bool),
            ('physical_defense', check_u8),
            ('magic_defense', check_u8),
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
            ('causes_condemned', check_bool),
            ('causes_kneeling', check_bool),
            ('causes_blink', check_bool),
            ('causes_silence', check_bool),
            ('causes_berserk', check_bool),
            ('causes_confusion', check_bool),
            ('causes_hp_drain', check_bool),
            ('causes_sleep', check_bool),
            ('evade_animation', check_enum_member(WeaponEvadeAnimation))
        )

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.ItemNamesOffset + name_offset
        name = rom.read_dte_battle_string(name_start, cls.NameSize)
        data_offset = cls.DataSize * number
        data_start = rom.ItemDataOffset + data_offset
        type = rom.read_byte(data_start + 0)
        usability = type & 0xF0
        type = type & 0x0F
        equippable_chars = rom.read_short(data_start + 1)
        spell_learn_rate = rom.read_byte(data_start + 3)
        spell_learned = rom.read_byte(data_start + 4)
        field_effects = rom.read_byte(data_start + 5)
        cond_protection1 = rom.read_byte(data_start + 6)
        cond_protection2 = rom.read_byte(data_start + 7)
        cond_caused3 = rom.read_byte(data_start + 8)
        status_effects1 = rom.read_byte(data_start + 9)
        battle_effects1 = rom.read_byte(data_start + 10)
        status_effects2 = rom.read_byte(data_start + 11)
        battle_effects2 = rom.read_byte(data_start + 12)
        battle_effects3 = rom.read_byte(data_start + 13)
        targeting = rom.read_byte(data_start + 14)
        elements = rom.read_byte(data_start + 15)
        vigor_and_speed = rom.read_signed_nybbles(data_start + 16)
        stamina_and_mpow = rom.read_signed_nybbles(data_start + 17)
        attack_when_used = rom.read_byte(data_start + 18)
        physical_defense = rom.read_byte(data_start + 20)
        magic_defense = rom.read_byte(data_start + 21)
        absorbed_elements = rom.read_byte(data_start + 22)
        nullified_elements = rom.read_byte(data_start + 23)
        weak_elements = rom.read_byte(data_start + 24)
        cond_caused2 = rom.read_byte(data_start + 25)
        evade_and_mblock = rom.read_signed_nybbles(data_start + 26)
        evade_animation = rom.read_low_bits(data_start + 27, 4)
        # special_attack, evade_animation = rom.read_nybbles(data_start + 27)
        price = rom.read_short(data_start + 28)
        attributes = {}
        if type != cls._InventoryItemType.value:
            msg = 'Invalid item type in ROM (got %s, expected %s)'
            raise ValueError(msg % (type, cls._InventoryItemType))
        attributes['number'] = number
        attributes['type'] = cls._InventoryItemType
        attributes['name'] = name
        attributes['spell_learn_rate'] = spell_learn_rate
        attributes['spell_learned'] = spell_learned
        attributes['attack_when_used'] = attack_when_used
        attributes['physical_defense'] = physical_defense
        attributes['magic_defense'] = magic_defense
        attributes['vigor'], attributes['speed'] = vigor_and_speed
        attributes['stamina'], attributes['magic_power'] = stamina_and_mpow
        attributes['evade'], attributes['magic_block'] = evade_and_mblock
        attributes['evade_animation'] = get_enum_member(
                'evade_animation', WeaponEvadeAnimation, evade_animation)
        attributes['price'] = price
        enum_params = [
            ('usability', usability, InventoryItemUsability),
            ('equippable chars', equippable_chars, Character,
             'equippable_by_'),
            ('field effects', field_effects, FieldEffect),
            ('protected conditions 1', cond_protection1, Condition1,
             'protects_against_'),
            ('protected conditions 2', cond_protection2, Condition2,
             'protects_against_'),
            ('caused conditions 3', cond_caused3, Condition3, 'causes_'),
            ('status effects 1', status_effects1, StatusEffect1),
            ('battle effects 1', battle_effects1, BattleEffect1),
            ('status effects 2', status_effects2, StatusEffect2),
            ('battle effects 2', battle_effects2, BattleEffect2),
            ('battle effects 3', battle_effects3, BattleEffect3),
            ('targeting', targeting, Targeting, 'targets_'),
            ('elements', elements, Element, None, '_elemental'),
            ('absorbed elements', absorbed_elements, Element, 'absorbs_'),
            ('nullified elements', nullified_elements, Element, 'nullifies_'),
            ('weak elements', weak_elements, Element, 'weak_to_'),
            ('caused conditions 2', cond_caused2, Condition2, 'causes_'),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        attributes['causes_float'] = attributes['causes_dance_or_float']
        del attributes['causes_dance_or_float']
        return cls(**attributes)

class Tool(InventoryItem):

    TypeName = 'Tool'

    @classmethod
    def _attributes(cls):
        return super()._attributes() + (
            ('attack_when_used', check_u8),
            ('attack_strength', check_u8),
            ('hit_rate', check_u8)
        )

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.ItemNamesOffset+name_offset
        name = rom.read_dte_battle_string(name_start, 13)
        data_offset = cls.DataSize * number
        data_start = rom.ItemDataOffset+data_offset
        type = rom.read_byte(data_start + 0)
        usability = type & 0xF0
        type = type & 0x0F
        targeting = rom.read_byte(data_start + 14)
        attack_when_used = rom.read_byte(data_start + 18)
        attack_strength = rom.read_byte(data_start + 20)
        hit_rate = rom.read_byte(data_start + 21)
        price = rom.read_short(data_start + 28)
        attributes = {}
        if type != InventoryItemType.Tool.value:
            msg = 'Invalid item type in ROM (got %s, expected %s)'
            raise ValueError(msg % (type, InventoryItemType.Tool))
        attributes['number'] = number
        attributes['type'] = InventoryItemType.Tool
        attributes['name'] = name
        attributes['attack_when_used'] = attack_when_used
        attributes['attack_strength'] = attack_strength
        attributes['hit_rate'] = hit_rate
        attributes['price'] = price
        enum_params = [
            ('usability', usability, InventoryItemUsability),
            ('targeting', targeting, Targeting, 'targets_'),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        return cls(**attributes)

class Weapon(Equipment):

    TypeName = 'Weapon'

    @classmethod
    def _attributes(cls):
        return super()._attributes() + (
            ('hit_rate', check_u8),
            ('causes_regen', check_bool),
            ('causes_slow', check_bool),
            ('causes_haste', check_bool),
            ('causes_stop', check_bool),
            ('causes_shell', check_bool),
            ('causes_safe', check_bool),
            ('causes_reflect', check_bool),
            ('causes_float', check_bool),
            ('usable_with_bushido', check_bool),
            ('same_damage_from_back_row', check_bool),
            ('usable_with_two_hands', check_bool),
            ('usable_with_runic', check_bool),
            ('battle_power', check_u8),
            ('special_attack', check_enum_member(WeaponSpecialAttack)),
            ('evade_animation', check_enum_member(WeaponEvadeAnimation))
        )

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.ItemNamesOffset+name_offset
        name = rom.read_dte_battle_string(name_start, 13)
        data_offset = cls.DataSize * number
        data_start = rom.ItemDataOffset+data_offset
        type = rom.read_byte(data_start + 0)
        usability = type & 0xF0
        type = type & 0x0F
        equippable_chars = rom.read_short(data_start + 1)
        spell_learn_rate = rom.read_byte(data_start + 3)
        spell_learned = rom.read_byte(data_start + 4)
        field_effects = rom.read_byte(data_start + 5)
        cond_protection1 = rom.read_byte(data_start + 6)
        cond_protection2 = rom.read_byte(data_start + 7)
        cond_caused3 = rom.read_byte(data_start + 8)
        status_effects1 = rom.read_byte(data_start + 9)
        battle_effects1 = rom.read_byte(data_start + 10)
        status_effects2 = rom.read_byte(data_start + 11)
        battle_effects2 = rom.read_byte(data_start + 12)
        battle_effects3 = rom.read_byte(data_start + 13)
        targeting = rom.read_byte(data_start + 14)
        elements = rom.read_byte(data_start + 15)
        vigor_and_speed = rom.read_signed_nybbles(data_start + 16)
        stamina_and_mpow = rom.read_signed_nybbles(data_start + 17)
        attack_when_used = rom.read_byte(data_start + 18)
        weapon_properties = rom.read_byte(data_start + 19)
        battle_power = rom.read_byte(data_start + 20)
        hit_rate = rom.read_byte(data_start + 21)
        evade, mblock = rom.read_nybbles(data_start + 26)
        special_attack_and_evade_animation = rom.read_nybbles(data_start + 27)
        price = rom.read_short(data_start + 28)
        attributes = {}
        if type != InventoryItemType.Weapon.value:
            msg = 'Invalid item type in ROM (got %s, expected %s)'
            raise ValueError(msg % (type, InventoryItemType.Weapon))
        attributes['number'] = number
        attributes['name'] = name
        attributes['type'] = InventoryItemType.Weapon
        attributes['spell_learn_rate'] = spell_learn_rate
        attributes['spell_learned'] = spell_learned
        attributes['attack_when_used'] = attack_when_used
        attributes['battle_power'] = battle_power
        attributes['hit_rate'] = hit_rate
        attributes['vigor'], attributes['speed'] = vigor_and_speed
        attributes['stamina'], attributes['magic_power'] = stamina_and_mpow
        attributes['evade'] = evade * 10
        attributes['magic_block'] = mblock * 10
        attributes['price'] = price
        enum_params = [
            ('usability', usability, InventoryItemUsability),
            ('equippable chars', equippable_chars, Character,
             'equippable_by_'),
            ('field effects', field_effects, FieldEffect),
            ('protected conditions 1', cond_protection1, Condition1,
             'protects_against_'),
            ('protected conditions 2', cond_protection2, Condition2,
             'protects_against_'),
            ('caused conditions 3', cond_caused3, Condition3, 'causes_'),
            ('status effects 1', status_effects1, StatusEffect1),
            ('battle effects 1', battle_effects1, BattleEffect1),
            ('status effects 2', status_effects2, StatusEffect2),
            ('battle effects 2', battle_effects2, BattleEffect2),
            ('battle effects 3', battle_effects3, BattleEffect3),
            ('targeting', targeting, Targeting, 'targets_'),
            ('elements', elements, Element, None, '_elemental'),
            ('weapon properties', weapon_properties, WeaponProperty),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        attributes['causes_float'] = attributes['causes_dance_or_float']
        del attributes['causes_dance_or_float']
        attributes['special_attack'], attributes['evade_animation'] = \
        special_attack, evade_animation = special_attack_and_evade_animation
        attributes['special_attack'] = get_enum_member(
            'special attack', WeaponSpecialAttack, special_attack)
        attributes['evade_animation'] = get_enum_member(
            'evade animation', WeaponEvadeAnimation, evade_animation)
        return cls(**attributes)

class Armor(DefensiveEquipment):

    TypeName = 'Armor'

    _InventoryItemType = InventoryItemType.Armor

class Shield(DefensiveEquipment):

    TypeName = 'Shield'

    _InventoryItemType = InventoryItemType.Shield

class Hat(DefensiveEquipment):

    TypeName = 'Hat'

    _InventoryItemType = InventoryItemType.Hat

class Relic(DefensiveEquipment):

    TypeName = 'Relic'

    _InventoryItemType = InventoryItemType.Relic

class Item(InventoryItem):

    TypeName = 'Item'

    @classmethod
    def _attributes(cls):
        return super()._attributes() + (
            ('causes_dark', check_bool),
            ('causes_zombie', check_bool),
            ('causes_poison', check_bool),
            ('causes_magitek', check_bool),
            ('causes_vanish', check_bool),
            ('causes_imp', check_bool),
            ('causes_petrify', check_bool),
            ('causes_death', check_bool),
            ('causes_condemned', check_bool),
            ('causes_kneeling', check_bool),
            ('causes_blink', check_bool),
            ('causes_silence', check_bool),
            ('causes_berserk', check_bool),
            ('causes_confusion', check_bool),
            ('causes_hp_drain', check_bool),
            ('causes_sleep', check_bool),
            ('causes_dance_or_float', check_bool),
            ('causes_regen', check_bool),
            ('causes_slow', check_bool),
            ('causes_haste', check_bool),
            ('causes_stop', check_bool),
            ('causes_shell', check_bool),
            ('causes_safe', check_bool),
            ('causes_reflect', check_bool),
            ('causes_rage', check_bool),
            ('causes_frozen', check_bool),
            ('causes_protection_from_death', check_bool),
            ('causes_morph', check_bool),
            ('causes_casting', check_bool),
            ('causes_removed', check_bool),
            ('causes_defended_by_interceptor', check_bool),
            ('causes_float', check_bool),
            ('reverse_damage_on_undead', check_bool),
            ('restores_hp', check_bool),
            ('restores_mp', check_bool),
            ('removes_status_conditions', check_bool),
            ('causes_damage', check_bool),
            ('effect_is_proportionate', check_bool),
            ('effect_strength', check_u8),
            ('special_action', check_enum_member(ItemSpecialAction))
        )

    @classmethod
    def from_rom(cls, rom, number):
        name_offset = cls.NameSize * number
        name_start = rom.ItemNamesOffset+name_offset
        name = rom.read_dte_battle_string(name_start, 13)
        data_offset = cls.DataSize * number
        data_start = rom.ItemDataOffset+data_offset
        type = rom.read_byte(data_start + 0)
        usability = type & 0xF0
        type = type & 0x0F
        targeting = rom.read_byte(data_start + 14)
        item_properties = rom.read_byte(data_start + 19)
        effect_strength = rom.read_byte(data_start + 20)
        caused_conditions1 = rom.read_byte(data_start + 21)
        caused_conditions2 = rom.read_byte(data_start + 22)
        caused_conditions3 = rom.read_byte(data_start + 23)
        caused_conditions4 = rom.read_byte(data_start + 24)
        special_action = rom.read_byte(data_start + 27)
        price = rom.read_short(data_start + 28)
        attributes = {}
        if type != InventoryItemType.Item.value:
            msg = 'Invalid item type in ROM (got %s, expected %s)'
            raise ValueError(msg % (type, InventoryItemType.Item))
        attributes['number'] = number
        attributes['name'] = name
        attributes['type'] = InventoryItemType.Item
        attributes['effect_strength'] = effect_strength
        attributes['price'] = price
        enum_params = [
            ('usability', usability, InventoryItemUsability),
            ('caused conditions 1', caused_conditions1, Condition1, 'causes_'),
            ('caused conditions 2', caused_conditions2, Condition2, 'causes_'),
            ('caused conditions 3', caused_conditions3, Condition3, 'causes_'),
            ('caused conditions 4', caused_conditions4, Condition4, 'causes_'),
            ('item properties', item_properties, ItemProperty),
            ('targeting', targeting, Targeting, 'targets_'),
        ]
        for args in enum_params:
            attributes.update(get_matching_values_as_params(*args))
        attributes['special_action'] = get_enum_member(
            'special action', ItemSpecialAction, special_action)
        if 'no_item_property' in attributes:
            del attributes['no_item_property']
        return cls(**attributes)

class Items(TypedObjectContainer):

    ObjectCount = 256
    ObjectType = Item
    Name = 'Items'

    @classmethod
    def get_object_from_rom(cls, rom, n):
        item_location = rom.ItemDataOffset + (n * InventoryItem.DataSize)
        item_type = rom.read_byte(item_location) & 0x0F
        if item_type == InventoryItemType.Tool.value:
            return Tool.from_rom(rom, n)
        if item_type == InventoryItemType.Weapon.value:
            return Weapon.from_rom(rom, n)
        if item_type == InventoryItemType.Armor.value:
            return Armor.from_rom(rom, n)
        if item_type == InventoryItemType.Shield.value:
            return Shield.from_rom(rom, n)
        if item_type == InventoryItemType.Hat.value:
            return Hat.from_rom(rom, n)
        if item_type == InventoryItemType.Relic.value:
            return Relic.from_rom(rom, n)
        if item_type == InventoryItemType.Item.value:
            return Item.from_rom(rom, n)
        raise ValueError('Unknown item type in ROM (got %s)' % (type))
