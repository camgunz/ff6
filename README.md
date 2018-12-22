# FF6

This is a library for modifying a Final Fantasy VI ROM.  The idea is to modify
the ROM declaratively in order to facilitate collaboration and the use of
version control.

## Example

```python
from ff6.ff6rom import FF6ROM

rom = FF6ROM.deserialize_from_file('ff6.rom')
rom.inventory_items.dirk.battle_power = 200
rom.serialize_to_file('ff6-super-dagger.rom')
```

## Save Games

Basic save game support exists for the 1st slot, but because there is so little
data about the format it's limited more or less to character data.
