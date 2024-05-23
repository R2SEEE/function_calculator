from tkinter import *
from graficks.grath import plot_graph
from functions.func import (
    exp_maclaurin,
    binomial_maclaurin,
    ln_maclaurin,
    hyperbole_maclaurin,
    arccos_maclaurin,
    arctan_maclaurin,
    arcsin_maclaurin,
    tan_maclaurin,
    sin_maclaurin,
    cos_maclaurin,
)
import matplotlib.pyplot as plt
from math import pi
import pygame

root = Tk()
root.title("Calculator")
root.geometry("600x700")

pygame.mixer.init()
pygame.mixer.music.load("sounds/popsound.mp3")


def popsound():
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)


def set_text(text):
    entrybox.delete(0, END)
    entrybox.insert(0, text)
    global funcFlag
    funcFlag = entrybox.get()
    popsound()


# Интерфейс команды
class Command:
    def execute(self):
        pass


# Конкретные команды для каждой функции
class CosCommand(Command):
    def execute(self, x):
        return cos_maclaurin(x)


class LnCommand(Command):
    def execute(self, x):
        if -1 < x <= 1:
            return ln_maclaurin(x)
        else:
            errorPopup("Enter -1 < x <= 1")


class ExpCommand(Command):
    def execute(self, x):
        return exp_maclaurin(x)


class ArcsinCommand(Command):
    def execute(self, x):
        if -1 <= x <= 1:
            return arcsin_maclaurin(x)
        else:
            errorPopup("Enter -1 <= x <= 1")


class SinCommand(Command):
    def execute(self, x):
        return sin_maclaurin(x)


class TanCommand(Command):
    def execute(self, x):
        if x % (pi / 2) != 0:
            return tan_maclaurin(x)
        else:
            errorPopup("Enter x not equal pi/2 + pi*k")


class ArccosCommand(Command):
    def execute(self, x):
        if -1 <= x <= 1:
            return arccos_maclaurin(x)
        else:
            errorPopup("Enter -1 <= x <= 1")


class BinomialCommand(Command):
    def execute(self, x, m):
        if (
            (m >= 0 and -1 <= x <= 1)
            or (-1 < m < 0 and -1 < x <= 1)
            or (m <= -1 and -1 < x < 1)
        ):
            return binomial_maclaurin(x, m)
        else:
            errorPopup(
                "Enter x and m:\nm>=0, x[-1, 1]\n -1<m<0, x(-1, 1]\nm<=-1, x(-1, 1)"
            )


class ArctanCommand(Command):
    def execute(self, x):
        if -1 <= x <= 1:
            return arctan_maclaurin(x)
        else:
            errorPopup("Enter -1 <= x <= 1")


class HyperboleCommand(Command):
    def execute(self, x):
        if -1 < x < 1:
            return hyperbole_maclaurin(x)
        else:
            errorPopup("Enter -1 < x < 1")


def solveButton():
    plt.close("all")
    answerbox.delete(0, END)
    result = getAnswer()
    answerbox.insert(0, result)
    if result != "":
        plot_graph(funcFlag)
    popsound()


def errorPopup(error_text):
    popsound()
    global pop
    pop = Toplevel(root)
    pop.title("Error")
    pop.geometry("250x150")
    popLabel = Label(pop, text=error_text, font=("Arial", 13), pady=45)
    popLabel.pack()
    OKbtn = Button(pop, text="OK", font=("Arial", "20"), command=pop.destroy)
    OKbtn.pack()
    answerbox.delete(0, END)
    answerbox.insert(0, "Your answer")


def getXM():
    expressionStr = entrybox.get()
    expressionStr = expressionStr.replace(",", ".")
    expressionStr = expressionStr.replace(" ", "")
    argumentX = expressionStr[expressionStr.index("(") + 1 : expressionStr.index(")")]
    if "pi" in expressionStr:
        if "/" in argumentX:
            return pi / float(argumentX[argumentX.index("/") + 1 :])
        elif "*" in argumentX:
            return pi * float(argumentX[argumentX.index("*") + 1 :])
        else:
            return pi
    else:
        if '+' in argumentX and (')^' not in expressionStr):
            argumentX = argumentX[argumentX.index('+')+1:]
            try:
                return float(argumentX)
            except:
                errorPopup('You entered wrong data type!')
        elif ')^' in expressionStr:
            argumentM = expressionStr[expressionStr.index('^')+1:]
            argumentX = argumentX[argumentX.index('+')+1:]
            try:
                return float(argumentX), float(argumentM)
            except:
                errorPopup('You entered wrong data type!')
        else:
            try:
                return float(argumentX)
            except:
                errorPopup('You entered wrong data type!')

def getAnswer():
    x = getXM()
    if x is None:
        return ""

    commands = {
        "cos(x)": CosCommand(),
        "ln(1 + x)": LnCommand(),
        "e^(x)": ExpCommand(),
        "arcsin(x)": ArcsinCommand(),
        "sin(x)": SinCommand(),
        "tg(x)": TanCommand(),
        "arccos(x)": ArccosCommand(),
        "(1 + x)^m": BinomialCommand(),
        "arctg(x)": ArctanCommand(),
        "1/(1+x)": HyperboleCommand(),
    }

    command = commands.get(funcFlag)
    if command:
        if funcFlag == "(1 + x)^m":
            # Дополнительный аргумент для биномиальной команды
            x = getXM()[0]
            m = int(getXM()[1])
            return command.execute(x, m)
        else:
            return command.execute(x)
    else:
        return ""


# Создание интерфейса
master_frame = Frame(root)
master_frame.pack(pady=20)

entrybox = Entry(master=master_frame, width=17, font=("Arial", 33))
entrybox.grid(row=1, column=1)

solve_btn = Button(
    master_frame,
    background="#62AAFF",
    text="Solve",
    font=("Arial, 20"),
    command=solveButton,
)
solve_btn.grid(row=1, column=2)

answerbox = Entry(
    master=master_frame, width=17, background="#62AAFF", font=("Arial", 30)
)
answerbox.grid(row=2, column=1, sticky=W)
answerbox.insert(0, "Your answer")

# Создание кнопок для каждой функции
buttons = [
    ("(1 + x)^m", "imgs_for_gui/1xm.png"),
    ("1/(1+x)", "imgs_for_gui/11x.png"),
    ("arccos(x)", "imgs_for_gui/acos.png"),
    ("arctg(x)", "imgs_for_gui/arctg.png"),
    ("arcsin(x)", "imgs_for_gui/asin.png"),
    ("cos(x)", "imgs_for_gui/cos.png"),
    ("e^(x)", "imgs_for_gui/ex.png"),
    ("ln(1 + x)", "imgs_for_gui/ln1x.png"),
    ("sin(x)", "imgs_for_gui/sin.png"),
    ("tg(x)", "imgs_for_gui/tg.png"),
]

control_btns_frame = Frame(root)
control_btns_frame.pack(fill="both", expand=True, padx=20, pady=20)

for i, (text, img) in enumerate(buttons):
    img_obj = PhotoImage(file=img)
    btn = Button(
        control_btns_frame,
        image=img_obj,
        borderwidth=0,
        command=lambda t=text: set_text(t),
    )
    btn.image = img_obj  # сохранить ссылку на изображение
    btn.grid(row=i // 2, column=i % 2, padx=22, pady=12)
root.mainloop()
