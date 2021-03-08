#import
from tkinter import *
from PIL import Image, ImageTk
import os
import time
from tkinter import messagebox

game = True

class GameMenu:
    os.chdir('C:\\teleport\\Code\\Paper Wars\\game-assets')

    def __init__(self, title):
        self.title = title

    def chest(self):
        import daily

        daily.chest()

    def startM(self):
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                game = False
                time.sleep(1)
                root.destroy()

        # root
        root = Tk()

        # set the color
        root.config(bg='white')

        # set icon
        root.iconbitmap(r'paper_icon.ico')

        # root size
        root.geometry('1000x700')

        #non resizable
        root.resizable(False, False)

        # set title
        root.title(self.title)

        # upload images
        o1 = Image.open('battle.png')
        o2 = Image.open('beta.png')
        o3 = Image.open('characters.png')
        o4 = Image.open('chest.png')
        o5 = Image.open('play.png')
        o6 = Image.open('settings.png')
        o7 = Image.open('stats.png')
        o8 = Image.open('shop.png')

        oo1 = ImageTk.PhotoImage(o1)
        oo2 = ImageTk.PhotoImage(o2)
        oo3 = ImageTk.PhotoImage(o3)
        oo4 = ImageTk.PhotoImage(o4)
        oo5 = ImageTk.PhotoImage(o5)
        oo6 = ImageTk.PhotoImage(o6)
        oo7 = ImageTk.PhotoImage(o7)
        oo8 = ImageTk.PhotoImage(o8)

        b1 = Button(image=oo1)
        b1.config(background='turquoise', relief=GROOVE)
        b1.place(x=0, y=200)

        b2 = Button(image=oo3)
        b2.config(background='turquoise', relief=GROOVE)
        b2.place(x=450, y=195)

        b3 = Button(image=oo5)
        b3.config(background='turquoise', relief=GROOVE)
        b3.pack()

        b4 = Button(image=oo2)
        b4.config(background='turquoise', relief=GROOVE, state='disabled')
        b4.pack(side=BOTTOM)

        b5 = Button(image=oo4)
        b5.config(background='turquoise', relief=GROOVE)
        b5.pack(side=BOTTOM)

        b6 = Button(image=oo6)
        b6.config(background='turquoise', relief=GROOVE)
        b6.pack(side=BOTTOM)

        b7 = Button(image=oo7)
        b7.config(background='turquoise', relief=GROOVE)
        b7.pack(side=BOTTOM)

        b8 = Button(image=oo8)
        b8.config(background='turquoise', relief=GROOVE, command=chest)
        b8.pack(side=BOTTOM)

        #mainloop
        while game:
            root.protocol("WM_DELETE_WINDOW", on_closing)
            root.update()
            time.sleep(0.01)

GameMenu('Paper Wars').startM()