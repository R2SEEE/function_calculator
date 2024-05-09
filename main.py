import math
import numpy


from graficks.grath import plot_graph
from functions.func import sin_maclaurin, cos_maclaurin, exp_maclaurin, binomial_maclaurin, ln_maclaurin, \
    hyperbole_maclaurin, arcsin_maclaurin, arccos_maclaurin, tan_maclaurin


if "__main__" == __name__:
    x = 1.5
    m = 10
    # print(f"sin({x}) : {sin_maclaurin(x)}")
    # print(f"cos({x}) : {cos_maclaurin(x)}")
    # print(f"exp({x}) : {exp_maclaurin(x)}")
    # print(f"(1 + {x}) ** {m} : {binomial_maclaurin(x, m)}")
    # print(f"ln(1 + {x}) : {ln_maclaurin(x)}")
    # print(f"1 / (1 + {x}) : {hyperbole_maclaurin(x)}")
    # print(f"arccos({x}) : {arccos_maclaurin(x)}")
    # print(f"arcsin({x}) : {arcsin_maclaurin(x)}")
    print(tan_maclaurin(1.5))

