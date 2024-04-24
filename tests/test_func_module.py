import pytest
import math
from functions import func


@pytest.mark.parametrize("x, expected_result", [(0, round(math.sin(0), 9)),
                                                (1, round(math.sin(1), 9)),
                                                (9, round(math.sin(9), 9)),
                                                (0.12, round(math.sin(0.12), 9)),
                                                (4, round(math.sin(4), 9)),
                                                (0.647, round(math.sin(0.647), 9)),
                                                (-0.12, round(math.sin(-0.12), 9)),
                                                (15, round(math.sin(15), 9)),
                                                (-15, round(math.sin(-15), 9))
                                                ])
def test_sin(x, expected_result):
    assert func.sin_maclaurin(x) == expected_result


@pytest.mark.parametrize("x, expected_result", [(0, round(math.cos(0), 9)),
                                                (1, round(math.cos(1), 9)),
                                                (9, round(math.cos(9), 9)),
                                                (0.12, round(math.cos(0.12), 9)),
                                                (4, round(math.cos(4), 9)),
                                                (0.647, round(math.cos(0.647), 9)),
                                                (-0.12, round(math.cos(-0.12), 9)),
                                                (15, round(math.cos(15), 9)),
                                                (-15, round(math.cos(-15), 9))
                                                ])
def test_cos(x, expected_result):
    assert func.cos_maclaurin(x) == expected_result


@pytest.mark.parametrize('x, expected_result', [(0, 1),
                                                (2, 7.389056099),
                                                (-3, 0.049787068),
                                                (1, 2.718281828),
                                                (10, 22026.465794807),
                                                (-10, 0.0000454),
                                                (153, 2.7993405242674957e+66),
                                                (2.23, 9.299866079),
                                                (4.124, 61.805972365),
                                                (0.531, 1.700632091)])
def test_exp(x, expected_result):
    assert func.exp_maclaurin(x) == expected_result


@pytest.mark.parametrize('x, m, expected_result', [(0.78, 4, 10.03875856),
                                                   (0.78, 10, 319.300812083),
                                                   (0.34, 5, 4.320400342),
                                                   (0.001, 10, 1.010045120),
                                                   (0.12464, 20, 10.477810014),
                                                   (-0.12464, 20, 0.069780479),
                                                   (-0.156, 50, 0.00020755),
                                                   (-0.25, 60, 3.2e-08)])
def test_binomial(x, m, expected_result):
    assert func.binomial_maclaurin(x, m) == expected_result


@pytest.mark.parametrize('x, expected_result', [(0.144, round(math.asin(0.144), 9)),
                                                (0.2564, round(math.asin(0.2564), 9)),
                                                (0.54262, round(math.asin(0.54262), 9)),
                                                (0.9, round(math.asin(0.9), 9)),
                                                (0.72352, round(math.asin(0.72352), 9)),
                                                (-0.72352, round(math.asin(-0.72352), 9)),
                                                (-0.9, round(math.asin(-0.9), 9)),
                                                (-0.54262, round(math.asin(-0.54262), 9)),
                                                (-0.144, round(math.asin(-0.144), 9))])
def test_arcsin(x, expected_result):
    assert func.arcsin_maclaurin(x) == expected_result


@pytest.mark.parametrize('x, expected_result', [(0.144, round(math.acos(0.144), 9)),
                                                (0.2564, round(math.acos(0.2564), 9)),
                                                (0.54262, round(math.acos(0.54262), 9)),
                                                (0.9, round(math.acos(0.9), 9)),
                                                (0.72352, round(math.acos(0.72352), 9)),
                                                (-0.7235, round(math.acos(-0.7235), 9)),
                                                (-0.9, round(math.acos(-0.9), 9)),
                                                (-0.542, round(math.acos(-0.542), 9)),
                                                (-0.144, round(math.acos(-0.144), 9))])
def test_arccos(x, expected_result):
    assert func.arccos_maclaurin(x) == expected_result


@pytest.mark.parametrize('x, expected_result', [(0.144, round(math.atan(0.144), 9)),
                                                (0.2564, round(math.atan(0.2564), 9)),
                                                (0.54262, round(math.atan(0.54262), 9)),
                                                (0.9, round(math.atan(0.9), 9)),
                                                (0.72352, round(math.atan(0.72352), 9)),
                                                (-0.7235, round(math.atan(-0.7235), 9)),
                                                (-0.9, round(math.atan(-0.9), 9)),
                                                (-0.542, round(math.atan(-0.542), 9)),
                                                (-0.144, round(math.atan(-0.144), 9))])
def test_arctan(x, expected_result):
    assert func.arctan_maclaurin(x) == expected_result


@pytest.mark.parametrize('x, expected_result', [(0.144, round(math.tan(0.144), 9)),
                                                (0.2564, round(math.tan(0.2564), 9)),
                                                (0.54262, round(math.tan(0.54262), 9)),
                                                (0.9, round(math.tan(0.9), 9)),
                                                (0.72352, round(math.tan(0.72352), 9)),
                                                (-0.7235, round(math.tan(-0.7235), 9)),
                                                (-0.9, round(math.tan(-0.9), 9)),
                                                (-0.542, round(math.tan(-0.542), 9)),
                                                (-0.144, round(math.tan(-0.144), 9))])
def test_tan(x, expected_result):
    assert func.tan_maclaurin(x) == expected_result


@pytest.mark.parametrize('x, expected_result', [(0.144, round(math.log(1 + 0.144), 9)),
                                                (0.2564, round(math.log(1 + 0.2564), 9)),
                                                (0.54262, round(math.log(1 + 0.54262), 9)),
                                                (0.9, round(math.log(1 + 0.9), 9)),
                                                (0.72352, round(math.log(1 + 0.72352), 9)),
                                                (-0.7235, round(math.log(1 + -0.7235), 9)),
                                                (-0.9, round(math.log(1 + -0.9), 9)),
                                                (-0.542, round(math.log(1 + -0.542), 9)),
                                                (-0.144, round(math.log(1 + -0.144), 9))])
def test_ln(x, expected_result):
    assert func.ln_maclaurin(x) == expected_result


@pytest.mark.parametrize('x, expected_result', [(0.144, round(1 / (1 + 0.144), 9)),
                                                (0.2564, round(1 / (1 + 0.2564), 9)),
                                                (0.54262, round(1 / (1 + 0.54262), 9)),
                                                (0.9, round(1 / (1 + 0.9), 9)),
                                                (0.72352, round(1 / (1 + 0.72352), 9)),
                                                (-0.7235, round(1 / (1 + -0.7235), 9)),
                                                (-0.9, round(1 / (1 + -0.9), 9)),
                                                (-0.542, round(1 / (1 + -0.542), 9)),
                                                (-0.144, round(1 / (1 + -0.144), 9))])
def test_hiperbole(x, expected_result):
    assert func.hyperbole_maclaurin(x) == expected_result