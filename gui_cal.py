from tkinter import *
import pygame

root = Tk()
root.title('Calculator')
root.geometry('600x700')

# Initializing mixer
pygame.mixer.init()


def set_text(text):
    entrybox.delete(0, END)
    entrybox.insert(0, text)
    return


master_frame = Frame(root)
master_frame.pack(pady=20)
q = 'sadfasdf'
entrybox = Entry(master=master_frame, width=17, font=('Arial', 33))
entrybox.pack()

# Creating button's images
xm_btn_img = PhotoImage(file='imgs_for_gui/1xm.png')
x11_btn_img = PhotoImage(file='imgs_for_gui/11x.png')
acos_btn_img = PhotoImage(file='imgs_for_gui/acos.png')
arctg_btn_img = PhotoImage(file='imgs_for_gui/arctg.png')
asin_btn_img = PhotoImage(file='imgs_for_gui/asin.png')
cos_btn_img = PhotoImage(file='imgs_for_gui/cos.png')
ex_btn_img = PhotoImage(file='imgs_for_gui/ex.png')
ln1x_btn_img = PhotoImage(file='imgs_for_gui/ln1x.png')
sin_btn_img = PhotoImage(file='imgs_for_gui/sin.png')
tgx_btn_img = PhotoImage(file='imgs_for_gui/tg.png')

# Creating frame for buttons
control_btns_frame = Frame(root)
control_btns_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Creating buttons
xm_btn = Button(control_btns_frame, image=xm_btn_img, borderwidth=0, command=lambda: set_text("(1+x)^m"))
x11_btn = Button(control_btns_frame, image=x11_btn_img, borderwidth=0, command=lambda: set_text("1/(1+x)"))
acos_btn = Button(control_btns_frame, image=acos_btn_img, borderwidth=0, command=lambda: set_text("acos(x)"))
arctg_btn = Button(control_btns_frame, image=arctg_btn_img, borderwidth=0, command=lambda: set_text("arctg(x)"))
asin_btn = Button(control_btns_frame, image=asin_btn_img, borderwidth=0, command=lambda: set_text("asin(x)"))
cos_btn = Button(control_btns_frame, image=cos_btn_img, borderwidth=0, command=lambda: set_text("cos(x)"))
ex_btn = Button(control_btns_frame, image=ex_btn_img, borderwidth=0, command=lambda: set_text("e^(x)"))
ln1x_btn = Button(control_btns_frame, image=ln1x_btn_img, borderwidth=0, command=lambda: set_text("ln(1+x)"))
sin_btn = Button(control_btns_frame, image=sin_btn_img, borderwidth=0, command=lambda: set_text("sin(x)"))
tg_btn = Button(control_btns_frame, image=tgx_btn_img, borderwidth=0, command=lambda: set_text("tg(x)"))

xm_btn.grid(row=0, column=0, padx=22, pady=12)
x11_btn.grid(row=0, column=1, padx=22, pady=12)
acos_btn.grid(row=1, column=0, padx=22, pady=12)
arctg_btn.grid(row=1, column=1, padx=22, pady=12)
asin_btn.grid(row=2, column=0, padx=22, pady=12)
cos_btn.grid(row=2, column=1, padx=22, pady=12)
ex_btn.grid(row=3, column=0, padx=22, pady=12)
ln1x_btn.grid(row=3, column=1, padx=22, pady=12)
sin_btn.grid(row=4, column=0, padx=22, pady=12)
tg_btn.grid(row=4, column=1, padx=22, pady=12)

root.mainloop()
