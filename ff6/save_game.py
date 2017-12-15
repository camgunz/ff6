import struct

from datetime import timedelta

from ff6.typed_object import *

"""
        public const int SRM_SLOT_SIZE = 0xA00;
        public const int NEXT_CHARACTER_OFFSET = 37;
        public const int NEXT_CHARACTER_MAGIC_OFFSET = 54;
        private const int CHARACTER_OFFSET = 0x0;
        private const int KNOWN_MAGIC_OFFSET = 0x46E;
        private const int ESPER_OFFSET = 0x469;
        private const int SWDTECH_OFFSET = 0x6F7;
        private const int BLITZ_OFFSET = 0x728;
        private const int LORE_OFFSET = 0x729;
        private const int DANCE_OFFSET = 0x74C;
        private const int RAGE_OFFSET = 0x72C;
        private const int INVENTORY_ITEM_ID_OFFSET = 0x269;
        private const int INVENTORY_ITEM_COUNT_OFFSET = 0x369;
        private const int GOLD_OFFSET = 0x260;
        private const int STEPS_OFFSET = 0x266;
        private const int NUMBER_OF_SAVE_OFFSET = 0x7C7;
        private const int MAP_XY_OFFSET = 0x960;
        private const int AIRSHIP_XY_OFFSET = 0x962;
        /// Offset to Airship settings flag
        ///  bit 0: WoR: 0=sad song, 1=norm.song
        ///  bit 1: airship visibility
        ///  bit 2: 1=coin toss cutscean/crashed
        ///  bit 3: start w/ Veldt Music
        ///  bits 4, 5, 6: ?
        ///  bit 7: 1=is a save point
        private const int AIRSHIP_SETTINGS_OFFSET = 0x8B7;
        private const int GAME_TIME_OFFSET = 0x263;
    looks like active party and positions are handled in the area 2646 and 2469

const unsigned char BTL_MN1 =0;
const unsigned char BTL_MN2 =1;
const unsigned char BTL_MN3 =2;
const unsigned char BTL_MN4 =3;

const unsigned char EQ_SWRD =0;
const unsigned char EQ_SHLD =1;
const unsigned char EQ_HELM =2;
const unsigned char EQ_ARMR =3;
const unsigned char EQ_REL1 =4;
const unsigned char EQ_REL2 =5;

const unsigned char STAT_A  =0;
const unsigned char STAT_B  =1;
const unsigned char VIGOR   =2;
const unsigned char SPEED   =3;
const unsigned char STAMINA =4;
const unsigned char MAGPOW  =5;
const unsigned char ESPER   =6;
const unsigned char PROF1   =7;
const unsigned char PROF2   =8;

typedef unsigned char data;
const long maxdata = 36000lu;
const int  max_slots = 3;
const int  max_magic = 54;          // 54 spells
const int  slot1_offset = 0x0;
const int  slot2_offset = 0xA00;
const int  slot3_offset = 0x1400;
const int  slot_lenght = 0xA00;

// 16 official players + 2 customizable players
const int  nb_players_menu = 18;
const int  nb_players = 16;         // 16 official players
const int  nb_mgc_users = 12;       // 12 magic users

// the first 592 bytes cover character's abilities
const int  car_info_lenght = 37;    // 37 bytes X 16 players

const int  raster_offset  = 592;    // setup of active party(ies)
const int  gold_offset  = 608;      // gold pieces
const int  gtime_offset = 611;      // game time
const int  steps_offset = 614;      // steps
const int  itm_lst_offset = 617;    // possessed items
const int  itm_qty_offset = 873;    // quantity of items
// possessed espers
const int  esp_list_offset = 1129;  // four bytes, switch on/off
const int  magic_offset = 1134;     // learn % of magic X 12

// not decoded 1782, 1784 thru 1831

const int  swrdt_offset = 1783;     // swordtech abil.
const int  blitz_offset = 1832;     // blitz abil.
const int  lores_offset = 1833;     // lores abil.
const int  rages_offset = 1836;     // rages abil.
const int  dance_offset = 1868;     // dance abil.

const int  nb_saves_offset = 1991;  // number of saves, CzarDragon credit
const int  act_memb_offset = 2268;  // active members (shop selection), 2 bytes, CzarDragon credits, lsb byte1 is Terra
const int  act_memb2_offset = 2270; // active members (airship selection), 2 bytes, lsb byte1 is Terra
const int  map_xy_offset = 2400; // XY location on overworld, 2 bytes, CzarDragon credit
const int  ship_xy_offset = 2402;   // XY location of airship, 2 bytes, CzarDragon credit


// not decoded 1869 thru end (2560)

// decoded but not implemented yet:
const int  actgrp_offset = 1133;    // active group, CzarDragon credit


// sword tech name for FF6 CzarDragon credit
const int  swtk_name_offset = 1784; // 48 bytes

const int  btlspeed_offset = 1869;  // mess. and btl speed, 3bits: 6->4 lsb=btl, 2->0 msb=mess
                        // value from 1 to 6 = 0 to 5
                        // bit 7 = cmd.set, 1 = short; bit 3 = bat. mode, 1 = wait
const int  wallpaper_offset = 1870; // forest, chocobo, stone, ect., bit 0 -> 3
                        // gauge off, sound mono, cursor memory, reequip empty, bit 4->7 set to 1

const int  dummy1_offset = 1871;    // ????     when dummy1 to 5 + config1 is set to ff, all key becomes down key
const int  dummy2_offset = 1872;    // ????
const int  dummy3_offset = 1873;    // ????
const int  dummy4_offset = 1874;    // ????
const int  dummy5_offset = 1875;    // ????
const int  config1_offset = 1876;   // about single/multiple cntrl, mag. order, color "arrow" pointer
const int  fontcolor1_offset = 1877; // 00 = blue, red doesnt work
const int  fontcolor2_offset = 1878; //

// this is probably coded on 12 bits, it won't be tested yet...
const int  border1wp1_offset = 1879; // 1st color pntr, 00 = is blue (border part 1, wallpaper no 1)
const int  border2wp1_offset = 1880; // " 00 = is red
const int  border3wp1_offset = 1881; // 2nd color pointer
const int  border4wp1_offset = 1882; // 2nd color pointer
const int  border5wp1_offset = 1883; // 3nd color pointer
const int  border6wp1_offset = 1884; // 3rd color pointer
const int  border7wp1_offset = 1885; // 4rd color pointer
const int  border8wp1_offset = 1886; // 4rd color pointer
const int  border9wp1_offset = 1887; // 5rd color pointer
const int  border10wp1_offset = 1888; // 5rd color pointer
const int  border11wp1_offset = 1889; // 6rd color pointer
const int  border12wp1_offset = 1890; // 6rd color pointer
const int  border13wp1_offset = 1891; // 7th color pointer
const int  border14wp1_offset = 1892; // 7th color pointer


// 1893 thru 1906 wallparer 2
// 1907 thru 1920 wallparer 3
// 1921 thru 1934 wallparer 4
// 1935 thru 1948 wallparer 5
// 1949 thru 1962 wallparer 6
// 1963 thru 1976 wallparer 7
// 1977 thru 1990 wallparer 8
// those "illegal" wp may just be data representing something else in the game...


const int  test_offset = 2404;  // 2403,2418 sp warp ; 2418,1428 sprites
const int  test2_offset = 2405; // 2495,2559

const unsigned char tester = 0x76;

// random, semi-decoded data or not implemented
const int  airship_offset = 2231;   // Lord J, CzarDragon credit
                        // bit 0: WoR: 0=sad song, 1=norm.song
                        // bit 1: airship visibility
                        // bit 2: 1==coin toss cutscean/crashed
                        // bit 3: start w/ Veldt Music
                        // bit 4: ?
                        // bit 5: ?
                        // bit 6: ?
                        // bit 7: 1=is a save point
const int  sound_at_startup_offset = 2230; // 99$ = save pnt snd
const int  rare_items_offset = 2234;       // 3 bytes, rare items: 24 items, list is 20 long in game, 4 items are "illegal"

const int  world_offset = 2404;     // offset 2405 was set to 32
                        // 00 is in balance world, 01 is in world of ruin,
                        // 02 air ship, serpent trench????
                        // 03 biz, enemies, tent south, warp to floating isl. cinema, ect., airship battle
                        // 04 tomb battle bkgnd, no warp, 05 no nothing, 06 "semi" stalled airship
                        // 07 airship casino deck,
                        // 09 team splitup (banon) scenario, 0a, "fake" airship
                        // 0b overwold balance, sabin scenario or doesnt affect?
                        // 0c casino deck fake airship,
                        // 0d end of world setup on airship
                        // 0e,10 chocobo stable, warp to last caverm
                        // 0f s.fig house warp, blocked
                        // 75 imperial camp


const int  overworld_palette = 2416;// not confirmed yet
const int  special_warp_offset = 2495;
                        // 00 = normal, 01 = lete river scenario w/ Banon!,
                        // 03,02,3f,80,8f,99 = freeze,
                        // 88 = walk around in spiral!,9f = air ship takeoff +freeze
                        // 7f = crash

const int  x1_sp_offset = 2496;     // x offset at save point, add = right off., subs = left off.
const int  y1_sp_offset = 2497;     // y offset at save point, add = down off., subs = up off.

offset 0x1cb9(slot 3), bit 4 ON force Narshe song
offset 0x1cad(slot 3), bit 7 ON make control of AS avail.
offset 0x1cd8(slot 3), bit 1 ON make "cinema black bar" in town
offset 0x1c94(slot 3), bit 7 ON make airship change to FALCON
offset 0x1c93(slot 3), bit 6 ON make continent disapear (WOB)
offset 0x1c93(slot 3), bit 7 ON Floating continent unselectable from AS
           but if bit 6 is OFF and 7 OFF, still unselectable
offset 0x08ed(slot 1), the way Cid's going to bed!!
offset 0x09d0(slot 1), cid's health on deserted island
offset 0x0896(slot 1), bit 3 ON cid's fine, stay on bed
offset 0x08ec(slot 1), bit 7 OFF cid is gone (hacking), cid is healthy (normal)
*/
}
"""

