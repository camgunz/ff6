import subprocess
import threading

from tkinter import *
from tkinter.ttk import *

import lib

from rom import ROM
from patch import Patch

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.patch_file_name = StringVar()
        self.patch_description = StringVar()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.patch_file_name_entry = Entry(
            self,
            textvariable=self.patch_file_name
        )
        self.patch_file_name_label = Label(self, text='File name:')
        self.patch_description_entry = Entry(
            self,
            textvariable=self.patch_description
        )
        self.patch_description_label = Label(self, text='Description:')
        self.separator = Separator(self)
        self.edit_button = Button(self)
        self.edit_button['text'] = 'Edit ROM'
        self.edit_button['command'] = self.edit_rom
        self.save_patch_button = Button(self)
        self.save_patch_button['text'] = 'Save Patch'
        self.save_patch_button['command'] = self.save_patch
        self.rebuild_button = Button(self)
        self.rebuild_button['text'] = 'Rebuild From Patch List'
        self.rebuild_button['command'] = self.rebuild_rom
        self.launch_button = Button(self)
        self.launch_button['text'] = 'Launch Game'
        self.launch_button['command'] = self.launch_emulator
        self.patch_file_name_label.grid(
            row=0,
            column=0,
            padx=2,
            pady=5
        )
        self.patch_file_name_entry.grid(
            row=0,
            column=1,
            columnspan=2,
        )
        self.patch_description_label.grid(
            row=1,
            column=0,
            padx=2,
            pady=5
        )
        self.patch_description_entry.grid(
            row=1,
            column=1,
            columnspan=2,
        )
        self.separator.grid(row=2, column=0, ipady=5)
        self.edit_button.grid(
            row=3,
            column=0,
            pady=5,
            ipady=5
        )
        self.save_patch_button.grid(
            row=3,
            column=1,
            pady=5,
            ipady=5
        )
        self.rebuild_button.grid(
            row=3,
            column=2,
            pady=5,
            ipady=5
        )
        self.launch_button.grid(
            row=4,
            column=0,
            columnspan=3,
            pady=5,
            ipady=5
        )

    def run_editor(self):
        config = lib.get_config()
        subprocess.run([config['editor'], config['project_rom']])

    def launch_emulator(self):
        config = lib.get_config()
        subprocess.run([config['emulator'], config['project_rom']])

    def edit_rom(self):
        threading.Thread(target=self.run_editor).start()

    def save_patch(self):
        config = lib.get_config()
        base_rom = lib.build_rom()
        project_rom = ROM.from_file(config['project_rom'])
        patch = Patch.from_roms(
            self.patch_file_name.get(),
            False,
            True,
            self.patch_description.get(),
            base_rom,
            project_rom
        )
        patch.save()
        patched_rom = lib.build_rom()
        patched_rom.save_to_file(config['project_rom'])

    def rebuild_rom(self):
        config = lib.get_config()
        rom = lib.build_rom()
        rom.save_to_file(config['project_rom'])

    def emulate(self):
        threading.Thread(target=self.launch_emulator).start()

def main():
    root = Tk()
    root.title('FF3 ROM Builder')
    root.minsize(240, 100)
    app = Application(master=root)
    app.mainloop()

main()

# vi: et sw=4 ts=4 tw=79
