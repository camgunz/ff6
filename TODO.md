# To Do

## Data

- ROM:
  - Esper Descriptions (0x0F3B40, variable strings)
  - Blitz Specifications (0x035E1C, 14 elements, 2 bytes: char, rotation)
  - Checksum
  - Monster AI (I feel like this could be pretty simple, actually)

- Save game:
  - Magic
  - Lores
  - Espers
  - Rages
  - Bushido (?)
  - Blitz (?)

## Engineering

- Serialization
  - It would be better for value checks to raise an exception; that way we can
    catch it and pass along the message so the user knows what's wrong.  Right
    now it's pretty opaque.

- Save games
  - Save games need a ROM to reference, which complicates the field structure
    a little
  - Save games should also be all slots; it shouldn't be parameterized.  It's
    too big a change otherwise.
