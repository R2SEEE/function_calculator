import math


def evaluate_error(step, x):
    return x ** step / math.factorial(step)


def sin_maclaurin(x):
    """
    Функция синуса без автоматической
    подборки точности
    """

    n = 0
    result = 0
    while True:
        n += 1
        if n <= 5:
            result += ((-1) ** (n - 1)) * (x ** (2 * n - 1)) / math.factorial(2 * n - 1)
            continue
        elif evaluate_error(step=n, x=x) > pow(10, -9):
            result += ((-1) ** (n - 1)) * (x ** (2 * n - 1)) / math.factorial(2 * n - 1)
            continue
        else:
            break
    return round(result, 9)


def cos_maclaurin(x):
    """
    Функция косинуса без автоматической
    подборки точности
    """

    result = 1
    n = 1
    while True:
        n += 1
        if n <= 5:
            result += ((-1) ** (n - 1)) * (x ** (2 * n - 2)) / math.factorial(2 * n - 2)
        elif evaluate_error(step=n, x=x) > pow(10, -9):
            result += ((-1) ** (n - 1)) * (x ** (2 * n - 2)) / math.factorial(2 * n - 2)
            continue
        else:
            break
    return round(result, 9)


if __name__ == "__main__":
    pass
