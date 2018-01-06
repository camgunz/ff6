#!/usr/bin/env python

import pprint

from ff6.data import *
from ff6.patch import Patch
from ff6.ff6rom import FF6ROM
from ff6.save_game import SaveGame

ROM_FILENAME = 'ff6.rom'
SAVE_FILENAME = 'ff6.srm'
PATCH_FILENAMES = (
    'Patches/harden-narshe-fights.ips',
    'Patches/update-magitek.ips',
    'Patches/harder_rats.ips',
    'Patches/whelk-fight.ips',
    'Patches/whelk-fight-dialogue.ips',
    'Patches/edit-were-rats-slightly.ips',
    'Patches/harden-solo-terra-narshe-cave-fights.ips',
    'Patches/more-magitek-edits.ips',
    'Patches/buff-lobo-slightly.ips',
    'Patches/make-guard-faster.ips',
    # 'Patches/expand-battle-script-space.ips',
    'Patches/increase-encounter-rate-in-solo-terra-narshe-cave.ips',
    'Patches/buff-marshal.ips'
)

def get_rom(rom_filename):
    rom = FF6ROM.from_file(rom_filename)
    rom.deserialize()
    return rom

def get_patch(patch_filename):
    return Patch.from_file(patch_filename, False, False, '')

def get_save_game(rom, save_filename, slot):
    save_game = SaveGame.from_file(save_filename, rom, slot)
    save_game.deserialize()
    return save_game

def test_monsters(rom_filename):
    rom = get_rom(rom_filename)
    for monster in rom.monsters:
        pprint.pprint(monster.to_dict())

def test_items(rom_filename):
    rom = get_rom(rom_filename)
    for item in rom.inventory_items:
        pprint.pprint(item.to_dict())

def test_blitzes(rom_filename):
    rom = get_rom(rom_filename)
    for blitz in rom.blitzes:
        pprint.pprint(blitz.to_dict())

def test_bushidos(rom_filename):
    rom = get_rom(rom_filename)
    for bushido in rom.bushidos:
        pprint.pprint(bushido.to_dict())

def test_magic(rom_filename):
    rom = get_rom(rom_filename)
    for magic in rom.magic:
        pprint.pprint(magic.to_dict())

def test_hp_per_level(rom_filename):
    print(get_rom(rom_filename).hp_per_level)

def test_mp_per_level(rom_filename):
    print(get_rom(rom_filename).mp_per_level)

def test_xp_per_level(rom_filename):
    print(get_rom(rom_filename).xp_per_level)

def test_morph_packages(rom_filename):
    rom = get_rom(rom_filename)
    for morph_package in rom.morph_packages:
        pprint.pprint(morph_package.to_dict())

def test_character_starts(rom_filename):
    rom = get_rom(rom_filename)
    for character_start in rom.character_starts:
        pprint.pprint(character_start.to_dict())

def compare_roms(rom_filename):
    rom1 = get_rom(rom_filename)
    rom2 = get_rom(rom_filename)
    rom2.serialize()
    assert rom1 == rom2
    print('ROMs equal')

def read_save(rom_filename, save_filename):
    rom = get_rom(rom_filename)
    save_game = get_save_game(rom, save_filename, 0)
    print(save_game.gold)
    print(save_game.game_time)
    print(save_game.steps)
    for character in save_game.characters:
        pprint.pprint(character.to_dict())
    for slot in save_game.inventory_item_slots:
        if slot.id != 255 or slot.count != 0:
            print(slot)

def test_mapping(rom_filename):
    rom = get_rom(rom_filename)
    assert (rom.character_starts[0].armor.physical_defense ==
            rom.inventory_items[132].physical_defense)
    rom.character_starts[0].armor.physical_defense = 80
    assert (rom.character_starts[0].armor.physical_defense ==
            rom.inventory_items[132].physical_defense)
    rom.inventory_items[132].physical_defense = 28
    assert (rom.character_starts[0].armor.physical_defense ==
            rom.inventory_items[132].physical_defense)
    repr(rom.inventory_items)
    assert rom.character_starts[0].armor == rom.inventory_items[132]

def test_espers(rom_filename):
    rom = get_rom(rom_filename)
    for esper in rom.espers:
        pprint.pprint(esper.to_dict())
        if esper.level_bonus:
            pprint.pprint(esper.level_bonus.to_dict())

