#import tkinter as tk

def LoadTextFile(file="readme.txt"):
    fileobject = open(file, "r")
    content = fileobject.read()
    fileobject.close()
    return content

