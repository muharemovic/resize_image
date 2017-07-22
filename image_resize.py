#!/usr/bin/python3
# Author: Ramiz Muharemovic
# https://github.com/muharemovic
import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image

class Foto():

    def __init__(self, gui):
        self.gui = gui
        self.var1 = IntVar()
        self.small = Radiobutton(gui, text="Small (800 x 600)      ", variable=self.var1,value = 1, bg ='#FF5733',font=("Ubuntu", 18) ).place( x=20, y=10 + 4 * 10, width=320, height=40)
        self.medium = Radiobutton(gui, text="Medium(1024 x 768)", variable=self.var1,value = 2, bg ='#7FB3D5',font=("Ubuntu", 18) ).place(x=20, y=10 + 4 * 30, width=320, height=40)
        self.large = Radiobutton(gui, text="Large(1920 x 1080)", variable=self.var1,value = 3,  bg ='#17A589',font=("Ubuntu", 18) ).place(x=20, y=10 + 4 * 50, width=320, height=40)
        self.costum = Radiobutton(gui, text="Custum                 X           ", variable=self.var1,value = 4, bg ='#FDEBD0',font=("Ubuntu", 18)).place(x=20, y=10 + 4 * 70, width=370, height=40)
        self.e = StringVar()
        self.ent= Entry(gui, width=50, font=("Ubuntu", 18),textvariable = self.e).place(x=200, y=15 + 4 * 70, width=70, height=30)
        self.c = StringVar()
        self.entA = Entry(gui, width=50, font=("Ubuntu", 18),textvariable = self.c).place(x=310, y=15 + 4 * 70, width=70, height=30)
        self.l = Label(gui,text="Quality",font=("Ubuntu", 16) ).place(x=60, y=15 + 4 * 82, width=90, height=30)
        self.d = IntVar(value='100')
        self.quality = Spinbox(gui, from_=0, to=100,textvariable = self.d,font=("Ubuntu", 13)).place(x=145, y=15 + 4 * 82, width=52, height=33)
        self.g = StringVar(value='JPEG')
        self.forma = ttk.Combobox(gui, values=('JPEG','PNG'),textvariable = self.g ,font=("Ubuntu", 13)).place(x=300, y=15 + 4 * 82, width=70, height=30)
        self.lf = Label(gui, text="Format", font=("Ubuntu", 16)).place(x=220, y=15 + 4 * 82, width=70, height=30)
        self.openphoto = Button(gui,text="Open Photo",bg ='#A2D9CE',font=("Ubuntu", 11),command = self.resize_photo).place(x=65, y=120 + 4 * 70, width=100, height=40)
        self.openfolder = Button(gui,text="Open Folder",bg ='#F7DC6F',font=("Ubuntu", 11),command = self.resize_folder).place(x=230, y=120 + 4 * 70, width=100, height=40)


    def resize_photo(self):

        filename =  tk.filedialog.askopenfilename(initialdir=os.path.expanduser('~'), title="Select file",filetypes=[("Image", "*.jpg"), ("Image", "*.png")])
        photo = Image.open(filename)
        f, e = os.path.splitext(filename)

        if self.var1.get() == 1:
                    photo.resize((800, 600)).save(f + ' resized.{}'.format(self.g.get()), self.g.get(), quality=self.d.get())
        elif self.var1.get() == 2:
                    photo.resize((1024, 768)).save(f + ' resized.{}'.format(self.g.get()), self.g.get(), quality=self.d.get())
        elif self.var1.get() == 3:
                    photo.resize((1920, 1080)).save(f + ' resized.{}'.format(self.g.get()), self.g.get(), quality=self.d.get())
        elif self.var1.get() == 4:
                    photo.resize((int(self.e.get()), int(self.c.get()))).save(f + ' resized.{}'.format(self.g.get()), self.g.get(), quality=self.d.get())

        messagebox.showinfo("Resize Image", "DONE!")

    def resize_folder(self):

        filename = tk.filedialog.askdirectory(initialdir=('~'), title="Select file")
        a = filename + "/"
        dirs = os.listdir(a)
        for item in dirs:
            if os.path.isfile(a + item):
                photo = Image.open(a  + item)
                f, e = os.path.splitext(a  + item)
                if self.var1.get() == 1:
                    photo.resize((800, 600)).save(f + ' resized.{}'.format(self.g.get()), self.g.get(), quality=self.d.get())
                elif self.var1.get() == 2:
                    photo.resize((1024, 768)).save(f + ' resized.{}'.format(self.g.get()), self.g.get(), quality=self.d.get())
                elif self.var1.get() == 3:
                    photo.resize((1920, 1080)).save(f + ' resized.{}'.format(self.g.get()), self.g.get(), quality=self.d.get())
                elif self.var1.get() == 4:
                    photo.resize((int(self.e.get()), int(self.c.get()))).save(f + ' resized.{}'.format(self.g.get()), self.g.get(), quality=self.d.get())
        messagebox.showinfo("Resize Image","DONE!" )


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("410x460")
    root.title("Resize Image")
    app = Foto(root)
    root.mainloop()

