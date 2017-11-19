# FF6

## Installation

Copy `project-base.ini` to `project.ini`

Configure the settings in `project.ini` appropriately.

You will also need [FF3usME](http://www.angelfire.com/pq/jumparound/)

## Usage

Double-click `main.py` to start off.  This will bring up the ROM Builder.

`Rebuild From Patch List` rebuilds the ROM starting from the base FF6 rom, and
using all listed patches.  You probably want to start here.

`Edit ROM` brings up FF3usME with your current changes.  Edit away in here.

`Launch Game` brings up your emulator running your ROM with your current
changes.

`Save Patch` uses the fields `File name` and `Description` to build a new patch
from your current changes, and then rebuilds a new ROM from the new patch list.

Think of it like version control:

- `git checkout` / `git reset --hard`: `Rebuild From Patch List`
- `git commit`: `Save Patch`

## Caveats

Patches usually depend on every patch that comes before; you generally can't
pull a patch out of the history unless you pull all patches after that patch
too.  This isn't always the case, but it's caused problems before.

In general, don't worry about editing the patch history.  Just make a new patch with the changes you want and forget about the past.