def test_natural_magic(rom_filename):
    rom = get_rom(rom_filename)
    for natural_magic in rom.terra_natural_magic:
        pprint.pprint(natural_magic.to_dict())
    for natural_magic in rom.celes_natural_magic:
        pprint.pprint(natural_magic.to_dict())

def test_patch(patch_filename):
    patch = get_patch(patch_filename)
    for command, args in patch:
        print(command, (hex(args[0]), args[1], args[2]))

def test_shops(rom_filename):
    rom = get_rom(rom_filename)
    for shop in rom.shops:
        pprint.pprint(shop.to_dict())

def test_skean_attacks(rom_filename):
    rom = get_rom(rom_filename)
    for skean_attack in rom.skean_attacks:
        pprint.pprint(skean_attack.to_dict())

def test_dances(rom_filename):
    print(get_rom(rom_filename).dances)

def test_dance_attacks(rom_filename):
    rom = get_rom(rom_filename)
    for dance_attack in rom.dance_attacks:
        pprint.pprint(dance_attack.to_dict())

def test_slot_attacks(rom_filename):
    rom = get_rom(rom_filename)
    for slot_attack in rom.slot_attacks:
        pprint.pprint(slot_attack.to_dict())

def test_magitek_attacks(rom_filename):
    rom = get_rom(rom_filename)
    for magitek_attack in rom.magitek_attacks:
        pprint.pprint(magitek_attack.to_dict())

def test_lore_attacks(rom_filename):
    rom = get_rom(rom_filename)
    for lore_attack in rom.lore_attacks:
        pprint.pprint(lore_attack.to_dict())

def test_monster_attacks(rom_filename):
    rom = get_rom(rom_filename)
    for monster_attack in rom.monster_attacks:
        pprint.pprint(monster_attack.to_dict())

def test_desperation_attacks(rom_filename):
    rom = get_rom(rom_filename)
    for desperation_attack in rom.desperation_attacks:
        pprint.pprint(desperation_attack.to_dict())

def test_misc_attacks(rom_filename):
    rom = get_rom(rom_filename)
    for misc_attack in rom.misc_attacks:
        pprint.pprint(misc_attack.to_dict())

def test_magitek_menu(rom_filename):
    rom = get_rom(rom_filename)
    for magitek_menu_slot in rom.magitek_menu:
        pprint.pprint(magitek_menu_slot.to_dict())

def test_battle_dialogues(rom_filename):
    rom = get_rom(rom_filename)
    for battle_dialogue in rom.battle_dialogues1:
        pprint.pprint(battle_dialogue.to_dict())
    for battle_dialogue in rom.battle_dialogues2:
        pprint.pprint(battle_dialogue.to_dict())

def test_battle_messages(rom_filename):
    rom = get_rom(rom_filename)
    for battle_message in rom.battle_messages:
        pprint.pprint(battle_message.to_dict())

def main():
    read_save(ROM_FILENAME, SAVE_FILENAME)
    test_monsters(ROM_FILENAME)
    test_items(ROM_FILENAME)
    # compare_roms(ROM_FILENAME)
    test_blitzes(ROM_FILENAME)
    test_bushidos(ROM_FILENAME)
    test_magic(ROM_FILENAME)
    test_hp_per_level(ROM_FILENAME)
    test_mp_per_level(ROM_FILENAME)
    test_xp_per_level(ROM_FILENAME)
    test_morph_packages(ROM_FILENAME)
    test_character_starts(ROM_FILENAME)
    test_mapping(ROM_FILENAME)
    test_espers(ROM_FILENAME)
    test_natural_magic(ROM_FILENAME)
    for patch_filename in PATCH_FILENAMES:
        print(patch_filename)
        test_patch(patch_filename)
        print('')
    test_shops(ROM_FILENAME)
    test_skean_attacks(ROM_FILENAME)
    test_dance_attacks(ROM_FILENAME)
    test_slot_attacks(ROM_FILENAME)
    test_magitek_attacks(ROM_FILENAME)
    test_lore_attacks(ROM_FILENAME)
    test_monster_attacks(ROM_FILENAME)
    test_desperation_attacks(ROM_FILENAME)
    test_misc_attacks(ROM_FILENAME)
    test_magitek_menu(ROM_FILENAME)
    test_dances(ROM_FILENAME)
    test_battle_dialogues(ROM_FILENAME)
    test_battle_messages(ROM_FILENAME)

main()
