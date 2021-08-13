import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from abc import ABC, abstractmethod
from PIL import Image, ImageTk

class View(ABC):
    @abstractmethod
    def show_item(item_type, item, item_info):
        pass
    #and many more.


class TkinterView(View):
    def __init__(self):
        print("View loaded!")

        pass

    def call_back(self, controller):
        self.controller = controller

    def start_app(self):
        self.window = tk.Tk()
        self.window.title("QR Code Maker")
        self.window.geometry("680x450")
        self.window.grid()
        self.create_menu(self.window) # lays out the tabs
        self.create_tab1(self.tab1) # puts stuff in the tabs
        self.create_tab2(self.tab2)

        # more tabs
        self.window.mainloop()

    def show_item(item_type, item, item_info):
        pass


    def create_menu(self, window):

        self.tab_parent = ttk.Notebook(window)
        self.tab1 = ttk.Frame(self.tab_parent)
        self.tab2 = ttk.Frame(self.tab_parent)
        #self.tab3 = ttk.Frame(self.tab_parent)
        #self.tab4 = ttk.Frame(self.tab_parent)


        self.tab_parent.add(self.tab1, text="Read Me")
        self.tab_parent.add(self.tab2, text="Generate")
        #self.tab_parent.add(self.tab3, text="History")
        #self.tab_parent.add(self.tab4, text="Other")

        self.tab_parent.pack(expand=1, fill='both')

    def create_tab1(self, tab):
        self.controller.show_readme()

        self.controller.quit_app() # once this is called, this displays on all tabs!!!

    def create_tab2(self, tab):

        self.var1 = tk.StringVar()
        self.var1.set("https://www.default.com")

        self.label1 = tk.Label(tab, text="Make QR Code for:")
        self.label1.grid(row=0,column=0, sticky=tk.W+tk.N)

        self.entry1 = tk.Entry(tab, textvariable= self.var1)
        self.entry1.grid(row=0,column=1, sticky=tk.W+tk.S)


        self.button1 = tk.Button(self.tab2,
                                      text="Generate",
                                      command=lambda:self.generate_qr( self.var1.get() )) # requires lambda to pass a parameter!


        self.button1.grid(row=0,column=2, sticky=tk.E+tk.N)

        self.tab2.grid_rowconfigure(1, weight=1)
        self.tab2.grid_columnconfigure(1, weight=1)


    def show_readme(self, text):
        self.controller.show_readme()


    def show_quit_app(self):
        quitButton = tk.Button(
            self.window,
            text='Quit',
            command=lambda: self.window.destroy()
        ).pack() #expand=True

    def show_readme_box(self, text):
        #print("Attempting to print: " + text)
        self._clear_canvas(self.tab1)
        self.boxContents = tk.Message(self.tab1, justify="center", fg="#333333", text=text).pack()


    def show_qr(self, some_string, some_image):
        print("Showing QR")


        self.tab2.templogo = some_image

        #self.tab2.templogo = self.logo
        self.tab2.templogo = self.tab2.templogo.resize((200, 200), Image.ANTIALIAS)
        self.tab2.templogo = ImageTk.PhotoImage(self.tab2.templogo)
        # self.bokchoy = self.bokchoy.resize((34, 26), Image.ANTIALIAS)

        self.tab2.templogo_label = tk.Label(self.tab2, image = self.tab2.templogo)  # tab does NOT work with pad!
        self.tab2.templogo_label.image = self.tab2.templogo
        self.tab2.templogo_label.grid(row=1, column=1, padx=15, pady=15)  # .place(x=10, y=10)
        self.tab2.grid_rowconfigure(1, weight=1)
        self.tab2.grid_columnconfigure(1, weight=1)

        btn = tk.Button(self.tab2, text="Save QR Image", command=lambda: self.save_img(some_string))
        btn.grid(row=2, column=1, padx=15, pady=15)


    def save_img(self, some_string):
        print("Saving QR code")
        self.controller.save_img(some_string)



    def generate_qr(self, some_string):
        print("Generate Button Pressed!")

        if not self._check_empty(some_string):
            messagebox.showinfo("Application Error", "Empty Textbox")
        else:
            try:
                self.controller.generate_qr(some_string)
            except Exception as e:
                messagebox.showinfo("Error", e)


    def _clear_canvas(self, window):
        for widget in window.winfo_children():
            widget.destroy()


# modified from in-class example
    def _check_empty(self, var1, var2=None, var3=None):

        blank_textbox_count = 0

# in my example, I do a get() call with a lambda, so these are treated as pure variables not tk variables
        if var1 == "":
            blank_textbox_count = blank_textbox_count + 1

        if var2 == "":
            blank_textbox_count = blank_textbox_count + 1 # this wont be called

        if var3 == "":
            blank_textbox_count = blank_textbox_count + 1 # this wont be called

        if blank_textbox_count >= 1:
            return False
        return True