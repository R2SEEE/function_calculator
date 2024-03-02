import math


def sin_maclaurin(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return result


if __name__ == "__main__":
    pass
