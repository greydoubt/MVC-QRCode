import mvc_exceptions as mvc_exc
from Model import ModelBasic
from View import View
from loadtext import LoadTextFile

import tkinter as tk
from tkinter.filedialog import asksaveasfile

class Controller(object):

    def __init__(self, model, view):
        print("Controller loaded!")
        self.model = model
        self.view = view
        self.view.call_back(self)
        # has to be last method
        self.view.start_app()

    def show_text(self):
        pass

    def show_readme(self):
        try:
            readme = self.model.read_readme()
            self.view.show_readme_box(readme)
        except mvc_exc.ItemNotStored as e:
            self.view.display_missing_item_error(readme, e)

    def generate_qr(self, some_string):
        qr = self.model.make_qr(some_string) # sends the string to model
        # now we have an image, we send it back up to view
        self.view.show_qr(some_string, qr)

    def save_img(self, some_string):

        qr = self.model.make_qr(some_string)

        file = tk.filedialog.asksaveasfile(initialfile = some_string + '.png',  # data + '-' + dt + '
                                       mode='wb',
                                       # because PNG is bytes, need to set b as a parameter (otherwise anticipates a string)
                                       defaultextension=".png")
        if file:
            print("Saving QR Code to file: " + some_string + '.png')
            qr.save(file)


    def quit_app(self):
        self.view.show_quit_app()