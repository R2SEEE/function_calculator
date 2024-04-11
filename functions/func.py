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
        if evaluate_error_hyperbole(step=n, x=x) > pow(10, -11):
            result += ((-1) ** n) * x ** n
            n += 1
            continue
        break
    return round(result, 9)


def arcsin_maclaurin(x):
    if -1 <= x <= 1:
        result = x
        n = 1
        while True:
            denominator = 1.0
            numerator = 1.0
            for i in range(1, 2 * n + 1):
                if i % 2 == 0:
                    denominator *= i
                else:
                    numerator *= i
            member = numerator * x ** (2 * n + 1) / ((2 * n + 1) * denominator)
            if member > pow(10, -11):
                result += member
                n += 1
                continue
            break
        return round(result, 9)
    else:
        raise ValueError("-1 <= x <= 1")


def arccos_maclaurin(x):
    return round(math.pi / 2 - arcsin_maclaurin(x), 9)


def arctan_maclaurin(x):
    if -1 <= x <= 1:
        result = 0
        n = 0
        while True:
            member = (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
            if abs(member) > pow(10, -11):
                result += member
                n += 1
                continue
            break
        return round(result, 9)


def tan_maclaurin(x):
    if x != math.pi / 2 and x != -math.pi / 2:
        bernully_nums = [1, -1/2, 1/6]
        result = 0
        k = 2
        n = 1
        while True:
            member = abs(bernully_nums[2 * n]) * 2 ** (2 * n) * (2 ** (2 * n) - 1) * x ** (2 * n - 1) / \
                math.factorial(2 * n)
            if member > pow(10, -10):
                result += member
                n += 1
                k += 1
                bernully_num(k, bernully_nums)
                k += 1
                bernully_num(k, bernully_nums)
                continue
            break
        return round(result, 9)
    else:
        raise ValueError("x != pi/2 + 2 * pi * k, k = Z")


def bernully_num(n, bernully_before_n):
    summary = 0
    for i in range(0, n):
        summary += math.factorial(n + 1) / (math.factorial(n + 1 - i) * math.factorial(i)) * \
            bernully_before_n[i]
    res = -summary / (n + 1)
    bernully_before_n.append(res)
    return None


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
