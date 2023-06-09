from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Cool Cash")
window.geometry("300x266")
canvas = Canvas(master=window, height=600, width=600)
canvas.place(x=0, y=0)
background = Image.open("background.png")
resized_bg = background.resize((300, 266))
bg_img = ImageTk.PhotoImage(resized_bg)
bg = canvas.create_image(0,0, image=bg_img, anchor=NW)

overlay = Image.open("overlay.png")
resized_ovr = overlay.resize((350, 300))
ovr_img = ImageTk.PhotoImage(resized_ovr)
ovr = canvas.create_image(-16,-12, image=ovr_img, anchor=NW)

#cusor event
def enter():
    canvas.config(cursor="hand2")

def leave():
    canvas.config(cursor="")

tagname = "event"
def cmd(event):
    print("Programmed")
    window2 = Tk()
    window2.title("Savings and Current")
    window2.geometry("300x266")
    window2.mainloop()

#-------------------------- Home Page -------------------------------------#
img2 = Image.open("withdraw.png")
re_img2 = img2.resize((60, 55))
bg_img2 = ImageTk.PhotoImage(re_img2)
button2 = canvas.create_image(80,200, image=bg_img2, tag=tagname)
canvas.tag_bind(tagname, "<Enter>", lambda event:enter())
canvas.tag_bind(tagname, "<Leave>", lambda event:leave())
canvas.tag_bind(button2, "<Button-1>", cmd)

img3 = Image.open("send.png")
re_img3 = img3.resize((73, 63))
bg_img3 = ImageTk.PhotoImage(re_img3)
button3 = canvas.create_image(155, 200, image=bg_img3)

img4 = Image.open("transfer.png")
re_img4 = img4.resize((58, 58))
bg_img4 = ImageTk.PhotoImage(re_img4)
button4 = canvas.create_image(230, 200, image=bg_img4)

logo = Image.open("cool_logo.png")
logo_resize = logo.resize((90, 90))
logo_img = ImageTk.PhotoImage(logo_resize)
cool_logo = canvas.create_image(230, 90, image=logo_img)

#----------------------------- Labels -------------------------------
total_B_lbl = Label(text="Total balance", bg="white", fg="black", font=("Ariel", 15, "bold"))
total_B_lbl.place(x=60, y=90)
balance_lbl = Label(text="Balance", font=("Ariel", 38, "bold"), fg="black", bg="white")
balance_lbl.place(x=60, y=110)

window.mainloop()