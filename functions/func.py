import math


def sin_maclaurin(x, n):
    """
    Функция синуса без автоматической
    подборки точности
    """
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return result


def cos_maclaurin(x, n):
    """
    Функция косинуса без автоматической
    подборки точности
    """
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return result


if __name__ == "__main__":
    pass
