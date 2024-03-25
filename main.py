import math

from functions.func import sin_maclaurin, cos_maclaurin
from graficks.grath import graphic_visualization


if "__main__" == __name__:
    x = 3
    print(f"sin({x}) : {sin_maclaurin(x)}")
    print(f"cos({x}) : {cos_maclaurin(x)}")
    # graphic_visualization('sin(x)')
    # graphic_visualization('cos(x)')
    # graphic_visualization('tg(x)')
    # graphic_visualization('arctg(x)')
    graphic_visualization('e^(x)')