import tkinter as tk
from PIL import Image
import os
from datetime import datetime

os.chdir('C:\\teleport\\Code\\Paper Wars\\game-assets')

root = tk.Tk()
file="openingchest.gif"

root.title('Daily Chest')

root.iconbitmap(r"paper_icon.ico")

root.resizable(False, False)

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

def stop_animation():
    root.after_cancel(anim)

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count=0
        gif_label.pack_forget()

        if os.path.exists('daily.txt'):
            with open('daily.txt', 'r') as D:
                D.read()
                print(D)

                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)
                if D == current_time:
                    pass

        reward = tk.Label(root, text="Congratulations! You've just earned: ")
        reward.pack()

        stop_animation()
    else:
        anim = root.after(50,lambda :animation(count))

gif_label = tk.Label(root,image="")
gif_label.pack()

start = tk.Button(root,text="OPEN YOUR CHEST!",command=lambda :animation(count))
start.pack()

root.mainloop()