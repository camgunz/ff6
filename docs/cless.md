Final Fantasy VI (US) ROM hacking guide `©*´¯``·.¸¸.·´¯``·.¸¸.·´¯``·->`

======================================
FINAL FANTASY VI (US) ROMHACKING GUIDE
======================================
Version .6
Created by [Cless](mailto:tetsuya@crosswinds.net)[http://surf.to/starocean](http://surf.to/starocean)

Table of Contents

[Part 1: Intro and notes](#part1)
[Part 2: Revision History](#part2)
[Part 3: Credits
](#part3)[Part 4: Items](#part4)
 [Weapons](#item1)
 [Armor/Relics](#item2)
 [Items](#item3)
[Part 5: Monsters](#part5)
 [Status](#mons1)
 [Items](#mons2)
 [Magic/Attacks](#mons3)
  [AI data](#mons31) (...)
 [Control](#mons4)
 [Sketch](#mons5)
 [Rage](#mons6)
[Part 6: Enemy battle formations](#part6)
 [Misc data for each formation](#ebf1)
 [Magic Points per battle](#ebf2)
[Part 7: Collosseum](#part7)
[Part 8: Espers](#part8)
[Part 9: Magic](#part9)
[Part 10: Shops](#part10)
[Part 11: Ragnarok Metamorphosis](#part11)
[Part 12: Character Start-up](#part12)
[Part 13: Exp needed for level up](#part13)
[Part 14: HP gained at level up](#part14)
[Part 15: MP gained at level up](#part15)
[Part 16: Music pointers](#part16) (VERY INCOMPLETE)
[Part 17: Text stuff](#part17)
[Part 18: Palettes](#part18)
 [Battle sprite palette pointers](pal1)
 [Battle sprite palettes](pal2)
 [Out of battle sprite palettes](pal3)
 [Wallpaper pallete](pal4)
[Part 19: Stuff](#part19)
[Part 20: Byte Values](#part20)
[Part 21: Help](#part21)


* * *

**Part 1: Intro and notes**

This file itself was originally just made as a reference for myself while creating my gameplay hack of Final Fantasy VI, titled 'Final Fantasy VI Hard Type'; I then decided that I would clean it up, find some new datas that weren't of any use to me and then release it to (and hopefully overwhelm :P) the public. One reason I wanted to release it so that there could be more GAMEPLAY hacks out there, because I feel there aren't enough and, and frankly, I'm kind of sick of simple graphic/text hacks. With all that's included in this file, hopefully soon there will be some bad-ass hacks of this game, since there is so much data that can be tinkered with. Yet, there's still quite a bit of stuff I'm trying to find (see part 21!).

This file was created in HTML because I felt it would be too tedious to navigate through as plain text. Either way, I prefer documents written in HTML than any standard text format anyways. So enjoy all the nifty quick jumps...



* * *

**Part 2: Revision History**

12/20/99

-A pre-release. I'm releasing this earlier than I had planned. Many bytes are not figured out right now (but they'd otherwise be figured out if I had released it at a planned time.). Some sections might not even have anything entered in them. I'm releasing this almost as is (with a bit of minor editing). Some things might not have the right formatting. You're getting what you paid for. Bah humbug.

I released this early because I'm currently \_not\_ in a ROM hacking mood right now and only god knows when I will be again (I'd rather be tinkering with [VERGE 2](http://verge-rpg.com/) right now, and I'm also getting Tales of Phantasia (PSX remake), Final Fantasy VIII, Final Fantasy Anthology OR Suikdoen II, Thousand Arms and LUNAR: Silver Star Story Complete, so count 'em, that's FIVE new nice long RPGs for Christmas, so I'll be busy for awhile. What all that means is that there would've been a million more delays before I felt like getting full real deal out).

* * *

**Part 3: Credits**

**Roto**\- Found Item data, Monster data (stats and steal/drop data), Shop data, and the Esper data. Also figured out what some bytes pertained to in the data he found.

**CzarDragon**\- Found Ragnarok Metamorphosis data, and Enemy Formations data.

**Master ZED**\- Gave me some pointers on the tenth byte of the magic data, and a VERY VERY big thanks for the major help with the enemy magic! (found the AI script -pointers- and is doing well in helping me crack the AI data format!)

**Lord J**\- Yes, I stole some of the wonderful info from your page! Includes some byte info on some things I haven't figured out yet, all the palette data here, quite a bit more stuff I can't remember...

**Me (Cless)**\- Created the file, Found monster data (Control, Rage, and AI script data), Colosseum data, Magic data, character Start-up data, character Desperation attack data, Exp needed for level up data, figured out most of the byte values, and figured out the rest of what bytes pertained to what.


* * *

**Part 4: Items data**

This is really cool. If you know what you are doing, you can practically create new items, at the cost of changing another. Also, some bytes are only used by certain item types, I think.

Pre-release note: Umm, some of the byte descriptions for some bytes may be wrong. I really haven't messed with this stuf much.

Data (185200 - ??????)

Structure: 30 bytes per item


Weapons

1: Item type
2: [Who equips #1](#equip1)
3: [Who equips #2](#equip2)
4: (nothing?)
5: (nothing?)
6: Relic effect 1
7: ?
8: Relic effect 2
9: Status Effect
10: ?
11: ?
12: Relic effect 3
13: ?
14: ?
15: ?
16: [Attack elements](#elem)
17: [Speed (first half), Vigor (second half 18:](#vigor) [Mag.Pwr (first half), Stamina (second half)](#vigor)
19: ?
20: [Abilities can be used](#abil)
21: Bat.Pwr
22: Hit % rate
23: [Absorb HP (armor only)](#elem)
24: [No effect (armor only)](#elem)
25: [Weak point (armor only)](#elem)
26: Status effects (?) if used (armor only?)
27: [MBlock % (first half), Evade % (second half)](#evade)
28: ?
29: Lo price
30: Hi price

Armors/Relics

1: Item type
2: [Who equips #1](#equip1)
3: [Who equips #2](#equip2)
4: Spell Learn Rate
5: [Magic spell to learn](#magic)
6: ?
7: ?
8: ?
9: Status Effect
10: ?
11: ?
12: Relic effect
13: ?
14: ?
15: ?
16: 50% Damage
17: Speed (first half), Vigor (second half)
18: Mag.Pwr (first half), Stamina (second half)
19: ?
20:
21: Defense
22: Mag.Def
23: Absorb HP
24: No effect
25: Weak point
26: Status effects (?) if used
27: [MBlock % and Evade %](#evade)
28: ?
29: Lo price
30: Hi price

Items

1: Item type
2: [Who equips #1](#equip1)
3: [Who equips #2](#equip2)
4:
5:
6: ?
7: ?
8: ?
9: Status Effect
10: ?
11: ?
12: Relic effect
13: ?
14: ?
15: ?
16:
17:
18:
19: ?
20:
21:
22:
23:
24:
25:
26: Status effects (?) if used (armor only?)
27:
28: ?
29: Lo price
30: Hi price



Item locations:

185200: Dirk
18521E: MithrilKnife
18523C: Guardian
18525A: Air Lancet
185278: ThiefKnife
185296: Assassin
1852B4: Man Eater
1852D2: SwordBreaker
1852F0: Graedus
18530E: ValiantKnife
18532C: MithrilBlade
18534A: RegalCutlass
185368: Rune Edge
185386: Flame Sabre
1853A4: Blizzard
1853C2: ThunderBlade
1853E0: Epee
1853FE: BreakBlade
18541C: Drainer
18543A: Enhancer
185458: Crystal
185476: Falchion
185494: Soul Sabre
1854B2: Ogre Nix
1854D0: Excalibur
1854EE: Scimitar
18550C: Illumina
18552A: Ragnarok
185548: Atma Weapon
185566: Mithril Pike
185584: Trident
1855A2: Stout Spear
1855C0: Partisan
1855DE: Pearl Lance
1855FC: Gold Lance
18561A: Aura Lance
185638: Imp Halberd
185656: Imperial
185674: Kodachi
185692: Blossom
1856B0: Hardened
1856CE: Striker
1856EC: Stunner
18570A: Ashura
185728: Kotetsu
185746: Forged
185764: Tempest
185782: Murasame
1857A0: Aura
1857BE: Strato
1857DC: Sky Render
1857FA: Heal Rod
185818: Mithril Rod
185836: Fire Rod
185854: Ice Rod
185872: Thunder Rod
185890: Poison Rod
1858AE: Pearl Rod
1858CC: Gravity Rod
1858EA: Punisher
185908: Magus Rod
185926: Chocobo Brsh
185944: DaVinci Brsh
185962: Magical Brsh
185980: Rainbow Brsh
18599E: Shuriken
1859BC: Ninja Star
1859DA: Tack Star
1859F8: Flail
185A16: Full Moon
185A34: Morning Star
185A52: Boomerang
185A70: Rising Sun
185A8E: Hawk Eye
185AAC: Bone Club
185ACA: Sniper
185AE8: Wing Edge
185B06: Cards
185B24: Darts
185B42: Doom Darts
185B60: Trump
185B7E: Dice
185B9C: Fixed Dice
185BBA: MetalKnuckle
185BD8: MithrilClaw
185BF6: Kaiser
185C14: Poison Claw
185C32: Fire Knuckle
185C50: Dragon Claw
185C6E: Tiger Fangs
185C8C: Buckler
185CAA: Heavy Shld
185CC8: Mithril Shld
185CE6: Gold Shld
185D04: Aegis Shld
185D22: Diamond Shld
185D40: Flame Shld
185D5E: Ice Shld
185D7C: Thunder Shld
185D9A: Crystal Shld
185D88: Genji Shld
185DD6: TortoiseShld
185DF4: Cursed Shld
185E12: Paladin Shld
185E30: Force Shld
185E4E: Leather Hat
185E6C: Hair Band
185E8A: Plumed Hat
185EA8: Beret
185EC6: Magus Hat
185EE4: Bandana
185F02: Iron Helmet
185F20: Coronet
185F3E: Bard's Hat
185F5C: Green Beret
185F7A: Head Band
185F98: Mithril Helm
185FB6: Tiara
185FD4: Gold Helmet
185FF2: Tiger Mask
186010: Red Cap
18602E: Mystery Veil
18604C: Circlet
18606A: Regal Crown
186088: Diamond Helm
1860A6: Dark Hood
1860C4: Crystal Helm
1860E2: Oath Veil
186100: Cat Hood
18611E: Genji Helmet
18613C: Thornlet
18615A: Titanium
186178: LeatherArmor
186196: Cotton Robe
1861B4: Kung Fu Suit
1861D2: Iron Armor
1861F0: Silk Robe
18620E: Mithril Vest
18622C: Ninja Gear
18624A: White Dress
186268: Mithril Mail
186286: Gaia Gear
1862A4: Mirage Vest
1862C2: Gold Armor
1862E0: Power Sash
1862FE: Light Robe
18631C: Diamond Vest
18633A: Red Jacket
186358: Force Armor
186376: DiamondArmor
186394: Dark Gear
1863B2: Tao Robe
1863D0: Crystal Mail
1863EE: Czarina Gown
18640C: Genji Armor
18642A: Imp's Armor
186448: Minerva
186466: Tabby Suit
186484: Chocobo Suit
1864A2: Moogle Suit
1864C0: Nutkin Suit
1864DE: BehemothSuit
1864FC: Snow Muffler
18651A: NoiseBlaster
186538: Bio Blaster
A5: Flash
A6: Chain Saw
A7: Debilitator
A8: Drill
A9: Air Anchor
AA: AutoCrossbow
AB: Fire Skean
AC: Water Edge
AD: Bolt Edge
AE: Inviz Edge
AF: Shadow Edge
B0: Goggles
B1: Star Pendant
B2: Peace Ring
B3: Amulet
B4: White Cape
B5: Jewel Ring
B6: Fairy Ring
B7: Barrier Ring
B8: MithrilGlove
B9: Guard Ring
BA: RunningShoes
BB: Wall Ring
BC: Cherub Down
BD: Cure Ring
BE: True Knight
BF: DragoonBoots
C0: Zephyr Cape
C1: Czarina Ring
C2: Cursed Ring
C3: Earrings
C4: Atlas Armlet
C5: Blizzard Orb
C6: Rage Ring
C7: Sneak Ring
C8: Pod Bracelet
C9: Hero Ring
CA: Ribbon
CB: Muscle Belt
CC: Crystal Orb
CD: Gold Hairpin
CE: Economizer
CF: Thief Glove
D0: Gauntlet
D1: Genji Glove
D2: Hyper Wrist
D3: Offering
D4: Beads
D5: Black Belt
D6: Coin Toss
D7: FakeMustache
D8: Gem Box
D9: Dragon Horn
DA: Merit Award
DB: Memento Ring
DC: Safety Bit
DD: Relic Ring
DE: Moogle Charm
DF: Charm Bangle
E0: Marvel Shoes
E1: Back Guard
E2: Gale Hairpin
E3: Sniper Sight
E4: Exp. Egg
E5: Tintinabar
E6: Sprint Shoes
E7: Rename Card
E8: Tonic
E9: Potion
EA: X-Potion
EB: Tincture
EC: Ether
ED: X-Ether
EE: Elixir
EF: Megalixir
F0: Fenix Down
F1: Revivify
F2: Antidote
F3: Eyedrop
F4: Soft
F5: Remedy
F6: Sleeping Bag
F7: Tent
F8: Green Cherry
F9: Magicite
FA: Super Ball
FB: Echo Screen
FC: Smoke Bomb
FD: Warp Stone
FE: Dried Meat
FF: Empty

* * *

Part 5: Monsters

(nice big offset table way below... have fun with it)

Status (F0200 - F31FF)

Structure: 32 bytes per monster

#: Attributes to:
1: Speed
2: Attack
3: Hit %
4: Evade %
5: Magic Block
6: Defense
7: Magic Defense
8: Magic Power
9: Lo HP
10: Hi HP
11: Lo MP
12: Hi MP
13: Lo EXP
14: Hi EXP
15: Lo GP
16: Hi GP
17: Level
18: Morph template
19: Misc byte
20: Misc byte 2
21: Block Status 1
22: Block Status 2
23: Block Status 3
24: [Absorb](#elem)
25: [No Effect](#elem)
26: [Weakness](#elem)
27: Attack type
28: Status 1
29: Status 2
30: Status 3
31: Status 4
32: [Special attack attribute](#espec)

* * *

Items: (F3200-F37FF)

Structure: 4 bytes per monster

1: [Steal item 1 (rare)](#item)
2: [Steal item 2 (common)](#item)
3: [Leave item 1 (rare)](#item)
4: [Leave item 2 (common)](#item)

Steal and Leave slot 1 control the 'rare' item. Items in the 'common' slots tend to come very very frequently, so if you only want the item to be left once in awhile, stick it in the rare slot and leave the common slot empty. If there is a different item in both common or rare slots, you're pretty much guranteed to get one, though obviously, the one in the common slot will appear more often. If the rare AND common slots of either of the two are filled with the same item, it's a guaranteed stolen/left item.

* * *

Magic/Special attacks (F8600-F88FF)

(This data is actually divided into two parts. One part are the pointers (this portion) to the enemies attack data/AI and the second part IS the attack data/AI location.)
Structure: 2 bytes per monster

1: AI script pointer x1
2: AI script pointer x256

These bytes simply point to a particular byte in the massive AI data. To calculate the location of an enemie's AI script, take byte 2, and multiply it by FFh, and ADD the amount in byte 1. Now that you have figured out how many bytes the script pointers are together, add F8900 and you'll get the exact location of where exactly the enemy's AI data begins. To make things confusing, the size of each AI is varied.

* * *

AI script data (F8900-FC24F)

Structure: The entire thing

This here takes the cake for being the most difficult data I've found in the ROM (well, besides the world map's compression).

There is no particular size for any AI script, and that's one big reason why this whole thing is such a bitch to figure out. The enemy script pointers simply point to a particular byte in this whole labyrnith. They always seem to point to an 'attack type' byte (the value begins with "F"), and gives a list of attacks used afterward. But that's only how simple scripts are. We have yet to figure out what controls counter attacks, final death attacks and how the actual script ends, etc.

For all I can tell you so far...

The "attack type" can only be one that begins with an F. If it's something else, it'll be 'defaulted' as a magic attack.

If the attack type byte is:

F0: Magic Attack
F4: Character battle command
F6: Throw item

Simply changing the attack type byte will affect what the next set up values will be. Because of this, something tells me we're hacking ASM commands...

Much of this helpful info came from Master ZED. If it weren't for him, I probably would've given on up this. Just what we've figured out was over a span of a couple of months of on and off testings. If you want to help figure it out completely, tell me about your additional findings. :)

* * *

Control: (F3F00-F44FF)

Structure: 4 bytes per monster

1: [Spell 1](#magic)
2: [Spell 2](#magic)
3: [Spell 3](#magic)
4: [Spell 4](#magic)

This is to change each individual battle window for each monster with Relms' Control command. You can give them anything classified as a magic spell.

* * *

Sketch: (F4500-F47FF)

Structure: 2 bytes per monster

1: [Spell 1](#magic)
2: [Spell 2](#magic)

Yay, the data that changes what spells enemies use when Relm sketches them.

Structure: 2 bytes per monster

* * *

Rage: (F4800-F49FF)

Structure: 2 bytes per monster

1: [Spell 1](#magic)
2: [Spell 2](#magic)

Want to make Rage a better command (IYO)? Then this is for you. Each enemy is allotted 2 bytes for the spells they use when a character use the Rage command. The normal game ALWAYS uses the first byte as the normal attack. However, the second one is normally used as the special attack/magic spell. But with this, you can change the normal attack into anything classified as a spell, so instead of one, each of Rage can have TWO special attacks.

* * *

Offset table

Have fun with this table, like I did making it (me got a sore finger from pasting all the damn HTML hundreds of times...) and calculating each offset...




STATS

ITEMS

CONTROL

SKETCH

RAGE

`Guard_____`:

F0200

F3200

F3F00

F4500

F4800

`Soldier___`:

F0220

F3204

F3F04

F4502

F4802

`Templar___`:

F0240

F3208

F3F08

F4504

F4804

`Ninja_____`:

F0260

F320C

F3F0C

F4506

F4806

`Samurai___`:

F0280

F3210

F3F10

F4508

F4808

`Orog______`:

F02A0

F3214

F3F14

F450A

F480A

`Mag Roader`:

F02C0

F3218

F3F18

F450C

F480C

`Retainer__`:

F02E0

F321C

F3F1C

F450E

F480E

`Hazer_____`:

F0300

F3220

F3F20

F4510

F4810

`Dahling___`:

F0320

F3224

F3F24

F4512

F4812

`Rain Man__`:

F0340

F3228

F3F28

F4514

F4814

`Brawler___`:

F0360

F322C

F3F2C

F4516

F4816

`Apokryphos`:

F0380

F3230

F3F30

F4518

F4818

`Dark Force`:

F03A0

F3234

F3F34

F451A

F481A

`Whisper___`:

F03C0

F3238

F3F38

F451C

F481C

`Over-Mind_`:

F03E0

F323C

F3F3C

F451E

F481E

`Osteosaur_`:

F0400

F3240

F3F40

F4520

F4820

`Commander_`:

F0420

F3244

F3F44

F4522

F4822

`Rhodox____`:

F0440

F3248

F3F48

F4524

F4824

`Were-Rat__`:

F0460

F324C

F3F4C

F4526

F4826

`Ursus_____`:

F0480

F3250

F3F50

F4528

F4828

`Rhinotaur_`:

F04A0

F3254

F3F54

F452A

F482A

`Steroidite`:

F04C0

F3258

F3F58

F452C

F482C

`Leafer____`:

F04E0

F325C

F3F5C

F452E

F482E

`Stray Cat_`:

F0500

F3260

F3F60

F4530

F4830

`Lobo______`:

F0520

F3264

F3F64

F4532

F4832

`Doberman__`:

F0540

F3268

F3F68

F4534

F4834

`Vomammoth_`:

F0560

F326C

F3F6C

F4536

F4836

`Fidor_____`:

F0580

F3270

F3F70

F4538

F4838

`Baskervor_`:

F05A0

F3274

F3F74

F453A

F483A

`Suriander_`:

F05C0

F3278

F3F78

F453C

F483C

`Chimera___`:

F05E0

F327C

F3F7C

F453E

F483E

`Behemoth__`:

F0600

F3280

F3F80

F4540

F4840

`Mesosaur__`:

F0620

F3284

F3F84

F4542

F4842

`Pterodon__`:

F0640

F3288

F3F88

F4544

F4844

`FossilFang`:

F0660

F328C

F3F8C

F4546

F4866

`White Drgn`:

F0680

F3290

F3F90

F4548

F4869

`Doom Drgn_`:

F06A0

F3294

F3F94

F454A

F486A

`Brachosaur`:

F06C0

F3298

F3F98

F454C

F486C

`Tyranosaur`:

F06E0

F329C

F3F9C

F454E

F486E

`Dark Wind_`:

F0700

F32A0

F3FA0

F4550

F4850

`Beakor____`:

F0720

F32A4

F3FA4

F4552

F4852

`Vulture___`:

F0740

F32A8

F3FA8

F4554

F4854

`Harpy_____`:

F0760

F32AC

F3FAC

F4556

F4856

`HermitCrab`:

F0780

F32B0

F3FB0

F4558

F4858

`Trapper___`:

F07A0

F32B4

F3FB4

F455A

F485A

`Hornet____`:

F07C0

F32B8

F3FB8

F455C

F485C

`CrassHoppr`:

F07E0

F32BC

F3FBC

F455E

F485E

`Delta Bug_`:

F0800

F32C0

F3FC0

F4560

F4860

`Gilomantis`:

F0820

F32C4

F3FC4

F4562

F4862

`Trilium___`:

F0840

F32C8

F3FC8

F4564

F4864

`Nightshade`:

F0860

F32CC

F3FCC

F4566

F4866

`TumbleWeed`:

F0880

F32D0

F3FD0

F4568

F4868

`Bloompire_`:

F08A0

F32D4

F3FD4

F456A

F486A

`Trilobiter`:

F08C0

F32D8

F3FD8

F456C

F486C

`Siegfried_`:

F08E0

F32DC

F3FDC

F456E

F486E

`Nautiloid_`:

F0900

F32E0

F3FE0

F4570

F4870

`Exocite___`:

F0920

F32E4

F3FE4

F4572

F4872

`Anguiform_`:

F0940

F32E8

F3FE8

F4574

F4874

`Reach Frog`:

F0960

F32EC

F3FEC

F4576

F4876

`Lizard____`:

F0980

F32F0

F3FF0

F4578

F4878

`ChickenLip`:

F09A0

F32F4

F3FF4

F457A

F487A

`Hoover____`:

F09C0

F32F8

F3FF8

F457C

F487C

`Rider_____`:

F09E0

F32FC

F3FFC

F457E

F487E

`Chupon____`:

F0A00

F3300

F4000

F4580

F4880

`Pipsqueak_`:

F0A20

F3304

F4004

F4582

F4882

`M-TekArmor`:

F0A40

F3308

F4008

F4584

F4884

`Sky Armor_`:

F0A60

F330C

F400C

F4586

F4886

`Telstar___`:

F0A80

F3310

F4010

F4588

F4888

`Lethal Wpn`:

F0AA0

F3314

F4014

F458A

F488A

`Vaporite__`:

F0AC0

F3318

F4018

F458C

F488C

`Flan______`:

F0AE0

F331C

F401C

F458E

F488E

`Ing_______`:

F0B00

F3320

F4020

F4590

F4890

`Humpty____`:

F0B20

F3324

F4024

F4592

F4892

`Brainpan__`:

F0B40

F3328

F4028

F4594

F4894

`Cruller___`:

F0B60

F332C

F402C

F4596

F4896

`Cactrot___`:

F0B80

F3330

F4030

F4598

F4898

`Repo Man__`:

F0BA0

F3334

F4034

F459A

F489A

`Harvester_`:

F0BC0

F3338

F4038

F459C

F489C

`Bomb______`:

F0BE0

F333C

F403C

F459E

F489E

`Still Life`:

F0C00

F3340

F4040

F45A0

F48A0

`Boxed Set_`:

F0C20

F3344

F4044

F45A2

F48A2

`SlamDancer`:

F0C40

F3348

F4048

F45A4

F48A4

`HadesGigas`:

F0C60

F334C

F404C

F45A6

F48A6

`Pug_______`:

F0C80

F3350

F4050

F45A8

F48A8

`Magic Urn_`:

F0CA0

F3354

F4054

F45AA

F48AA

`Mover_____`:

F0CC0

F3358

F4058

F45AC

F48AC

`Figaliz___`:

F0CE0

F335C

F405C

F45AE

F48AE

`Buffalax__`:

F0D00

F3360

F4060

F45B0

F48B0

`Aspik_____`:

F0D20

F3364

F4064

F45B2

F48B2

`Ghost_____`:

F0D40

F3368

F4068

F45B4

F48B4

`Crawler___`:

F0D60

F336C

F406C

F45B6

F48B6

`Sand Ray__`:

F0D80

F3370

F4070

F45B8

F48B8

`Areneid___`:

F0DA0

F3374

F4074

F45BA

F48BA

`Actaneon__`:

F0DC0

F3378

F4078

F45BC

F48BC

`Sand Horse`:

FODE0

F337C

F407C

F45BE

F48BE

`Dark Side_`:

F0E00

F3380

F4080

F45C0

F48C0

`Mad Oscar_`:

F0E20

F3384

F4084

F45C2

F48C2

`Crawly____`:

F0E40

F3388

F4088

F4554

F48C4

`Bleary____`:

F0E60

F338C

F408C

F45C6

F48C6

`Marshal___`:

F0E80

F3390

F4090

F45C8

F48C8

`Trooper___`:

F0EA0

F3394

F4094

F45CA

F48CA

`General___`:

F0EC0

F3398

F4098

F45CC

F48CC

`Covert____`:

F0EE0

F339C

F409C

F45CE

F48CE

`Ogor______`:

F0F00

F33A0

F40A0

F45D0

F48D0

`Warlock___`:

F0F20

F33A4

F40A4

F45D2

F48D2

`Madam_____`:

F0F40

F33A8

F40A8

F45D4

F48D4

`Joker_____`:

F0F60

F33AC

F40AC

F45D6

F48D6

`Iron Fist_`:

F0F80

F33B0

F40B0

F45D8

F48D8

`Goblin____`:

F0FA0

F33B4

F40B4

F45DA

F48DA

`Apparite__`:

F0FC0

F33B8

F40B8

F45DC

F48DC

`PowerDemon`:

F0FE0

F33BC

F40BC

F45DE

F48DE

`Displayer_`:

F1000

F33C0

F40C0

F45E0

F48E0

`Vector Pup`:

F1020

F33C4

F40C4

F45E2

F48E2

`Peepers___`:

F1040

F33C8

F40C8

F45E4

F48E4

`Sewer Rat_`:

F1060

F33CC

F40CC

F45E6

F48E6

`Slatter___`:

F1080

F33D0

F40D0

F45E8

F48E8

`Rhinox____`:

F10A0

F33D4

F40D4

F45EA

F48EA

`Rhobite___`:

F10C0

F33D8

F40D8

F45EC

F48EC

`Wild Cat__`:

F10E0

F33DC

F40DC

F45EE

F48EE

`Red Fang__`:

F1100

F33E0

F40E0

F45F0

F48F0

`Bounty Man`:

F1120

F33E4

F40E4

F45F2

F48F2

`Tusker____`:

F1140

F33E8

F40E8

F45F4

F48F4

`Ralph_____`:

F1160

F33EC

F40EC

F45F6

F48F6

`Chitonid__`:

F1180

F33F0

F40F0

F45F8

F48F8

`Wart Puck_`:

F11A0

F33F4

F40F4

F45FA

F48FA

`Rhyos_____`:

F11C0

F33F8

F40F8

F45FC

F48FC

`SrBehemoth`:

F11E0

F33FC

F40FC

F45FE

F48FE

`Vectaur___`:

F1200

F3400

F4100

F4600

F4900

`Wyvern____`:

F1220

F3404

F4104

F4602

F4902

`Zombone___`:

F1240

F3408

F4108

F4604

F4904

`Dragon____`:

F1260

F340C

F410C

F4606

F4906

`Brontaur__`:

F1280

F3410

F4110

F4608

F4908

`Allosaurus`:

F12A0

F3414

F4114

F460A

F490A

`Cirpius___`:

F12C0

F3418

F4118

F460C

F490C

`Sprinter__`:

F12E0

F341C

F411C

F460E

F490E

`Gobbler___`:

F1300

F3420

F4120

F4610

F4910

`Harpiai___`:

F1320

F3424

F4124

F4612

F4912

`GloomShell`:

F1340

F3428

F4128

F4614

F4914

`Drop______`:

F1360

F342C

F412C

F4616

F4916

`Mind Candy`:

F1380

F3430

F4130

F4618

F4918

`WeedFeeder`:

F13A0

F3434

F4134

F461A

F491A

`Luridan___`:

F13C0

F3438

F4138

F461C

F491C

`Toe Cutter`:

F13E0

F343C

F413C

F461E

F491E

`Over Grunk`:

F1400

F3440

F4140

F4620

F4920

`Exoray____`:

F1420

F3444

F4144

F4622

F4922

`Crusher___`:

F1440

F3448

F4148

F4624

F4924

`Uroburos__`:

F1460

F344C

F414C

F4626

F4926

`Primordite`:

F1480

F3450

F4150

F4628

F4928

`Sky Cap___`:

F14A0

F3454

F4154

F462A

F492A

`Cephaler__`:

F14C0

F3458

F4158

F462C

F492C

`Maliga____`:

F14E0

F345C

F415C

F462E

F492E

`Gigan Toad`:

F1500

F3460

F4160

F4630

F4930

`Geckorex__`:

F1520

F3464

F4164

F4632

F4932

`Cluck_____`:

F1540

F3468

F4168

F4634

F4934

`Land Worm_`:

F1560

F346C

F416C

F4636

F4936

`Test Rider`:

F1580

F3470

F4170

F4638

F4938

`PlutoArmor`:

F15A0

F3474

F4174

F463A

F493A

`Tomb Thumb`:

F15C0

F3478

F4178

F463C

F493C

`HeavyArmor`:

F15E0

F347C

F417C

F463E

F493E

`Chaser____`:

F1600

F3480

F4180

F4640

F4940

`Scullion__`:

F1620

F3484

F4184

F4642

F4942

`Poplium___`:

F1640

F3488

F4188

F4644

F4944

`Intangir__`:

F1660

F348C

F418C

F4646

F4946

`Misfit____`:

F1680

F3490

F4190

F4648

F4948

`Eland_____`:

F16A0

F3494

F4194

F464A

F494A

`Enuo______`:

F16C0

F3498

F4198

F464C

F494C

`Deep Eye__`:

F16E0

F349C

F419C

F464E

F494E

`GreaseMonk`:

F1700

F34A0

F41A0

F4650

F4950

`NeckHunter`:

F1720

F34A4

F41A4

F4652

F4952

`Grenade___`:

F1740

F34A8

F41A8

F4654

F4954

`Critic____`:

F1760

F34AC

F41AC

F4656

F4956

`Pan Dora__`:

F1780

F34B0

F41B0

F4658

F4958

`SoulDancer`:

F17A0

F34B4

F41B4

F465A

F495A

`Gigantos__`:

F17C0

F34B8

F41B8

F465C

F495C

`Mag Roader`:

F17E0

F34BC

F41BC

F465E

F495E

`Spek Tor__`:

F1800

F34C0

F41C0

F4660

F4960

`Parasite__`:

F1820

F34C4

F41C4

F4662

F4962

`EarthGuard`:

F1840

F34C8

F41C8

F4664

F4964

`Coelecite_`:

F1860

F34CC

F41CC

F4666

F4966

`Anemone___`:

F1880

F34D0

F41D0

F4668

F4968

`Hipocampus`:

F18A0

F34D4

F41D4

F466A

F496A

`Spectre___`:

F18C0

F34D8

F41D8

F466C

F496C

`Evil Oscar`:

F18E0

F34DC

F41DC

F466E

F496E

`Slurm_____`:

F1900

F34E0

F41E0

F4670

F4970

`Latimeria_`:

F1920

F34E4

F41E4

F4672

F4972

`StillGoing`:

F1940

F34E8

F41E8

F4674

F4974

`Allo Ver__`:

F1960

F34EC

F41EC

F4676

F4976

`Phase_____`:

F1980

F34F0

F41F0

F4678

F4978

`Outsider__`:

F19A0

F34F4

F41F4

F467A

F497A

`Barb-e____`:

F19C0

F34F8

F41F8

F467C

F497C

`Parasoul__`:

F19E0

F34FC

F41FC

F467E

F497E

`Pm Stalker`:

F1A00

F3500

F4200

F4680

F4980

`Hemophyte_`:

F1A20

F3504

F4204

F4682

F4982

`Sp Forces_`:

F1A40

F3508

F4208

F4684

F4984

`Nohrabbit_`:

F1A60

F350C

F420C

F4686

F4986

`Wizard____`:

F1A80

F3510

F4210

F4688

F4988

`Scrapper__`:

F1AA0

F3514

F4214

F468A

F498A

`Ceritops__`:

F1AC0

F3518

F4218

F468C

F498C

`Commando__`:

F1AE0

F351C

F421C

F468E

F498E

`Opinicus__`:

F1B00

F3520

F4220

F4690

F4990

`Poppers___`:

F1B20

F3524

F4224

F4692

F4992

`Lunaris___`:

F1B40

F3528

F4228

F4694

F4994

`Garm______`:

F1B60

F352C

F422C

F4696

F4996

`Vindr_____`:

F1B80

F3530

F4230

F4698

F4998

`Kiwok_____`:

F1BA0

F3534

F4234

F469A

F499A

`Nastidon__`:

F1BC0

F3538

F4238

F469C

F499C

`Rinn______`:

F1BE0

F353C

F423C

F469E

F499E

`Insecare__`:

F1C00

F3540

F4240

F46A0

F49A0

`Vermin____`:

F1C20

F3544

F4244

F46A2

F49A2

`Mantodea__`:

F1C40

F3548

F4248

F46A4

F49A4

`Bogy______`:

F1C60

F354C

F424C

F46A6

F49A6

`Prussian__`:

F1C80

F3550

F4250

F46A8

F49A8

`Black Drgn`:

F1CA0

F3554

F4254

F46AA

F49AA

`Adamanchyt`:

F1CC0

F3558

F4258

F46AC

F49AC

`Dante_____`:

F1CE0

F355C

F425C

F46AE

F49AE

`Wirey Drgn`:

F1D00

F3560

F4260

F46B0

F49B0

`Dueller___`:

F1D20

F3564

F4264

F46B2

F49B2

`Psychot___`:

F1D40

F3568

F4268

F46B4

F49B4

`Muus______`:

F1D60

F356C

F426C

F46B6

F49B6

`Karkass___`:

F1D80

F3570

F4270

F46B8

F49B8

`Punisher__`:

F1DA0

F3574

F4274

F46BA

F49BA

`Balloon___`:

F1DC0

F3578

F4278

F46BC

F49BC

`Gabbldegak`:

F1DE0

F357C

F427C

F46BE

F49BE

`GtBehemoth`:

F1E00

F3580

F4280

F46C0

F49C0

`Scorpion__`:

F1E20

F3584

F4284

F46C2

F49C2

`Chaos Drgn`:

F1E40

F3588

F4288

F46C4

F49C4

`Spit Fire_`:

F1E60

F358C

F428C

F46C6

F49C6

`Vectagoyle`:

F1E80

F3590

F4290

F46C8

F49C8

`Lich______`:

F1EA0

F3594

F4294

F46CA

F49CA

`Osprey____`:

F1EC0

F3598

F4298

F46CC

F49CC

`Mag Roader`:

F1EE0

F359C

F429C

F46CE

F49CE

`Bug_______`:

F1F00

F35A0

F42A0

F46D0

F49D0

`Sea Flower`:

F1F20

F35A4

F42A4

F46D2

F49D2

`Fortis____`:

F1F40

F35A8

F42A8

F46D4

F49D4

`Abolisher_`:

F1F60

F35AC

F42AC

F46D6

F49D6

`Aquila____`:

F1F80

F35B0

F42B0

F46D8

F49D8

`Junk______`:

F1FA0

F35B4

F42B4

F46DA

F49DA

`Mandrake__`:

F1FC0

F35B8

F42B8

F46DC

F49DC

`1st Class_`:

F1FE0

F35BC

F42BC

F46DE

F49DE

`Tap Dancer`:

F2000

F35C0

F42C0

F46E0

F49E0

`Necromancr`:

F2020

F35C4

F42C4

F46E2

F49E2

`Borras____`:

F2040

F35C8

F42C8

F46E4

F49E4

`Mag Roader`:

F2060

F35CC

F42CC

F46E6

F49E6

`Wild Rat__`:

F2080

F35D0

F42D0

F46E8

F49E8

`Gold Bear_`:

F20A0

F35D4

F42D4

F46EA

F49EA

`Innoc_____`:

F20C0

F35D8

F42D8

F46EC

F49EC

`Trixter___`:

F20E0

F35DC

F42DC

F46EE

F49EE

`Red Wolf__`:

F2100

F35E0

F42E0

F46F0

F49F0

`Didalos___`:

F2120

F35E4

F42E4

F46F2

F49F2

`Woolly____`:

F2140

F35E8

F42E8

F46F4

F49F4

`Veteran___`:

F2160

F35EC

F42EC

F46F6

F49F6

`Sky Base__`:

F2180

F35F0

F42F0

F46F8

F49F8

`IronHitman`:

F21A0

F35F4

F42F4

F46FA

F49FA

`Io________`:

F21C0

F35F8

F42F8

F46FC

F49FC


If you want the partial easy way out of doing this, you can Lord J's Monster Editor located at [Zophar's Domain](http://www.zophar.net). It currently only edits the monsters' stats and stealable items, and not the Rage/Sketch/Control data.

* * *

**Part 6: Enemy battle "formations" (F6400 - F85B0)**

Change the battles that appear. Using this stuff you can change the enemies in a battle, or if you want to make a fight harder, you can add more of the same.

Structure: 15 bytes per battle

1: The 'graphic fixer' byte
2: (Has something to do with the # of enemies...)
3: [Monster 1](#monst) [If monster is a boss](#boss)
4: [Monster 2](#monst) [If monster is a boss](#boss)
5: [Monster 3](#monst) [If monster is a boss](#boss)
6: [Monster 4](#monst) [If monster is a boss](#boss)
7: [Monster 5](#monst) [If monster is a boss](#boss)
8: [Monster 6](#monst) [If monster is a boss](#boss)
9: Monster 1 Position
10: Monster 2 Position
11: Monster 3 Position
12: Monster 4 Position
13: Monster 5 Position
14: Monster 6 Position
15: Monster types (normal/boss)


This stuff can really be a pain in the butt work with in hex editor. The main reason is because of the friggin # of battle types this game holds. It's thanks to Lord J for creating his FF6 Monster Edit and implementing a 'Make report' option that makes it so that it dumps all the enemy battle formations into a nifty txt file. There was NO WAY I was going to find out what each battle was on my own (would've taken too much time). But because of Lord J's excellent program, the list of battles can be found [here](battles.txt). To calculate the location of the battle you want to edit manually, do this:

1) Open up [battles.txt](battles.txt)
2) Look at the number of the battle you want to edit, and convert it to hex.
3) Multiply that number by E.
4) Then add F6400. This marks the location of the battle.

If you want the easy way out, go ahead and use Lord J's Monster Editor located at [Zophar's Domain](http://www.zophar.net). Not that it will help with fixing the graphic, though.

* * *

Misc Data for each formation

* * *

Magic Points per battle (IFB600-IFB7FF)

Structure: 1 byte

1: Amount of Magic Points for that particular battle

This data is interesting. There are 576 battle formations, however with this, you can only set the number of Magic Points gained for the first 512. Is that not interesting? Right after battle #512 begins the Colosseum data.

Now, let's get down to the meat of this data. Remember how in the original FF6, monsters would only drop at the most 10 Magic Points? With this, it's possible to make them drop up to 255. You could make yourself a super tough fight and make it drop like 50 or something...

* * *

**Part 7: Colosseum data (1FB800 - 1FFBBF)**

Structure: 4 bytes per battle

1: [Monster to fight](#monst)
2: ? (all collosseum battles share the same value...)
3: [Item won](#item)
4: Show won item name? (00: Yes, FF: No \[show name as ????????????\])

The data goes in the order of the item bet. The items order is the games' order of importance, so the first item would be the result of a Dirk and so on.

* * *

**Part 8: Esper Data (187000 - 187127)**

Structure: 11 bytes per Esper

1: Spell 1 Learn rate
2: Spell 1
3: Spell 2 Learn rate
4: Spell 2
5: Spell 3 Learn rate
6: Spell 3
7: Spell 4 Learn rate
8: Spell 4
9: Spell 5 Learn rate
10: Spell 5
11: Level up bonus

`Ramuh___`: 187000
`Ifrit___`: 18700B
`Shiva___`: 187016
`Siren___`: 187021
`Terrato_`: 18702C
`Shoat___`: 187037
`Maduin__`: 187042
`Bismark_`: 18704D
`Stray___`: 187058
`Palador_`: 187063
`Tritoch_`: 18706E
`Odin____`: 187079
`Raiden__`: 187084
`Bahamut_`: 18708F
`Alexandr`: 18709A
`Crusader`: 1870A5
`Ragnarok`: 1870B0
`Kirin___`: 1870BB
`ZoneSeek`: 1870C6
`Carbunkl`: 1870D1
`Phantom_`: 1870DC
`Sraphim_`: 1870E7
`Golem___`: 1870F2
`Unicorn_`: 1870FD
`Fenrir__`: 187108
`Starlet_`: 187113
`Phoenix_`: 18711E

* * *

**Part 9: Magic data (46CC0-47ABF)**

1: Targetting
2: [Elements](elem)
3: Effect
4: Damage type (first half) Where used (second half)
5: Effect 2
6: MP Cost
7: Power
8: ?
9: ?
10: [Special effect](#mse)
11: [Status 1](#stat1)
12: [Status 2](#stat2)
13: [Status 3](#stat3)
14: [Status 4](#stat4)

Structure: 14 bytes per spell

46CC0: Fire
46CCE: Ice
46CDC: Bolt
46CEA: Poison
46CF8: Drain
46D06: Fire 2
46D14: Ice 2
46D22: Bolt 2
46D30: Bio
46D3E: Fire 3
46D4C: Ice 3
46D5A: Bolt 3
46D68: Break
46D76: Doom
46D84: Pearl
46D92: Flare
46DA0: Demi
46DAE: Quartr
46DBC: X-Zone
46DCA: Meteor
46DD8: Ultima
46DE6: Quake
46DF4: W Wind
46E02: Merton
46E10: Scan
46E1E: Slow
46E2C: Rasp
46E3A: Mute
46E48: Safe
46E56: Sleep
46E64: Muddle
46E72: Haste
46E80: Stop
46E8E: Bserk
46E9C: Float
46EAA: Imp
46EB8: Rflect
46EC6: Shell
46ED4: Vanish
46EE2: Haste 2
46EF0: Slow 2
46EFE: Osmose
46F0C: Warp
46F1A: Quick
46F28: Dispel
46F36: Cure
46F44: Cure 2
46F52: Cure 3
46F60: Life
46F6E: Life 2
46F7C: Antdot
46F8A: Remedy
46F98: Regen
46FA6: Life 3

* * *

**Part 10: Shops (477C0-47FCF)**

Structure: 9 bytes per shop
1: 50% Discount if character x is leading (first 4 bits), Shop type (second 4 bits)
2: Item 1 in list
3: Item 2 in list
4-9: (all the rest are just the items in the list, in the same order)

Change the shops to contain anything in the game. It was fun identifying some of these...

Hmm, and apparently, you can use any character to get a discount at 50%, and not just Edgar, just set the first half to the predefined character #. The game only uses Edgar in certain situations, but you can change that to anyone else to any shop. Maybe you can secretly add a lead character for each shop to get discounts or something, \*shrug\*.
47CC0: Narshe weapons (before Magitek factory)
47CC9: Narshe armor (before Magitek factory)
47CD2: Narshe relics (before Magitek factory)
47CDB: Narshe items (before Magitek factory)
47CE4: Figaro castle items (before Kefka arrives)
47CED: South Figaro weapons (WoB)
47CF6: South Figaro armor (WoB)
47CFF: South Figaro relics (WoB)
47D08: South Figaro items (WoB)
47D11: Mobliz weapons
47D1A: Mobliz armor
47D23: Mobliz relics
47D2C: Mobliz items
47D35: Nikeah weapons (WoB)
47D3E: Nikeah armor (WoB)
47D47: Nikeah items (WoB)
47D50: Nikeah relics (WoB)
47D59: Kohlinghen weapons (WoB)
47D62: Kohlinghen armor (WoB)
47D6B: Kohlinghen items (WoB)
47D74: Jidoor weapons (WoB)
47D7D: Jidoor armor (WoB)
47D86: Jidoor items (WoB)
47D8F: Jidoor relics (WoB)
47D98: Blackjack's items (I think)
47DA1: Albrook weapons (WoB)
47DAA: Albrook armor (WoB)
47DB3: Vector weapons
47DBC: Vector armor
47DC5: Tzen weapons (WoB)
47DCE: Tzen armor (WoB)
47DD7: Tzen items (WoB)
47DE0: Tzen relics (WoB)

* * *

**Part 11: Ragnarok Metamorphosis (48140-481A7)**

Structure: 4 bytes per cycle

1-4: Each byte represents one of the items that can be won in a cycle.

There are 4 unused cycles, allowing you to create 4 additional ones without changing others. To have those cycles you've created go into effect, assign it monsters. The hex value for the cycle is the cycle's number in hex.


* * *

**Part 12: Start-up (2D7EA0 - ?)**

Structure: 22 bytes per character

1: HP
2: MP
3: [Battle Command 1](#battle)
4: [Battle Command 2](#battle)
5: [Battle Command 3](#battle)
6: [Battle Command 4](#battle)
7: Vigor
8: Speed
9: Stamina
10: Mag.Pwr
11: Bat.Pwr
12: Defense
13: Mag.Def
14: Evade %
15: MBlock %
16: [Weapon](#item)
17: [Shield](#item)
18: [Helm](#item)
19: [Armor](#item)
20: [Relic 1](#item)
21: [Relic 2](#item)
22: Level

2D7EA0: Terra
2D7EB6: Locke
2D7ECC: Cyan
2D7EE2: Shadow
2D7EF8: Edgar
2D7F0E: Sabin
2D7F24: Celes
2D7F3A: Strago
2D7F50: Relm
2D7F66: Setzer
2D7F7C: Mog
2D7F92: Gau
2D7FA8: Gogo
2D7FBE: Umaro
2D7FD4: Banon
2D7FEA: Leo
2D8000: ????? (Ghost1)
2D8016: ????? (Ghost2)
2D802C: Kupek
2D8042: Kupop
2D8058: Kumama
2D806E: Kuku
2D8084: Kutan
2D809A: Kupan
2D80B0: Kushu
2D80C6: Kurin
2D80DC: Kuru
2D80F2: Kamog
2D8108: Mog (scenario select)
2D811E: ????? (Terra)*
2D8134: Maduin (hmm...)
2D814A: ?????
2D8160: Wedge
2D8176: Vicks
2D8226: Kefka (Terra's flashback and imperial camp)
2D823C: Kefka (Esper Cave)
2D8252: Kefka (Thamasa attack)
2D8268: Kefka (Dummy entity; never used)
2D827E: Kefka (Dummy entity; never used)
2D8294: Kefka (Dummy entity; never used)
2D82AA: Kefka (Dummy entity; never used)

There are more, for the other dummy characters (Tork, Fabian, Drake, Ho, Victor, Siele, etc), but the values are all 00 and you can't get these guys anyway (like the last 4 dummy Kefka's) and they have no sprite.

*this is basically nothing. In the part where the character names are stored, this is Terra's name in the beginning. Changing any values will do nothing.

C9C94 and C9C95: GP at startup. (bytes are reversed/inverted)

* * *

**Part 13: EXP needed for level up (2D8420-2D84F3)**

Since the data here is so small and so simple (it's only two bytes for each level that have to do with numerical values), I'm not going to list the offsets for each level. It should be simple to figure out what level is which.

Structure: 2 bytes per level

1: Exp needed for level up x8
2: Exp needed for level up x2048

* * *

**Part 14: HP gained at level up (26F6A0-26F701)**

Structure: 1 byte per level

1: The HP gained at that level

Unfortunately, you can't set up the way the HP is gained for each individual character at level ups (you can only set how much they begin with at level 1), so this is completely global for every character. You're limited to 255 HP per level.

Since you can set the HP the characters have at level 1 where their start up data, this data begins at what they get at level TWO.

* * *

**Part 15: MP gained at level up (26F702-26F763)**

Structure: 1 byte per level

1: The MP gained at that level

This works exactly the same as HP at level up, except it's for MP.

* * *

**Part 16: Music pointers (varied locations)**

The structure is always one byte, and that's for the song.

No, this doesn't allow you to edit the music, but rather change the music to other songs at certain points in the game

Do note that this list is very incomplete, since music pointers seem to be scattered all around the ROM. Thanks to a Game Genie code, I was able to find the pointer to the normal battle music. However, right next to the normal battle music, were the pointers for the boss, and big boss battle music! Then, after a little search, I found the musics to all 4 overworld themes! And so I found a few more later. So far, 13 pointers have been found.

2C13B: Normal battle music
2C13C: Boss battle music
2C13D: Big boss music

2E858A: World of Balance in-flight airship music
2E858C: World of Ruin in-flight airship music

2E858D: Chocobo music in the WoB.
2E858E: Chocobo music (on the Veldt?) (unable to be tested)
2E858F: Chocobo music (when the default world theme is "Dark World")
2E8590: Chocobo music in the WoR.

2E8591: World of Balance overworld music
2E8592: Veldt music
2E8593: World of Ruin, first 'dark' world music
2E8594: World of Ruin main overworld music

* * *

* * *

**Part 17: Text stuff**

(this is the text that uses the 'small' font)
2AFE0: Status effects
34B0D: "Config" menu text
35E4A: "Skills" menu text and Esper text
36671: "Status" menu text
36AE5: "Please enter a name" text.
37DB1: LV, HP, MP text in menu
379C7: Group formation text
38F18: "Item" menu text
38F7A: Equipment status text (double click in items menu)
3A4BC: "Equip" menu text part 1
3A50B: "Equip" menu text part 2
3A573: "Equip" menu text part 3
3A5C7: "Equip" menu text part 4
3B611: Colosseum challenger text
3C4FE: Shop text
47AC0: Character names
EFDA0: Rare items and descriptions
F3B40: Esper attack descriptions
F3E40: SwdTech attack names
FC250: Monster names
FD2D0: Monster pre-defined special attack names
FE3E0: Battle text part 1(lots of dummied text in here!)
FFE00: Blitz descriptions
FFF00: Sword Technique descriptions
1000AE: Esper level up bonuses
10D400: Battle text part 2
11F200: Battle text part 3
127100: Item types
12B500: Item names
18CBA0: Magic spell descriptions
18D0A0: Battle commands
26F767: Magic spells (includes special attacks too)
2D6600: Item descriptions
2E0000: Esper level up bonus descriptions

* * *

**Part 18: Palettes**


Battle sprite palette pointers

Structure: 1 byte per character

1: Palette used

2D02B: Terra
2D02C: Locke
2D02D: Cyan
2D02E: Shadow
2D02F: Edgar
2D030: Sabin
2D031: Celes
2D032: Strago
2D033: Relm
2D034: Setzer
2D035: Moogle
2D036: Gau
2D037: Gogo
2D038: Umaro

Overworld character palette data (268200-?)

Structure: 32 bytes

Every two bytes is one color on the palette, and that's all I know about this. Since the SNES uses a very, very vast palette, I'm pretty much stuck in the dark here on how this works. Here it is, as explained by Lord J:

32 bytes are used for one palette setting. Two bytes are used for one color. Each color is coded RGB, with 5 bits per basic color, wich leaves 1 extra bit for transparency (not used for wall paper settings tough).

Here is the encoding of one color:

<\-\-\- byte n -->   <- byte n+1 -->
msb         lsb   msb         lsb
x x x x x x x x   x x x x x x x x
____\] \[_______\]   | \[_______\] \[__
3lsb    5bits     | 5bits     2msb
green    red      |  blue     green
                  |
                  \\__transparency bit


The 2 bytes are inverted: this is the way the CPU stores 16 bits info
in memory (8-bits LIFO).


Analysis on WP palette information:
base: 0x2D1E00, 32 bytes per WP, 8 WP in total

offsets:
00 and 01: unused colors (set to 0000 -> black)
02 to 0f included: palette for wp (7 adjustable RGB colors)
10 to 1f included: unused color (all set to 00-38 -> dark blue)

those undecoded bytes were unused colors, so each palette would hold a maximum of 16 colors

Pre-release note: The rest of the palette data isn't here. Check Lord J's page, that's where the rest are. Though his URL evades my mind right now...

* * *

**Part 19: Stuff**

2CE600: Hmm, this data looks interesting...
2CEA00: So does this
2CEB00: As does this

**Part 20: Byte Values**

1st byte of who can equip byte values:

Bits

bit 1= Terra
bit 2= Locke
bit 3= Cyan
bit 4= Shadow
bit 5= Edgar
bit 6= Sabin
bit 7= Celes
bit 8= Strago

Bytes

(first half)

1: Edgar
2: Sabin
3: Edgar, Sabin
4: Celes
5: Edgar, Celes
6: Sabin, Celes
7: Edgar, Sabin, Celes
8: Strago
9: Edgar, Strago
A: Sabin, Strago
B: Edgar, Sabin, Strago
C: Celes, Strago
D: Edgar, Celes, Strago
E: Sabin, Celes, Strago
F: Edgar, Sabin, Celes, Strago

(second half)

1: Terra
2: Locke
3: Terra, Locke
4: Cyan
5: Terra, Cyan
6: Locke, Cyan
7: Terra, Locke, Cyan
8: Shadow
9: Terra, Shadow
A: Locke, Shadow
B: Terra, Locke, Shadow
C: Cyan, Shadow
D: Terra, Cyan, Shadow
E: Locke, Cyan, Shadow
F: Terra, Locke, Cyan, Shadow

2nd byte of who can equip byte values:

Bits

bit 1= Relm
bit 2= Setzer
bit 3= Mog
bit 4= Gau
bit 5= Gogo
bit 6= Umaro
bit 7= Effective only if an Imp
bit 8= Unknown bit

(first half)

1: Gogo
2: Umaro
3: Gogo, Umaro
4: Effective only if an Imp
5: Gogo, Effective only if an Imp
6: Umaro, Effective only if an Imp
7, Gogo, Umaro, Effective only if an Imp
8: Unknown (used if Gogo CAN'T normally use it)
9: Gogo, Unknown (this is what the game uses if Gogo can normally use it)
A: Umaro, Unknown
B: Gogo, Umaro, Unknown
C: Effective only if an Imp, Unknown
D: Gogo, Effective only if an Imp, Unknown
E: Umaro, Effective only if an Imp, Unknown
F: Gogo, Umaro, Effective only if an Imp, Unknown

(Remember, Umaro can't equip anything besides Relics, unless a bit or something that allows you to change his equipment is ever found...)

(second half)

1: Relm
2: Setzer
3: Relm, Setzer
4: Mog
5: Relm, Mog
6: Setzer, Mog
7: Relm, Setzer, Mog
8: Gau
9: Relm, Gau
A: Setzer, Gau
B: Relm, Setzer, Gau
C: Mog, Gau
D: Relm, Mog, Gau
E: Setzer, Mog, Gau
F: Relm, Setzer, Mog, Gau

Vigor/Speed/Stamina/Mag.Pwr bonus byte values:

0: 0
1: +1
2: +2
3: +3
4: +4
5: +5
6: +6
7: +7
8: 0
9: -1
A: -2
B: -3
C: -4
D: -5
E: -6
F: -7

Abilities can be used byte values:

Bits

bit 1= ? Unused bit
bit 2= SwdTech
bit 3= ? Unused bit
bit 4= ? Unused bit
bit 5= ? Unused bit
bit 6= 2-hand
bit 7= Runic
bit 8= ? Unused bit

(first half)

0-3: None
4-7: 2-hand
8-B: Runic
C-F: Runic, 2-hand

(second half)
0: None
1: Unknown
2: SwdTech
3: Unknown, SwdTech

(The rest of the results are just a bunch of unknown stuff, with SwdTech in some of them and are probably nothing anyways.)

MBlock% and Evade % byte values:

The first half pertain to the MBlock% and the right four pertain to Evade %.

1: 10%
2: 20%
3: 30%
4: 40%
5: 50%
6: -10%
7: -20%
8: -30%
9: -40%
A: -50%
B: (glitch) sets specified stat 0 no matter what (?)
C-F: (glitch) sets specified stat to 255 no matter what (?)


Byte 4 of Magic data values:

Damage type (first half of byte 4 in magic):

Bits

bit 1= Unknown bit
bit 2= Do damage
bit 3= Unknown bit
bit 4= Unknown/MP switch

Not exactly sure how to explain it, but bit 4 acts as a kind of 'switch' for the 'do damage' bit (if present) which causes it to do MP damage instead.

Bytes:

0: No damage
1: Unknown 1
2: Do damage
3: Unknown 1, Do Damage
4: Unknown 2
5: Unknown 1, Unknown 2
6: Do Damage, Unknown 2
7: Unknown 1, Do damage, Unknown 2
8: Unknown/MP switch
9: Unknown 1, Unknown/MP switch
A: MP damage (switch)
B: Unknown 2, Unknown/MP switch
C: Unknown 1, MP damage
D: Unknown 1, Unknown 2, Unknown/MP switch
E: Unknown 2, MP damage
F: Unknown 1, Unknown 2, MP damage

Useable outside battle? (second half):

Bits

bit 1= Yes
bit 2= No
bit 3= Unknown bit
bit 4= Unknown bit

Bytes

Note: Ones with "No and Yes" in the same description end up being "Yes" while the game is running. They are both No AND Yes, according to the binary result, but in the case, Yes prevails in the end, because it's the higher bit. (in other words, the effect would be 'Yes' anyways). Also, bits that are labeled with 'Unknown' or 'Nothing', are automatically counted as 'No'. Hope this doesn't confuse anyone, since I'm terrible at explaining things. :P

0: Nothing
1: Yes
2: No
3: Yes, No
4: Unknown 1
5: Yes, Unknown 1
6: No, Unknown 1
7: Yes, No, Unknown 1
8: Unknown 2
9: Yes, Unknown 2
A: No, Unknown 2
B: Yes, No, Unknown 2
C: Unknown 1, Unknown 2
D: Yes, Unknown 1, Unknown 2
E: No, Unknown 1, Unknown 2
F: Yes, No, Unknown 1, Unknown 2

And only god knows what the unknown bits are.

Magic Effect 2

(1st half of byte 5):
Bits

5: Unknown
6: Never misses
7: Unknown
8: Does a certain % of damage in accordance to the spell's power*

2: Never misses
8: Does a certain % of damage in accordance to the Spell's power*

*It's based about the % of the value used in hex. This is used in spells like Demi and Quartr.

(2nd half of byte 5 in magic)


Bits

1: Heal HP
2: Absorb Target's HP
3: Remove Status
4: Give Status

Byte values


1: Heal HP
2: Caster absorbs Target's HP
3: Target absorbs Caster's HP
4: Give Status
5: Heal HP, Give status
6: Caster absorbs Target's HP, Give Status
7: Target absorbs Caster's HP, Give Status
8: Remove status
9: Heal HP, Remove status
A: Caster absorbs Target's HP, Remove status
B: Target absorbs Caster's HP, Remove status
C: Remove, Remove status
D: Heal HP, Give Status, Remove status
E: Caster Absorbs Target's HP, Give Status, Remove status
F: Target Absorbs Target's HP, Give Status, Remove status

Note1: If the spell's power level is set at 00, there will be no damage, and the damage numerals will not appear and have no damage effect. (00 is only useful for Give/Remove status... if you put a higher power value, those spells will damage the target).

Note2: "Target absorbs Caster's HP" is actually a mixed effect of "Caster absorbs Target's HP" and "Heal". Healing in addition makes it do the opposite absorbing effect.

Note3: If there is no power level set for the spell, there will no damage/healing and/or any absorb effects won't do didily squat.

Magic Special effect

Bytes:

00 = Physical damage? (Pummel)
10 = See enemy's HP/MP/LV/Weaknesses (Scan)
11 = The Earth Wall effect (Golem)
12 = Morph enemy (Ragnarok)
13 = Makes target jump (Palidor)
15 = Hit everyone in target group except caster (if in target group); Damage/Heal points are dealt by dividing by the amount of targets. (Mantra)
16 = Removes caster from battle, fully restores target party (Spiraler)
18 = Party runs away if possible, does not matter who the target is (Warp)
19 = Does damage = to caster's HP to the caster and the enemy (Exploder)
1A = Does 1000 damage (Blow Fish)
1B = Attack/Healing move subtracts/adds HP according to caster's HP (Pearl Wind)
1C = Only works if enemy has Reflect status (Reflect???)
1D = Damages enemies whose levels are multiples of the last digit of your GP (L? Pearl)
1E = Damage in accordance to # of steps (Step Mine)
1F = Halves level (Dischord)
20 = Kills Caster, sets HP and MP to 0 and removes him/her from battle (Pep Up)
21 = Switches all status ailments or effects that are listed in bytes 11, 12, 13, and 14 if found (Rippler)
22 = Mucho extra damage if target enemy is same level as the caster (Stone)
23 = Death; kills undead too (Odin, Raiden, Cleave, X-Fer, X-Zone)
25 = Does not hit Floating enemies, ignores unblockable status in spell (Quake, Terrato, Takedown, Wild Fang, Magnitude8, and any other Earth-elemental spell in the game)
26 = Changes weakness to one particular element, all others ineffective, exact opposites of weak element absorbed (WallChange)
27 = Causes one to be counted as run away? Untested. (Escape)
28 = ??? (Mind Blast)
29 = Freeze target in ice (N. Cross)
2A = Level * spell strength determines damage (Flare Star)
2B = Switches target's row position \[untested\] (R. Polarity)
2C = Spell attacks eight times \[can't aim, autoaims at enemies\] (Launcher)
2D = Makes target take physical blows for target (Love Token)
2E = Takes opponent and drains HP \[Enemy only, makes spell miss every time for player controlled characters\] (Seize)
2F = ??? (Targetting)
30 = ??? (Suplex)
31 = Eliminates one random element \[Maybe this could be derandomized? Nah.\] (ForceField)
32 = Spell attacks four times \[same as 2C in aiming\] (Quadra Slam, Quadra Slice)
33 = ??? (Bababreath)
34 = Muddle, unblockable, no visual effect (Charm)
35 = Death; restores undead/character with Relic Ring (Doom)
36 = Combined with drain (1st part = 2 on 5th byte) and A2 on 4th byte, allows one to drain both HP and MP. Without one or the other, it causes the visual effect of the spell not to occur and do instant damage (or at least it looks like it if left without modifications at all). Doesn't have the intended effect unless the 2 bytes are changed to the previously specified as well (or to something that does the same, I guess) Complicated little thing. (Empowerer)
38 = Banish target from battle? (Sneeze)
39 = Banish target from battle? (Engulf)
3A = Possession of an enemy or ally until he/she dies \[I think, untested, but Zinger does work when used by player-controlled characters so...\] (Zinger)
3B = ??? (Evil Toot)
3C = ??? (Retort)
3E = Small HP drain, uncurable (Phantasm)
3F = ??? (Stunner)
40 = Drop HP to 1 (Fallen One)
43 = Target gets 2 turns in a row without interruption, effects only player-controlled characters (Quick)
44 = Eliminates Seize effect? (Discard)
45 = ??? (Clear)
FF = Nothing (Most spells)

Palette pointer values:
00: Edgar,Sabin
01: Locke
02: Terra
03: Strago, Relm
04: Cyan, Shadow
05: Umaro
06: Mog
07: Unused, all white.

(all the rest are appear to be weird, glitch palettes)

Element values:

Bits:

1: Fire
2: Ice
3: Lightning
4: Poison
5: Wind
6: Pearl
7: Earth
8: Water

Values:

(second half)

1: Fire
2: Ice
3: Fire, Ice
4: Lightning
5: Fire, Lightning
6: Ice, Lightning
7: Fire, Ice, Lightning
8: Poison
9: Fire, Poison
A: Ice, Poison
B: Fire, Ice, Poison
C: Lightning, Poison
D: Fire, Lightning, Poison
E: Ice, Lightning, Poison
F: Fire, Ice, Lightning, Poison

(first half)

1: Wind
2: Pearl
3: Wind, Pearl
4: Earth
5: Wind, Earth
6: Pearl, Earth
7: Wind, Pearl, Earth
8: Water
9: Wind, Water
A: Pearl, Water
B: Wind, Pearl, Water
C: Earth, Water
D: Wind, Earth, Water
E: Pearl, Earth, Water
F: Wind, Pearl, Earth, Water

Battle Command byte values:


00: Fight

01: Item

02: Magic

03: Morph

04: Revert

05: Steal

06: Capture

07: SwdTech

08: Throw

09: Tools

0A: Blitz

0B: Runic

0C: Lore

0D: Sketch

0E: Control

0F: Slot

10: Rage

11: Leap

12: Mimic

13: Dance

14: Row

15: Def.

16: Jump

17: X Magic

18: GP Rain

19: Summon

1A: Health

1B: Shock

1C: Possess

1D: MagiTek

FF: (blank)



Enemy Special attack attribute values:

Bits

bit 1-6= Effects (see below for the values)
bit 7= No HP damage if true
bit 8= Unknown bit

Bytes:

: Note: Add 40h to cause the enemies to do no damage with their special, and just induce a status effect. So if you wanted the enemies' special to use slow (12h) on you, ADD 40h, so it'd be 52h.

00: Blind
01: Zombie
02: Poison
03: Magitek (on/off)
04: Clear
05: Imp
06: Petrify
07: Dead
08: Condemned
09: Near Fatal
0A: Image
0B: Mute
0C: Berserk
0D: Muddle
0E: Seizure (doesn't show condition...)
0F: Psyche
10: Dance (uppermost in list)
11: Regen
12: Slow
13: Haste
14: Stop
15: Shell
16: Safe
17: Wall
18: Rage (uppermost in list)
19: Frozen
1A: Life 3
1B: Esper Morph
1C: Magic Cast
1D: Disappear (if you have HP left, then Berserked as well)
1E: Interceptor
1F: Float
20: Attack power 1
21: Attack power 2
22: Attack power 3
23: Attack power 4
24: Attack power 5
25: Attack power 6
26: Attack power 7
27: Attack power 8
28: Attack power 9
29: Attack power 10
2A: Attack power 11
2B: Attack power 12
2C: Attack power 13
2D: Attack power 14
2E: Attack power 15
2F: Attack power 16
30: Absorb HP
31: Absorb MP
32 - 3F= Unknown values.

Each attack power value is more powerful than the last one. They also rely on the monsters' base attack power, but I don't know how it's calculated so you might want to experiment with them to 'home in' on the range of power you want...

Magic values:



00: Fire

01: Ice

02: Bolt

03: Poison

04: Drain

05: Fire 2

06: Ice 2

07: Bolt 2

08: Bio

09: Fire 3

0A: Ice 3

0B: Bolt 3

0C: Break

0D: Doom

0E: Pearl

0F: Flare

10: Demi

11: Quartr

12: X-Zone

13: Meteor

14: Ultima

15: Quake

16: W Wind

17: Merton

18: Scan

19: Slow

1A: Rasp

1B: Mute

1C: Safe

1D: Sleep

1E: Muddle

1F: Haste

20: Stop

21: Bserk

22: Float

23: Imp

24: Rflect

25: Shell

26: Vanish

27: Haste 2

28: Slow 2

29: Osmose

2A: Warp

2B: Quick

2C: Dispel

2D: Cure

2E: Cure 2

2F: Cure 3

30: Life

31: Life 2

32: Antdot

33: Remedy

34: Regen

35: Life 3

36: Ramuh

37: Ifrit

38: Shiva

39: Siren

3A: Terrato

3B: Shoat

3C: Maduin

3D: Bismark

3E: Stray

3F: Palador

40: Tritoch

41: Odin

42: Raiden

43: Bahamut

44: Alexandr

45: Crusader

46: Ragnarok

47: Kirin

48: ZoneSeek

49: Carbunkl

4A: Phantom

4B: Sraphim

4C: Golem

4D: Unicorn

4E: Fenrir

4F: Starlet

50: Phoenix

51: Fire Skean

52: Water Edge

53: Bolt Edge

54: Storm

55: Dispatch

56: Retort

57: Slash

58: Quadra Slam

59: Empowerer

5A: Stunner

5B: Quadra Slice

5C: Cleave

5D: Pummel

5E: AuraBolt

5F: Suplex

60: Fire Dance

61: Mantra

62: Air Blade

63: Spiraler

64: Bum Rush

65: Wind Slash

66: Sun Bath

67: Rage

68: Harvester

69: Sand Storm

6A: Antlion

6B: Elf Fire

6C: Specter

6D: Land Slide

6E: Sonic Boom

6F: El Nino

70: Plasma

71: Snare

72: Cave In

73: Snowball

74: Surge

75: Cokatrice

76: Wombat

77: Kitty

78: Tapir

79: Whump

7A: Wild Bear

7B: Pois. Frog

7C: Ice Rabbit

7D: Super Ball

7E: Flash

7F: Chocobop

80: H-Bomb

81: 7-Flush

82: Megahit

83: Fire Beam

84: Bolt Beam

85: Ice Beam

86: Bio Blast

87: Heal Force

88: Confuser

89: X-Fer

8A: TekMissile

8B: Condemned

8C: Roulette

8D: CleanSweep

8E: Aqua Rake

8F: Aero

90: Blow Fish

91: Big Guard

92: Revenge

93: Pearl Wind

94: L.5 Doom

95: L.4 Flare

96: L.3 Muddle

97: Reflect???

98: L.? Pearl

99: Step Mine

9A: ForceField

9B: Dischord

9C: Sour Mouth

9D: Pep Up

9E: Rippler

9F: Stone

A0: Quasar

A1: GrandTrain

A2: Exploder

A3: Imp Song

A4: Clear

A5: Virite

A6: ChokeSmoke

A7: Schiller

A8: Lullaby

A9: Acid Rain

AA: Confusion

AB: Megazerk

AC: Mute

AD: Net

AE: Slimer

AF: Delta Hit

B0: Entwine

B1: Blaster

B2: Cyclonic

B3: Fire Ball

B4: Atomic Ray

B5: Tek Laser

B6: Diffuser

B7: WaveCannon

B8: Mega Volt

B9: Giga Volt

BA: Blizzard

BB: Absolute 0

BC: Magnitude8

BD: Raid

BE: Flash Rain

BF: TekBarrier

C0: Fallen One

C1: WallChange

C2: Escape

C3: 50 Gs

C4: Mind Blast

C5: N. Cross

C6: Flare Star

C7: Love Token

C8: Seize

C9: R.Polarity

CA: Targetting

CB: Sneeze

CC: S. Cross

CD: Launcher

CE: Charm

CF: Cold Dust

D0: Tentacle

D1: HyperDrive

D2: Train

D3: Evil Toot

D4: Grav Bomb

D5: Engulf

D6: Disaster

D7: Shrapnel

D8: Bomblet

D9: Heart Burn

DA: Zinger

DB: Discard

DC: Overcast

DD: Missile

DE: Goner

DF: Meteo

E0: Revenger

E1: Phantasm

E2: Dread

E3: Shock Wave

E4: Blaze

E5: Soul Out

E6: Gale Cut

E7: Shimsham

E8: Lode Stone

E9: Scar Beam

EA: BabaBreath

EB: LifeShaver

EC: Fire Wall

ED: Slide

EE: Battle

EF: Special

F0: Riot Blade

F1: Mirager

F2: Back Blade

F3: ShadowFang

F4: RoyalShock

F5: TigerBreak

F6: Spin Edge

F7: Sabre Soul

F8: Star Prism

F9: Red Card

FA: MoogleRush

FB: X-Meteo

FC: Takedown

FD: Wild Fang

FE: Lagomorph

FF: (Nothing)

Esper Level up bonus value list:


00: HP + 10%

01: HP + 30%

02: HP + 50%

03: MP + 10%

04: MP + 30%

05: MP + 50%

06: HP + 100% (!)

07: LV + 30% (?)

08: LV + 50% (?)

09: Strength +1

0A: Strength +2

0B: Speed +1

0C: Speed +2

0D: Stamina +1

0E: Stamina +2

0F: Mag.Pwr +1

10: Mag.Pwr +2

FF: (no bonus)


All other values are a glitch.

Item byte values:


00: Dirk

01: MithrilKnife

02: Guardian

03: Air Lancet

04: ThiefKnife

05: Assassin

06: Man Eater

07: SwordBreaker

08: Graedus

09: ValiantKnife

0A: MithrilBlade

0B: RegalCutlass

0C: Rune Edge

0D: Flame Sabre

0E: Blizzard

0F: ThunderBlade

10: Epee

11: BreakBlade

12: Drainer

13: Enhancer

14: Crystal

15: Falchion

16: Soul Sabre

17: Ogre Nix

18: Excalibur

19: Scimitar

1A: Illumina

1B: Ragnarok

1C: Atma Weapon

1D: Mithril Pike

1E: Trident

1F: Stout Spear

20: Partisan

21: Pearl Lance

22: Gold Lance

23: Aura Lance

24: Imp Halberd

25: Imperial

26: Kodachi

27: Blossom

28: Hardened

29: Striker

2A: Stunner

2B: Ashura

2C: Kotetsu

2D: Forged

2E: Tempest

2F: Murasame

30: Aura

31: Strato

32: Sky Render

33: Heal Rod

34: Mithril Rod

35: Fire Rod

36: Ice Rod

37: Thunder Rod

38: Poison Rod

39: Pearl Rod

3A: Gravity Rod

3B: Punisher

3C: Magus Rod

3D: Chocobo Brsh

3E: DaVinci Brsh

3F: Magical Brsh

40: Rainbow Brsh

41: Shuriken

42: Ninja Star

43: Tack Star

44: Flail

45: Full Moon

46: Morning Star

47: Boomerang

48: Rising Sun

49: Hawk Eye

4A: Bone Club

4B: Sniper

4C: Wing Edge

4D: Cards

4E: Darts

4F: Doom Darts

50: Trump

51: Dice

52: Fixed Dice

53: MetalKnuckle

54: MithrilClaw

55: Kaiser

56: Poison Claw

57: Fire Knuckle

58: DragonClaw

59: Tiger Fangs

5A: Buckler

5B: Heavy Shld

5C: MithrilShld

5D: Gold Shld

5E: Aegis Shld

5F: Diamond Shld

60: Flame Shld

61: Ice Shld

62: Thunder Shld

63: Crystal Shld

64: Genji Shld

65: TortoiseShld

66: Cursed Shld

67: Paladin Shld

68: Force Shld

69: Leather Hat

6A: Hair Band

6B: Plumed Hat

6C: Beret

6D: Magus Hat

6E: Bandana

6F: Iron Helmet

70: Coronet

71: Bard's Hat

72: Green Beret

73: Head Band

74: Mithril Helm

75: Tiara

76: Gold Helmet

77: Tiger Mask

78: Red Cap

79: Mystery Veil

7A: Circlet

7B: Regal Crown

7C: Diamond Helm

7D: Dark Hood

7E: Crystal Helm

7F: Oath Veil

80: Cat Hood

81: Genji Helmet

82: Thornlet

83: Titanium

84: LeatherArmor

85: Cotton Robe

86: Kung Fu Suit

87: Iron Armor

88: Silk Robe

89: Mithril Vest

8A: Ninja Gear

8B: White Dress

8C: Mithril Mail

8D: Gaia Gear

8E: Mirage Vest

8F: Gold Armor

90: Power Sash

91: Light Robe

92: Diamond Vest

93: Red Jacket

94: Force Armor

95: DiamondArmor

96: Dark Gear

97: Tao Robe

98: Crystal Mail

99: Czarina Gown

9A: Genji Armor

9B: Imp's Armor

9C: Minerva

9D: Tabby Suit

9E: Chocobo Suit

9F: Moogle Suit

A0: Nutkin Suit

A1: BehemothSuit

A2: Snow Muffler

A3: NoiseBlaster

A4: Bio Blaster

A5: Flash

A6: Chain Saw

A7: Debilitator

A8: Drill

A9: Air Anchor

AA: AutoCrossbow

AB: Fire Skean

AC: Water Edge

AD: Bolt Edge

AE: Inviz Edge

AF: Shadow Edge

B0: Goggles

B1: Star Pendant

B2: Peace Ring

B3: Amulet

B4: White Cape

B5: Jewel Ring

B6: Fairy Ring

B7: Barrier Ring

B8: MithrilGlove

B9: Guard Ring

BA: RunningShoes

BB: Wall Ring

BC: Cherub Down

BD: Cure Ring

BE: True Knight

BF: DragoonBoots

C0: Zephyr Cape

C1: Czarina Ring

C2: Cursed Ring

C3: Earrings

C4: Atlas Armlet

C5: Blizzard Orb

C6: Rage Ring

C7: Sneak Ring

C8: Pod Bracelet

C9: Hero Ring

CA: Ribbon

CB: Muscle Belt

CC: Crystal Orb

CD: Gold Hairpin

CE: Economizer

CF: Thief Glove

D0: Gauntlet

D1: Genji Glove

D2: Hyper Wrist

D3: Offering

D4: Beads

D5: Black Belt

D6: Coin Toss

D7: FakeMustache

D8: Gem Box

D9: Dragon Horn

DA: Merit Award

DB: Memento Ring

DC: Safety Bit

DD: Relic Ring

DE: Moogle Charm

DF: Charm Bangle

E0: Marvel Shoes

E1: Back Guard

E2: Gale Hairpin

E3: Sniper Sight

E4: Exp. Egg

E5: Tintinabar

E6: Sprint Shoes

E7: Rename Card

E8: Tonic

E9: Potion

EA: X-Potion

EB: Tincture

EC: Ether

ED: X-Ether

EE: Elixir

EF: Megalixir

F0: Fenix Down

F1: Revivify

F2: Antidote

F3: Eyedrop

F4: Soft

F5: Remedy

F6: Sleeping Bag

F7: Tent

F8: Green Cherry

F9: Magicite

FA: Super Ball

FB: Echo Screen

FC: Smoke Bomb

FD: Warp Stone

FE: Dried Meat

FF: Empty


Monster byte values:


00: Guard

01: Soldier

02: Templar

03: Ninja

04: Samurai

05: Orog

06: Mag Roader

07: Retainer

08: Hazer

09: Dahling

0A: Rain Man

0B: Brawler

0C: Apokryphos

0D: Dark Force

0E: Whisper

0F: Over-Mind

10: Osteosaur

11: Commander

12: Rhodox

13: Were-Rat

14: Ursus

15: Rhinotaur

16: Steroidite

17: Leafer

18: Stray Cat

19: Lobo

1A: Doberman

1B: Vomammoth

1C: Fidor

1D: Baskervor

1E: Suriander

1F: Chimera

20: Behemoth

21: Mesosaur

22: Pterodon

23: FossilFang

24: White Drgn

25: Doom Drgn

26: Brachosaur

27: Tyranosaur

28: Dark Wind

29: Beakor

2A: Vulture

2B: Harpy

2C: HermitCrab

2D: Trapper

2E: Hornet

2F: CrassHoppr

30: Delta Bug

31: Gilomantis

32: Trilium

33: Nightshade

34: TumbleWeed

35: Bloompire

36: Trilobiter

37: Siegfried

38: Nautiloid

39: Exocite

3A: Anguiform

3B: Reach Frog

3C: Lizard

3D: ChickenLip

3E: Hoover

3F: Rider

40: Chupon

41: Pipsqueak

42: M-TekArmor

43: Sky Armor

44: Telstar

45: Lethal Wpn

46: Vaporite

47: Flan

48: Ing

49: Humpty

4A: Brainpan

4B: Cruller

4C: Cactrot

4D: Repo Man

4E: Harvester

4F: Bomb

50: Still Life

51: Boxed Set

52: SlamDancer

53: HadesGigas

54: Pug

55: Magic Urn

56: Mover

57: Figaliz

58: Buffalax

59: Aspik

5A: Ghost

5B: Crawler

5C: Sand Ray

5D: Areneid

5E: Actaneon

5F: Sand Horse

60: Dark Side

61: Mad Oscar

62: Crawly

63: Bleary

64: Marshal

65: Trooper

66: General

67: Covert

68: Ogor

69: Warlock

6A: Madam

6B: Joker

6C: Iron Fist

6D: Goblin

6E: Apparite

6F: PowerDemon

70: Displayer

71: Vector Pup

72: Peepers

73: Sewer Rat

74: Slatter

75: Rhinox

76: Rhobite

77: Wild Cat

78: Red Fang

79: Bounty Man

7A: Tusker

7B: Ralph

7C: Chitonid

7D: Wart Puck

7E: Rhyos

7F: SrBehemoth

80: Vectaur

81: Wyvern

82: Zombone

83: Dragon

84: Brontaur

85: Allosaurus

86: Cirpius

87: Sprinter

88: Gobbler

89: Harpiai

8A: GloomShell

8B: Drop

8C: Mind Candy

8D: WeedFeeder

8E: Luridan

8F: Toe Cutter

90: Over Grunk

91: Exoray

92: Crusher

93: Uroburos

94: Primordite

95: Sky Cap

96: Cephaler

97: Maliga

98: Gigan Toad

99: Geckorex

9A: Cluck

9B: Land Worm

9C: Test Rider

9D: PlutoArmor

9E: Tomb Thumb

9F: HeavyArmor

A0: Chaser

A1: Scullion

A2: Poplium

A3: Intangir

A4: Misfit

A5: Eland

A6: Enuo

A7: Deep Eye

A8: GreaseMonk

A9: NeckHunter

AA: Grenade

AB: Critic

AC: Pan Dora

AD: SoulDancer

AE: Gigantos

AF: Mag Roader

B0: Spek Tor

B1: Parasite

B2: EarthGuard

B3: Coelecite

B4: Anemone

B5: Hipocampus

B6: Spectre

B7: Evil Oscar

B8: Slurm

B9: Latimeria

BA: StillGoing

BB: Allo Ver

BC: Phase

BD: Outsider

BE: Barb-e

BF: Parasoul

C0: Pm Stalker

C1: Hemophyte

C2: Sp Forces

C3: Nohrabbit

C4: Wizard

C5: Scrapper

C6: Ceritops

C7: Commando

C8: Opinicus

C9: Poppers

CA: Lunaris

CB: Garm

CC: Vindr

CD: Kiwok

CE: Nastidon

CF: Rinn

D0: Insecare

D1: Vermin

D2: Mantodea

D3: Bogy

D4: Prussian

D5: Black Drgn

D6: Adamanchyt

D7: Dante

D8: Wirey Drgn

D9: Dueller

DA: Psychot

DB: Muus

DC: Karkass

DD: Punisher

DE: Balloon

DF: Gabbldegak

E0: GtBehemoth

E1: Scorpion

E2: Chaos Drgn

E3: Spit Fire

E4: Vectagoyle

E5: Lich

E6: Osprey

E7: Mag Roader

E8: Bug

E9: Sea Flower

EA: Fortis

EB: Abolisher

EC: Aquila

ED: Junk

EE: Mandrake

EF: 1st Class

F0: Tap Dancer

F1: Necromancr

F2: Borras

F3: Mag Roader

F4: Wild Rat

F5: Gold Bear

F6: Innoc

F7: Trixter

F8: Red Wolf

F9: Didalos

FA: Woolly

FB: Veteran

FC: Sky Base

FD: IronHitman

FE: Io

FF: Pugs



Bosses list. (from Lord J)
00: Whelk_____ (shell)
01: Presenter_ (shell)
02: Mega Armor
03: Vargas____
04: TunnelArmr
05: Prometheus
06: GhostTrain
07: Dadaluma__
08: Shiva_____
09: Ifrit_____
0A: Number 024
0B: Number 128
0C: Inferno___
0D: Crane_____
0E: Crane_____
0F: Umaro_____
10: Umaro_____ (2nd dummy encounter?)
11: Guardian__
12: Guardian__
13: Air Force_
14: Tritoch___ (in the mines)
15: Tritoch___ (snow field)
16: FlameEater
17: AtmaWeapon
18: Nerapa____
19: SrBehemoth
1A: Kefka_____ (??... never encountered?)
1B: Tentacle__
1C: Dullahan__
1D: Doom Gaze_
1E: Chadarnook
1F: Curley____
20: Larry_____
21: Moe_______
22: Wrexsoul__
23: Hidon_____
24: KatanaSoul
25: L.30 Magic
26: Hidonite__
27: Doom______
28: Goddess___
29: Poltrgeist
2A: Kefka_____ (final Kefka)
2B: L.40 Magic
2C: Ultros____ (first encounter)
2D: Ultros____ (second encounter)
2E: Ultros____ (third encounter)
2F: Chupon____
30: L.20 Magic
31: Siegfried_ (Ghost train imposter)
32: L.10 Magic
33: L.50 Magic
34: Head______ (This is Whelk's head)
35: Whelk Head (This is Presenter's head... irony?)
36: Colossus__ (dummied boss)
37: CzarDragon (dummied boss)
38: Master Pug
39: L.60 Magic
3A: Merchant__
3B: B.Day Suit
3C: Tentacle__
3D: Tentacle__
3E: Tentacle__
3F: RightBlade
40: Left Blade
41: Rough_____
42: Striker___
43: L.70 Magic
44: Tritoch___ (the one you fight to get his Magicite)
45: Laser Gun_
46: Speck_____
47: MissileBay
48: Chadarnook
49: Ice Dragon
4A: Kefka_____ (Narshe invasion)
4B: Storm Drgn
4C: Dirt Drgn_
4D: Ipooh_____
4E: Leader____
4F: Grunt_____
50: Gold Drgn_
51: Skull Drgn
52: Blue Drgn_
53: Red Dragon
54: Piranha___
55: Rizopas___
56: Specter___
57: Short Arm_ (looks like golden Dragon, Poltergeist statue reborn, final battle part 1)
58: Long Arm__ " "
59: Face______ " "
5A: Tiger_____ (looks like golden Dragon, Doom statue reborn, final battle part 2)
5B: Tools_____ " "
5C: Magic_____ " "
5D: Hit_______ " "
5E: Girl______ (looks like golden Dragon, Goddess statue reborn, final battle part 3)
5F: Sleep_____ " "
60: Hidonite__
61: Hidonite__
62: Hidonite__
63: L.80 Magic
64: L.90 Magic
65: ProtoArmor
66: MagiMaster
67: SoulSaver_
68: Ultros____
69: Naughty___
6A: Phunbaba__ (fight w/Terra, no damage)
6B: Phunbaba__ (battle with your characters)
6C: Phunbaba__ (before Bababreath)
6D: Phunbaba__ (w/morph Terra after Bababreath)
6E: __________ (Kefka bidding Terra to burn everything w/ m-tek)
6F: __________ (Kefka taunting Sabin at imperial camp)
70: __________ (Cyan fighting at imperial camp)
71: Zone Eater
72: __________ (Gau returning from Veldt)
73: __________ (Kefka from Leo's final fight)
74: __________ (Kefka opening Esper world)
75: Officer___
76: Cadet_____
77: __________ (Kefka getting a magicite w/ x-zone)
78: __________
79: Soldier___ (the ones in Terra's flashback)
7A: __________
7B: __________
7C: __________
7D: Atma______
7E: __________
7F: __________
80: __________ (illegal... Ramuh? followings are Espers...)

**Part 21: Help**
Yeah, a lot of stuff in this game has been found above, but there is still quite a bunch of stuff that's left out. I need help in finding:

-Character spell level up data.

This is something I've tried searching a billion times for. It's not stored any way I can possibly think of. I think this data would be something really neat to mess with and I'd probably redo FF6 Hard Type if it works the way I hope it would...

-Special character data

You know, the kind of stuff that makes it so that you can't equip special characters and stuff. Like Banon for instance, you can't reequip him, but if you find this bit/byte and change it, you'd be able to. Other things may include a customizable battle menu, like with Gogo, and possibly allow other characters to learn Lore spells, etc.

-Enemy pre-defined special attack data.

-Character sprites

If you wanted to switch characters around, without having to go through the tedious character swapping and the dreaded palette which hasn't been found yet, I'm sure this stuff could help.

-Palettes

The save screen/party selection palette is stored yet another way (damn you Square. What's the point of having THREE separate palettes that are the same colors? Wasted space...). My Duncan in my Brachosaur fight demo had to use Banon's palette on the save screen because of this.

Finally, where might the character's palette pointers be stored for the overworld AND Save Screen/Party Select palettes? I'm sure this would be mighty helpful for people who want to change a character's palette to a different one in the game without changing the palette itself (and further messing up other characters that use it).

-I could always get more help on the enemy AI data. It's really confusing, and by far the most difficult to crack data I've found anywhere, every bit of info helps. If you wanna help, send me some mail, and I'll send out updates on people's findings.

Any other ideas on something YOU'RE trying to find? Give me a mail and I'll add it here.
