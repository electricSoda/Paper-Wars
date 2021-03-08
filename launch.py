from tkinter import *
import os
from PIL import Image, ImageTk
import webbrowser
import loading


# return exite
def exite():
    root.destroy()

def launched():
    global root
    #root
    root = Tk()
    os.chdir('C:\\teleport\\Code\\Paper Wars')
    import game
    os.chdir('C:\\teleport\\Code\\Paper Wars\\launch-assets')

    #setting width and height
    w = 800
    h = 700

    #set the color
    root.config(bg='white')

    #set icon
    root.iconbitmap(r'paper_icon.ico')

    #get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #minsize
    root.minsize(800, 700)

    #set title
    root.title('Paper Wars')

    #heading
    imageopen = Image.open("paper_icon.ico")
    headingimg = ImageTk.PhotoImage(imageopen)

    imageopen2 = Image.open("heading.png")
    headingimg2 = ImageTk.PhotoImage(imageopen2)

    head = Label(image=headingimg, background='white')
    head.place(x=0, y=0)

    head2 = Label(image=headingimg2)
    head2.place(x= 120, y=10)

    #functions for buttons
    def mwebsite():
        webbrowser.open('https://electricsoda.github.io/esteemsite/')

    def start():
        exite()
        loading.initiate()

    #launch
    openl = Image.open("launch.png")
    ll = ImageTk.PhotoImage(openl)

    launch = Button(image=ll)
    launch.config(background='green', activebackground='dark green', relief=GROOVE, command=start)
    launch.pack(side=BOTTOM)

    openw = Image.open("website.png")
    ww = ImageTk.PhotoImage(openw)

    website = Button(image=ww)
    website.config(background='turquoise', activebackground='blue', relief=GROOVE, command=mwebsite)
    website.pack(side=RIGHT, padx=50)

    openu = Image.open("updates.png")
    uu = ImageTk.PhotoImage(openu)

    updates = Button(image=uu)
    updates.config(background='yellow', activebackground='khaki3', relief=GROOVE)
    updates.pack(side=LEFT, padx=50)

    #mainloop
    root.mainloop()