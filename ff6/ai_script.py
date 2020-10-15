class UniqueSpell:

    def __init__(self, spell):
        self.spell = spell


class RandomSpell:

    def __init__(self, spell1=None, spell2=None, spell3=None):
        self.spell1 = spell1
        self.spell2 = spell2
        self.spell3 = spell3


###
# F0: Random spell
#
#     4 bytes syntax: F0 (spell 1) (spell 2) (spell 3)
#     Randomly execute one of the three available spells to use.
#
# F1: Set targets
#
#     2 bytes syntax: F1 (target)
#     The instruction changes the target for the next executed spell. It can
#     fail, if the target is invalid.
#
#     (target) values:
#         00: Terra
#         01: Locke
#         02: Cyan
#         03: Shadow
#         04: Edgar
#         05: Sabin
#         06: Celes
#         07: Strago
#         08: Setzer
#         09: Relm
#         0A: Mog
#         0B: Gau
#         0C: Gogo
#         0D: Umaro
#         0E: Banon
#         0F: Leo
#         30: Monster ID 1
#         31: Monster ID 2
#         32: Monster ID 3
#         33: Monster ID 4
#         34: Monster ID 5
#         35: Monster ID 6
#         36: Self
#         37: All monsters (excluding itself)
#         38: All monsters
#         39: Random monster (excluding itself)
#         3A: Random monster
#         3B: All characters with Dead status
#         3C: Random character with Dead status
#         3D: All monsters with Dead status
#         3E: All monsters with Dead status
#         3F: All characters with Wall status
#         40: Random character with Wall status
#         41: All monsters with Wall status
#         42: Random monster with Wall status
#         43: All characters
#         44: Random character
#         45: Last attacking character/monster
#         46: All characters and monsters
#         47: Default spell target
#         48: Character ID 1
#         49: Character ID 2
#         4A: Character ID 3
#         4B: Character ID 4
#         4C: All targets or one random target (excluding itself)
#         4D: Last target of "Targetting" spell
#
# F2: Formation change
#
#     4 bytes syntax: F2 (unknown) (formation low byte) (formation high byte)
#     The instruction changes the actual enemy formation to a new one. It won't
#     work correctly if the monsters and formations aren't compatible.  The
#     highest bit of the formation determinates if the new monsters HP will be
#     set to maximum.
#
# F3: Display message
#
#     3 bytes syntax: F3 (message low byte) (message high byte)
#     Display a message.
#
# F4: Use command
#
#     4 bytes syntax: F4 (command 1) (command 2) (command 3)
#     The instruction will use a random character command, based in three
#     available commands. The majority of the commands don't work and have
#     glitches. The instruction must be used with care.
#
# F5: Change enemies
#
#     4 bytes syntax: F5 (animation) (HP flags) (monsters bitfield)
#     The instruction changes between active and inactive enemies in battle
#     without changing the monster formation.
#
#     (HP flags) values:
#         00: Unhide and sets max HP
#         01: Hide and nulls HP
#         02: Unhide without changing HP
#         03: Hide and sets max MP
#         04: Hide without changing HP
#
# F6: Throw or use items
#
#     4 bytes syntax: F6 (Usage flag) (Item 1) (Item 2)
#     The instruction throw or use items, based in the <Usage flag>. One of the
#     two available items is choose at random.
#
# F7: Special event
#
#     2 bytes syntax: F7 (Event ID)
#     Triggers a special event.
#
# F8: Arithmetic Variable manipulation
#
#     3 bytes syntax: F8 (Variable ID) (Operation)
#     The instruction change variables values based in arithmetic operations.
#     The two highest bits of (Operation) determinate the operation. The other
#     six bytes determinate the value for the operation.
#
#     Two highest bits of (Operation) values:
#         00 bits: Set variable
#         01 bits: Set variable
#         10 bits: Add variable
#         11 bits: subtract variable
#
# F9: Bit Variable manipulation
#
#     4 bytes syntax: F9 (operation) (variable ID) (related bits)
#     The instruction changes variables based in bits operations.
#
#     (Operation) values:
#         #$00: Toggle bits
#         #$01: Set bits
#         #$02: Clear bits
#
# FA: Use animation
#
#     4 bytes syntax: FA (animation) (monsters bitfield) (complement)
#     The instruction executes a graphical animation for the specified enemies.
#
#     (animation) values:
#         00: Monster stays, flashes red
#         01: Monster moves back, 1 step, slow
#         02: Monster moves forward, 1 step, slow
#         03: Monster moves back, 1 step, fast
#         04: Monster moves forward, 1 step, fast
#         05: Characters run to the right
#         06: Characters run to the left
#         07: Monster moves back, 3 steps, fast
#         08: Monster moves forward, 3 steps, fast
#         09: Plays a sound. The sound is determined by (complement)
#         0A: Head appears and screen shakes, like in the final battle against
#         Kefka.
#         0B: Monster stays, flashes
#         0C: monster stays, flashes
#         0D: Boss death animation
#
# FB: Miscellaneous
#
#     4 bytes syntax: FB (opcode) (target) (complement)
#     The instruction does different miscellaneous operations, based in
#     (Opcode).
#
#     (Opcode) values:
#         00: Sets the battle timer to zero.
#         01: Target becomes invincible.
#         02: Ends the battle.
#         03: Adds Gau to party.
#         04: Sets the global timer to zero.
#         05: Cancels invincibility.
#         06: Target becomes targettable.
#         07: Target becomes untargettable.
#         08: Unknown.
#         09: Ends combat.
#         0A: Nothing.
#         0B: Set permanent status. Status are set by (Complement).
#         0C: Unset permanent status. Status are unset by (Complement).
#
# FC: Conditional execution
#
#     4 bytes syntax: FC (condition) (complement 1) (complement 2)
#     Executes all instructions between FC and FE instructions, if the
#     conditions are meet. Otherwise, they are ignored.  The conditions can
#     change the target of spells. It is recommended to use the F1 instruction
#     inside the conditional instructions.
#
#     (condition) values:
#         01: hit by command ID. Syntax: FC 01 (command) (unknown)
#         02: hit by spell ID. Syntax: FC 02 (command) (unknown)
#         03: hit by item ID. Syntax: FC 03 (item) (unknown)
#         04: hit by elements type. Syntax: FC 04 (bitfield) (unknown)
#         05: HP is decreased. Syntax: FC 05 (unknown) (unknown)
#         06: (target) HP is below (HP) * 128. Syntax: FC 06 (target) (HP)
#         07: (target) MP is below (MP). Syntax: FC 07 (target) (MP)
#         08: (target) has status (status). Syntax: FC 08 (target) (status)
#         09: (target) doesn't have status (status). Syntax: FC 09 (target)
#         (status)
#         0A: never executes.
#         0B: battle timer is greater than (time). Syntax: FC 0B (time)
#         (unknown)
#         0C: variable value is less than (value). Syntax: FC 0C (variable)
#         (value)
#         0D: variable value is equal or greater than (value). Syntax: FC 0D
#         (variable) (value)
#         0E: (target) level is less than (level). Syntax: FC 0E (target)
#         (level)
#         0F: (target) level is equal or greater than (level). Syntax: FC 0F
#         (target) (level)
#         10: only one kind of enemy alive. Syntax: FC 10 (unknown) (unknown)
#         11: specified monsters are alive. Syntax: FC 11 (monsters bitfield)
#         (unknown)
#         12: specified monsters are dead. Syntax: FC 12 (monster bitfield)
#         (unknown)
#         13: number of characters or monsters are equal or lesser than
#         (number). Syntax: FC 13 (character/monsters) (number)
#         14: specified bits are set in variable. Syntax: FC 14 (variable)
#         (bitfield)
#         15: specified bits are unset in variable. Syntax: FC 15 (variable)
#         (bitfield)
#         16: global timer is greater than (time). Syntax: FC 16 (time)
#         (unknown)
#         17: target is valid. Syntax: FC 17 (target) (unknown)
#         18: Gau isn't in party. Syntax: FC 18 (unknown) (unknown)
#         19: monster is (monster ID). Syntax: FC 19 (monster ID) (unknown)
#         1A: (target) is weak against elements. Syntax: FC 1A (target)
#         (elements bitfield)
#         1B: battle formations is equal to (formation). Syntax: FC 1B
#         (formation low byte) (formation high byte)
#         1C: always execute. Syntax: FC 1C (unknown) (unknown)
#
# FD: Wait next turn
#
#     1 byte syntax: FD
#     Wait for the monster next turn and resets targeting. It doesn't work
#     correctly inside of conditional instructions.
#
# FE: End of conditional
#
#     1 byte syntax: FE
#     Ends the conditional instruction FC and resets targeting.
#
# FF: End of script
#
#     1 byte syntax: FF
#     The instruction is used to identify the end of the script for the monster.
###
