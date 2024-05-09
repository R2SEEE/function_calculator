import math
from math import pi
from decimal import Decimal


def evaluate_error(num, den):
    res = num / den
    return res


def evaluate_error_exp(num, dev):
    return abs(num / dev)


def exp_maclaurin(x):
    x = Decimal(f"{x}")
    n = 1
    result = Decimal("1")
    dev = Decimal("1")
    num = Decimal(f"{x}")
    while True:
        dev *= n
        if evaluate_error_exp(num=num, dev=dev) > pow(10, -15):
            result += num / dev  # x ** n / factorial(n)
            num *= x
            n += 1
            continue
        break
    if result > pow(10, 12):
        return result
    return round(result, 9)


def evaluate_error_binomial(step, x, m, num, den):
    error = num / den
    error *= Decimal(f"{((1 + x) ** (m - step))}")
    for i in range(m, m - step, -1):
        error *= Decimal(f"{i}")
    return error


def binomial_maclaurin(x, m):
    if 1 > x > -1:
        n = 1
        x = Decimal(f"{x}")
        result = Decimal("1")
        num = Decimal(f"{x}")
        den = Decimal("1")
        while True:
            if abs(evaluate_error_binomial(step=n, x=x, m=m, num=num, den=den)) > pow(10, -15):
                member = num / den
                for i in range(m, m - n, -1):
                    member *= i
                result += member
                num *= x
                n += 1
                den *= n
                continue
            break
        return round(result, 9)
    else:
        raise ValueError("-1 < x < 1")


def evaluate_error_ln(step, num):
    return abs(Decimal(f"{num / step}"))


def ln_maclaurin(x):
    if -1 < x <= 1:
        result = Decimal("0")
        pow_x = Decimal(f"{x}")
        num = Decimal(f"{x}")
        n = 0
        while True:
            n += 1
            if evaluate_error_ln(step=n, num=num) > pow(10, -15):
                result += num / n
                num *= -pow_x
                continue
            break
        return round(result, 9)
    else:
        raise ValueError("-1 < x <= 1")


def hyperbole_maclaurin(x):
    result = Decimal("1")
    n = 1
    pow_x = Decimal(f"{x}")
    member = Decimal(f"{-pow_x}")
    while True:
        if abs(member) > pow(10, -15):
            result += member
            member *= -pow_x
            n += 1
            continue
        break
    return round(result, 9)


def arcsin_maclaurin(x):
    if -1 <= x <= 1:
        x_dec = Decimal(f"{x}")
        result = x_dec
        n = 1
        denominator = Decimal("1")
        den_count = Decimal("2")
        numerator = Decimal("1")
        num_count = Decimal("1")
        while True:
            x_dec *= Decimal(f"{x}") ** 2
            denominator *= den_count
            numerator *= num_count
            num = numerator * x_dec
            den = ((2 * n + 1) * denominator)
            member = num / den
            if abs(member) > pow(10, -15):
                result += member
                n += 1
                den_count += 2
                num_count += 2
                continue
            break
        return round(result, 9)
    else:
        raise ValueError("-1 <= x <= 1")


def arccos_maclaurin(x):
    return round(Decimal(f"{pi / 2}") - arcsin_maclaurin(x), 9)


def arctan_maclaurin(x):
    if -1 <= x <= 1:
        result = Decimal("0")
        x_dec = Decimal(f"{x}")
        n = 0
        while True:
            num = x_dec
            den = Decimal(f"{(2 * n + 1)}")
            member = num / den
            if abs(member) > pow(10, -15):
                result += member
                x_dec *= -Decimal(f"{x}") ** 2
                n += 1
                continue
            break
        return round(result, 9)


def tan_maclaurin(x):

    if x != pi / 2 and x != -pi / 2:
        bernully_nums = [1, -1/2, 1/6]
        result = Decimal("0")
        k = 2
        n = 1
        den = Decimal("2")
        x_num = Decimal(f"{x}")

        while True:

            bernully_member = Decimal(f"{abs(bernully_nums[2 * n])}")
            pow_two_member = Decimal(f"{2 ** (2 * n) * (2 ** (2 * n) - 1)}")

            num = bernully_member * pow_two_member * x_num
            member = num / den

            if abs(member) > pow(10, -15):
                result += member
                for i in range(2 * n + 1, 2 * (n + 1) + 1):
                    den *= i
                x_num *= Decimal(f"{x}") ** 2
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

    if abs(x) > 44:
        div = math.trunc(x / math.pi)
        if abs(div) % 2 == 0:
            x = x - div * math.pi
        else:
            if x > 0:
                x = x - ((div - 1) * math.pi)
            else:
                x = x - ((div + 1) * math.pi)
    n = 1
    result = Decimal("0")
    den = Decimal("1")
    num = Decimal(f"{x}")
    while True:
        if abs(evaluate_error(num=num, den=den)) > pow(10, -15):
            result += num / den
            n += 1
            num *= -Decimal(f"{x}") ** 2
            den *= (2 * n - 1) * (2 * n - 2)
            continue
        else:
            break
    return round(result, 9)


def cos_maclaurin(x):
    """
    Функция косинуса без автоматической
    подборки точности
    """

    if abs(x) > 44:
        div = math.trunc(x / math.pi)
        if abs(div) % 2 == 0:
            x = x - div * math.pi
        else:
            if x > 0:
                x = x - ((div - 1) * math.pi)
            else:
                x = x - ((div + 1) * math.pi)
    n = 2
    result = Decimal("1")
    den = Decimal("2")
    num = -Decimal(f"{x}") ** 2
    while True:
        if abs(evaluate_error(num=num, den=den)) > pow(10, -15):
            result += num / den
            n += 1
            num *= -Decimal(f"{x}") ** 2
            den *= (2 * n - 2) * (2 * n - 3)
            continue
        else:
            break
    return round(result, 9)


if __name__ == "__main__":
    pass
