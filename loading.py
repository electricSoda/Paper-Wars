import tkinter as tk
from PIL import Image
import time
import os
import game

def initiate():
    cheese = 0
    root = tk.Tk()
    os.chdir('C:\\teleport\\Code\\Paper Wars')
    file="paper.gif"


    root.iconbitmap(r'paper_icon.ico')
    root.title('Loading...')
    root.resizable(False,False)

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

    bum = 0
    dotscount = 0
    dots = ['', '.', '..', '...']
    ldingtxt = 'Loading' + dots[dotscount]
    loading = tk.Label(root, text=ldingtxt)
    loading.config(font=('KBZipaDeeDooDah', 25))
    loading.pack()

    gif_label = tk.Label(root,image="")
    gif_label.pack()

    count = 0
    anim = None
    Load = True

    def terminate123():
        root.destroy()
        game.GameMenu('Paper Wars').startM()

    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = root.after(50, lambda: animation(count))

    while Load:
        if cheese <= 150:
            im2 = im[count]

            if bum==25:
                bum = 0
                if dotscount == 3:
                    ldingtxt = 'Loading' + dots[dotscount]
                    loading.config(text=ldingtxt)
                    dotscount = 0
                else:
                    ldingtxt = 'Loading' + dots[dotscount]
                    loading.config(text=ldingtxt)
                    dotscount = dotscount + 1
            else:
                bum = bum + 1

            gif_label.configure(image=im2)
            count += 1
            if count == frames:
                count = 0
            anim = root.after(50,lambda :animation(count))

            time.sleep(0.01)

            cheese = cheese + 1

            root.update()
        else:
            terminate123()

#initiate()