import math

from functions.func import sin_maclaurin, cos_maclaurin


if "__main__" == __name__:
    x = 3
    print(f"sin({x}) : {sin_maclaurin(x)}")
    print(f"cos({x}) : {cos_maclaurin(x)}")

