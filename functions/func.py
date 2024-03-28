import math


def evaluate_error(step, x):
    return x ** step / math.factorial(step)


def evaluate_error_exp(step, x):
    return abs((x ** step) / math.factorial(step))


def exp_maclaurin(x):
    n = 1
    result = 1
    while True:
        if evaluate_error_exp(step=n, x=x) > pow(10, -9):
            result += x ** n / math.factorial(n)
            n += 1
            continue
        break
    return round(result, 9)


def evaluate_error_binomial(step, x, m):
    error = (x ** step) / math.factorial(step)
    error *= ((1 + x) ** (m - step))
    for i in range(m, m - step, -1):
        error *= i
    return error


def binomial_maclaurin(x, m):
    if 1 > x > -1:
        n = 1
        result = 1
        while True:
            if evaluate_error_binomial(step=n, x=x, m=m) > pow(10, -9):
                member = (x ** n) / math.factorial(n)
                for i in range(m, m - n, -1):
                    member *= i
                result += member
                n += 1
                continue
            break
        return round(result, 9)
    else:
        raise ValueError("-1 < x < 1")


def evaluate_error_ln(step, x):
    return abs(x ** step / step)


def ln_maclaurin(x):
    if -1 < x <= 1:
        result = 0
        n = 0
        while True:
            n += 1
            if evaluate_error_ln(step=n, x=x) > pow(10, -10):
                result += ((-1) ** (n + 1)) * (x ** n) / n
                continue
            break
        return round(result, 9)
    else:
        raise ValueError("-1 < x <= 1")


def evaluate_error_hyperbole(step, x):
    return abs(x ** step)


def hyperbole_maclaurin(x):
    result = 1
    n = 1
    while True:
        if evaluate_error_hyperbole(step=n, x=x) > pow(10, -10):
            result += ((-1) ** n) * x ** n
            n += 1
            continue
        break
    return round(result, 9)


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