class Character(TypedObject):

    NameSize = 6
    DataSize = 37

    @property
    def data_offset(self):
        return self.DataOffset + (self.DataSize * self.number)

    def _build_fields(self):
        return super()._build_fields() + (
            EnumField(self, 'actor', Actor, self.data_offset + 0),
            EnumField(self, 'character', Character, self.data_offset + 1),
            StrField(self, 'name', 6, self.data_offset + 2),
            U8Field(self, 'level', self.data_offset + 8),
            U16Field(self, 'current_hp', self.data_offset + 9),
            U16Field(self, 'max_hp', self.data_offset + 11),
            U16Field(self, 'current_mp', self.data_offset + 3),
            U16Field(self, 'max_mp', self.data_offset + 15),
            U24Field(self, 'experience', self.data_offset + 17),
        )

class SaveGame(TypedObject):

    MaxSize = 0xA00

    CharacterOffset = 0x0
    PartyInfoOffset = 0x250

    GoldOffset = 0x260
    GameTimeOffset = 0x263
    StepsOffset = 0x266
    InventoryItemIDOffset = 0x269
    InventoryItemCountOffset = 0x369
    EsperOffset = 0x469
    ActiveGroup = 0x46D # ???
    MagicOffset = 0x46E
    BushidoOffset = 0x6F7
    BushidoNameOffset = 0x6F8
    BlitzOffset = 0x728
    LoreOffset = 0x729
    RageOffset = 0x72C
    DanceOffset = 0x74C
    SaveCountOffset = 0x7C7
    AirshipSettingsOffset = 0x8B7
    ShopActiveMembersOffset = 0x8DC
    AirshipActiveMembersOffset = 0x8DE
    MapLocationOffset = 0x960
    AirshipLocationOffset = 0x962
    WorldInfoOffset = 0x964
    PartyOffset = 0xA56

    MagicCount = 54
    BushidoCount = 8
    BushidoNameSize = 6
    CharacterInfoSize = 37
    CharacterCount = 16
    MainCharacterCount = 12
    InventoryItemCount = 256

    def __init__(self, rom, data):
        self._rom = rom
        self._data = data
        self.items = self._load_items()
        self.gold = self._load_gold()
        self.game_time = self._load_game_time()
        self.steps = self._load_steps()

    @classmethod
    def from_file(cls, rom, file_name):
        with open(file_name, 'rb') as fobj:
            return cls(rom, fobj.read())

    def _load_items(self):
        fmt = '%dB' % (self.InventoryItemCount)
        ids = struct.unpack_from(fmt, self._data, self.InventoryItemIDOffset)
        counts = struct.unpack_from(
            fmt,
            self._data,
            self.InventoryItemCountOffset
        )
        return list(zip([self._rom.items[id] for id in ids], counts))

    def _load_gold(self):
        bytes = struct.unpack_from('3B', self._data, self.GoldOffset)
        print(bytes)
        return bytes[2] << 16 | bytes[1] << 8 | bytes[0]

    def _load_game_time(self):
        bytes = struct.unpack_from('3B', self._data, self.GameTimeOffset)
        print(bytes)
        return timedelta(hours=bytes[0], minutes=bytes[1], seconds=bytes[2])

    def _load_steps(self):
        bytes = struct.unpack_from('3B', self._data, self.StepsOffset)
        print(bytes)
        return bytes[2] << 16 | bytes[1] << 8 | bytes[0]

    def _load_characters(self):
        

    def _build_fields(self):
        return super()._build_fields() + (
            EnumField(self, 'actor', Actor, self.data_offset + 0),
            EnumField(self, 'character', Character, self.data_offset + 1),
            StrField(self, 'name', 6, self.data_offset + 2),
            U8Field(self, 'level', self.data_offset + 8),
            U16Field(self, 'current_hp', self.data_offset + 9),
            U16Field(self, 'max_hp', self.data_offset + 11),
            U16Field(self, 'current_mp', self.data_offset + 3),
            U16Field(self, 'max_mp', self.data_offset + 15),
            U24Field(self, 'experience', self.data_offset + 17),
        )

