#!/usr/bin/env python

import pprint

from ff6.data import *
from ff6.ff6rom import FF6ROM
from ff6.save_game import SaveGame

ROM_FILENAME = 'ff6.rom'
SAVE_FILENAME = 'ff6.srm'

def get_rom(rom_filename):
    rom = FF6ROM.from_file(rom_filename)
    rom.deserialize()
    return rom

def test_monsters(rom_filename):
    rom = get_rom(rom_filename)
    for n, monster in enumerate(rom.monsters):
        print(n, pprint.pformat(monster))

def test_items(rom_filename):
    rom = get_rom(rom_filename)
    for n, item in enumerate(rom.inventory_items):
        print(n, pprint.pformat(item))

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
    for n, magic in enumerate(rom.magic):
        print(n, pprint.pformat(magic))

def test_hp_per_level(rom_filename):
    rom = get_rom(rom_filename)
    print(rom.hp_per_level)

def test_mp_per_level(rom_filename):
    rom = get_rom(rom_filename)
    print(rom.mp_per_level)

def test_xp_per_level(rom_filename):
    rom = get_rom(rom_filename)
    print(rom.xp_per_level)

def test_morph_packages(rom_filename):
    rom = get_rom(rom_filename)
    for n, morph_package in enumerate(rom.morph_packages):
        print(n, pprint.pformat(morph_package))

def test_character_starts(rom_filename):
    rom = get_rom(rom_filename)
    for n, character_start in enumerate(rom.character_starts):
        print(n, pprint.pformat(character_start))

def compare_roms(rom_filename):
    rom1 = get_rom(rom_filename)
    rom2 = get_rom(rom_filename)
    rom2.serialize()
    assert rom1 == rom2
    print('ROMs equal')

def read_save(rom_filename, save_filename):
    rom = FF6ROM.from_file(rom_filename)
    rom.deserialize()
    save = SaveGame.from_file(0, rom, save_filename)
    save.deserialize()
    print(save.gold)
    print(save.game_time)
    print(save.steps)
    for character in save.characters:
        print('%r' % (character))
    for slot in save.inventory_item_slots:
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
    # print(rom.espers[26].spell1.caused_conditions)
    for n, esper in enumerate(rom.espers):
        print(n, pprint.pformat(esper))

def test_natural_magic(rom_filename):
    rom = get_rom(rom_filename)
    for natural_magic in rom.terra_natural_magic:
        pprint.pprint(natural_magic.to_dict())
    for natural_magic in rom.celes_natural_magic:
        pprint.pprint(natural_magic.to_dict())

def test_bushido_levels(rom_filename):
    rom = get_rom(rom_filename)
    for bushido_level in rom.bushido_levels:
        print(bushido_level)

def test_blitz_levels(rom_filename):
    rom = get_rom(rom_filename)
    for blitz_level in rom.blitz_levels:
        print(blitz_level)

def main():
    # read_save(ROM_FILENAME, SAVE_FILENAME)
    # test_monsters(ROM_FILENAME)
    # test_items(ROM_FILENAME)
    # # compare_roms(ROM_FILENAME)
    # test_blitzes(ROM_FILENAME)
    test_bushidos(ROM_FILENAME)
    # test_magic(ROM_FILENAME)
    # test_hp_per_level(ROM_FILENAME)
    # test_mp_per_level(ROM_FILENAME)
    # test_xp_per_level(ROM_FILENAME)
    # test_morph_packages(ROM_FILENAME)
    # test_character_starts(ROM_FILENAME)
    # test_mapping(ROM_FILENAME)
    # test_espers(ROM_FILENAME)
    # test_natural_magic(ROM_FILENAME)
    # test_bushido_levels(ROM_FILENAME)
    # test_blitz_levels(ROM_FILENAME)

main()
