from tkinter import *
from tkinter.ttk import *

import lib

###
# Text field for patch file name
# Text field for patch description
# Button to build, apply, and launch emulator
###

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
        self.save_patch_button = Button(self)
        self.save_patch_button['text'] = 'Save patch'
        self.save_patch_button['command'] = self.save_patch
        self.launch_button = Button(self)
        self.launch_button['text'] = 'Save patch'
        self.launch_button['command'] = self.launch_emulator
        self.patch_file_name_label.grid(row=0, column=0, padx=2, pady=5)
        self.patch_file_name_entry.grid(row=0, column=1)
        self.patch_description_label.grid(row=1, column=0, padx=2, pady=5)
        self.patch_description_entry.grid(row=1, column=1)
        self.separator.grid(row=2, column=0, columnspan=2, ipady=5)
        self.save_patch_button.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=5,
            ipady=5
        )
        self.launch_button.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=5,
            ipady=5
        )

    def launch_emulator(self):
        subprocess.run([config['emulator'], config['project_rom']])

    def save_patch(self):
        config = lib.get_config()
        lib.build_rom()
        lib.build_rom('temp.smc')
        project_rom = rom.Rom.from_file(config['project_rom'])
        temp_rom = rom.Rom.from_file('temp.smc')
        patch = patch.from_roms(project_rom, temp_rom)
        patch.save()

def main():
    root = Tk()
    root.title('FF3 ROM Builder')
    root.minsize(240, 100)
    app = Application(master=root)
    app.mainloop()

main()

# vi: et sw=4 ts=4 tw=79
