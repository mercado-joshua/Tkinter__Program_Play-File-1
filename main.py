#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

from glob import glob
import os
from pymediainfo import MediaInfo

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""
    #===========================================
    def __init__(self, title, icon, theme):
        super().__init__()
        self.style = ttk.Style(self)
        self.resizable(False, False)
        self.title(title)
        self.iconbitmap(icon)
        self.style.theme_use(theme)

        self.init_UI()
        self.init_events()

    # INITIALIZER ==============================
    @classmethod
    def create_app(cls, app):
        return cls(app['title'], app['icon'], app['theme'])

    #===========================================
    def init_events(self):
        self.listbox.bind('<Double-Button>', self.evt_play)
        self.listbox.bind('<<ListboxSelect>>', self.evt_see_properties)

    def init_UI(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.main_frame, text='Select a file', justify=tk.LEFT)
        self.label.pack(anchor=tk.W, fill=tk.X, expand=True)

        """
        you can specify any file extension you want to be displayed in the listbox.
        """
        list_of_file = glob(r'*.mp4')
        self.listbox = tk.Listbox(self.main_frame)
        for file in list_of_file:
            self.listbox.insert(0, file)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # METHODS -----------------------------------
    def filename(self):
        filename = self.listbox.get(self.listbox.curselection())
        return filename

    def evt_play(self, event):
        os.startfile(self.filename())

    def evt_see_properties(self, event):
        size = os.path.getsize(self.filename())
        duration = MediaInfo.parse(self.filename())
        ms = int(duration.tracks[0].duration / 3600) * 4
        self.label['text'] = f'Size: {size} Mb\nDuration: {ms} seconds'

#===========================
# Start GUI
#===========================

def main(config):
    app = App.create_app(config)
    app.mainloop()

if __name__ == '__main__':
    main({
        'title' : 'Play File with OS mod version 1.0',
        'icon' : 'python.ico',
        'theme' : 'clam'
        })