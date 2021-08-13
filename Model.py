from loadtext import LoadTextFile
import qrcode

class ModelBasic(object):

    def __init__(self):
        print("Model loaded!")
        self._qr_string = ''
        # qr history list
        self._readme = LoadTextFile("readme.txt")
        #self.create_items()

    @property
    def readme(self):
        self._readme = LoadTextFile("readme.txt") # the readme is immutable
        return self._readme

    @readme.setter
    def readme(self, text="readme.txt"):
        #print("Loading Readme")
        self._readme = LoadTextFile(text)
        # from loadtext import LoadTextFile

    def read_readme(self):
        return self._readme

    @property
    def qr_string(self):
        return _qr_string

    @qr_string.setter
    def qr_string(self, text=""):
        self._qr_string = text

    def make_qr(self, some_string):
        # this will call the setter, and then the getter!
        # error checking happened already, in the view
        print("Making QR code for: " + some_string)
        self._qr_string = some_string
        img = qrcode.make(self._qr_string)
        return img

        # img.save('MyQRCode-' + dt + '.png')


'''
# existing Model stuff:
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self, name, price, quantity):
        basic_backend.create_item(name, price, quantity)

    def create_items(self, items):
        basic_backend.create_items(items)

    def read_item(self, name):
        return basic_backend.read_item(name)

    def read_items(self):
        return basic_backend.read_items()

    def update_item(self, name, price, quantity):
        basic_backend.update_item(name, price, quantity)

    def delete_item(self, name):
        basic_backend.delete_item(name)'''