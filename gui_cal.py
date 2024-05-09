from tkinter import *
from graficks.grath import plot_graph
from functions.func import exp_maclaurin, binomial_maclaurin, ln_maclaurin, hyperbole_maclaurin, arccos_maclaurin, \
    arctan_maclaurin, arcsin_maclaurin, tan_maclaurin, sin_maclaurin, cos_maclaurin
import matplotlib.pyplot as plt

root = Tk()
root.title('Calculator')
root.geometry('600x700')


def set_text(text):
    entrybox.delete(0, END)
    entrybox.insert(0, text)
    global funcFlag
    funcFlag = entrybox.get()


master_frame = Frame(root)
master_frame.pack(pady=20)

entrybox = Entry(master=master_frame, width=17, font=('Arial', 33))
entrybox.grid(row=1, column=1)
# entrybox.pack(side='left', padx=25)
solve_btn = Button(master_frame, background='#62AAFF', text='Solve', font=('Arial, 20'), command=lambda: solveButton())
solve_btn.grid(row=1, column=2)
# solve_btn.pack()
answerbox = Entry(master=master_frame, width=17, background='#62AAFF', font=('Arial', 30))
answerbox.grid(row=2, column=1, sticky=W)
answerbox.insert(0, 'Your answer')


# answerbox.pack()


def solveButton():
    plt.close('all')
    answerbox.delete(0, END)
    answerbox.insert(0, getAnswer())
    plot_graph(funcFlag)


def errorPopup():
    global pop
    pop = Toplevel(root)
    pop.title('Error')
    pop.geometry('250x150')
    pop.config()
    popLabel = Label(pop, text='You entered wrong data type!', font=('Arial', 13), pady=45)
    popLabel.pack()
    OKbtn = Button(pop, text='OK', font=('Arial', 20), command=pop.destroy)
    OKbtn.pack()
    answerbox.delete(0, END)
    answerbox.insert(0, 'Your answer')


def getXM():
    expressionStr = entrybox.get()  # sin(x)
    expressionStr = expressionStr.replace(',', '.')
    argumentX = expressionStr[expressionStr.index('(') + 1:expressionStr.index(')')]
    # if argumentX.isdigit()==0:
    #     print('You entered wrong data type!')
    #     errorPopup()
    argumentX = str(argumentX)
    if '+' in argumentX:
        argumentX = eval(argumentX + '-1')
        try:
            argumentX = float(argumentX)
        except ValueError:
            errorPopup()
            return None

    if ')^' in expressionStr:
        argumentM = expressionStr[expressionStr.index('^') + 1:]

        try:
            return float(argumentX), int(argumentM)
        except ValueError:
            errorPopup()
            return None

    return float(argumentX)


def getAnswer():
    if funcFlag == 'cos(x)' and getXM() is not None:
        return cos_maclaurin(getXM())
    elif funcFlag == 'ln(1 + x)' and getXM() is not None:
        return ln_maclaurin(getXM())
    elif funcFlag == 'e^(x)' and getXM() is not None:
        return exp_maclaurin(getXM())
    elif funcFlag == 'arcsin(x)' and getXM() is not None:
        return arcsin_maclaurin(getXM())
    elif funcFlag == 'sin(x)' and getXM() is not None:
        return sin_maclaurin(getXM())
    elif funcFlag == 'tg(x)' and getXM() is not None:
        return tan_maclaurin(getXM())
    elif funcFlag == 'arccos(x)' and getXM() is not None:
        return arccos_maclaurin(getXM())
    elif funcFlag == '(1 + x)^m' and getXM() is not None:
        return binomial_maclaurin(*getXM())
    elif funcFlag == 'arctg(x)' and getXM() is not None:
        return arctan_maclaurin(getXM())
    elif funcFlag == '1/(1+x)' and getXM() is not None:
        return hyperbole_maclaurin(getXM())
    else:
        return ''


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
xm_btn = Button(control_btns_frame, image=xm_btn_img, borderwidth=0, command=lambda: set_text("(1 + x)^m"))
x11_btn = Button(control_btns_frame, image=x11_btn_img, borderwidth=0, command=lambda: set_text("1/(1+x)"))
acos_btn = Button(control_btns_frame, image=acos_btn_img, borderwidth=0, command=lambda: set_text("arccos(x)"))
arctg_btn = Button(control_btns_frame, image=arctg_btn_img, borderwidth=0, command=lambda: set_text("arctg(x)"))
asin_btn = Button(control_btns_frame, image=asin_btn_img, borderwidth=0, command=lambda: set_text("arcsin(x)"))
cos_btn = Button(control_btns_frame, image=cos_btn_img, borderwidth=0, command=lambda: set_text("cos(x)"))
ex_btn = Button(control_btns_frame, image=ex_btn_img, borderwidth=0, command=lambda: set_text("e^(x)"))
ln1x_btn = Button(control_btns_frame, image=ln1x_btn_img, borderwidth=0, command=lambda: set_text("ln(1 + x)"))
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
