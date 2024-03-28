import numpy as np
import matplotlib.pyplot as plt
from graficks.setting import CELLS_GRAPHICS, THICKNESS_X_Y, COLOR_X_Y, MEASUREMENT_AXIS_X, \
    COLOR_FUNC


def change_axis_x(name_func):
    """
    Изменяет единицу измерения
    оси x на PI
    :return: None | object
    """
    x_ticks = None
    x_labels = None

    if name_func == 'sin(x)' or name_func == 'cos(x)':
        x_ticks = [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]
        x_labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$',
                    r'$\frac{3\pi}{2}$', r'$2\pi$']

    if name_func == 'ln(1 + x)' or name_func == '(1 + x)^m' \
            or name_func == '1/(1+x)' or name_func == 'arcsin(x)' or name_func == 'arccos(x)':
        x_ticks = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
        x_labels = [r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$']

    if name_func == 'arctg(x)' or name_func == 'e^(x)' or name_func == '1/(1+x)':
        x_ticks = [-5 * np.pi, -3 * np.pi, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi, 5 * np.pi]
        x_labels = [r'$-5\pi$', r'$-3\pi$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$',
                    r'$3\pi$', r'$5\pi$']

    if name_func == 'tg(x)':
        x_ticks = np.arange(-3 / 2 * np.pi, 3 / 2 * np.pi + np.pi / 2, np.pi / 2)
        x_labels = [r"$-\frac{3\pi}{2}$", r"$-\pi$", r"$-\frac{\pi}{2}$", r"$0$",
                    r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$"]

    if MEASUREMENT_AXIS_X == 'pi':
        return plt.xticks(x_ticks, x_labels)


def set_sin() -> None:
    """
    Создает график функции sin(x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # от -2π до 2π
    y_values = np.sin(x_values)
    plt.plot(x_values, y_values, color=COLOR_FUNC, label='sin(x)')


def set_cos() -> None:
    """
    Создает график функции cos(x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y_values = np.cos(x_values)
    plt.plot(x_values, y_values, color=COLOR_FUNC, label='cos(x)')


def set_tg() -> None:
    """
    Создает график функции tg(x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """

    # генерируем значения для оси x от -1.5π до 1.5π
    x_values = np.linspace(-1.5 * np.pi, 1.5 * np.pi, 1000)

    # разбиваем значения x на интервалы между асимптотами
    asymptotes = np.arange(-np.pi / 2, np.pi / 2 + np.pi, np.pi)
    asymptote_indices = np.searchsorted(x_values, asymptotes)

    for i in range(len(asymptotes) - 1):
        x_section = x_values[asymptote_indices[i]:asymptote_indices[i + 1]]
        y_section = np.tan(x_section)
        plt.plot(x_section, y_section, color=COLOR_FUNC)


def set_arctg() -> None:
    """
    Создает график функции arctg(x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
    y_values = np.arctan(x_values)
    plt.plot(x_values, y_values, label='arctan(x)', color=COLOR_FUNC)


def set_e_x() -> None:
    """
    Создает график функции e^(x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
    y_values = np.exp(x_values)
    plt.plot(x_values, y_values, label='$e^x$', color=COLOR_FUNC)


def set_ln_x_1() -> None:
    """
    Создает график функции ln(1 + x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """
    plt.figure(facecolor='lightgray')

    x_values = np.linspace(-np.pi, np.pi, 400)
    valid_indices = np.where(1 + x_values > 0)
    x_valid = x_values[valid_indices]
    y_values = np.log(1 + x_valid)

    plt.plot(x_valid, y_values, label='ln(1 + x)', color=COLOR_FUNC)


def set_1_x_m() -> None:
    """
    Создает график функции (1 + x)^m

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """
    m = 2
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-np.pi, np.pi, 400)
    y_values = (1 + x_values) ** m
    plt.plot(x_values, y_values, label='$(1 + x)^m$, m={}'.format(m), color=COLOR_FUNC)


def set_1_1_x() -> None:
    """
    Создает график функции 1/(1+x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """
    x1 = np.linspace(-10, -1.01, 400)  # для x < -1
    x2 = np.linspace(-0.99, 10, 400)  # для x > -1

    y1 = 1 / (1 + x1)
    y2 = 1 / (1 + x2)

    plt.plot(x1, y1, label='$1 / (1 + x)$', color=COLOR_FUNC, linewidth=2)
    plt.plot(x2, y2, color=COLOR_FUNC, linewidth=2)


def initialization(name_func):
    """
    Инициализирует параметры графика перед построением.

    :param name_func: Название функции
    :return: None
    """
    plt.title(f'Графи: {name_func}')
    plt.xlabel('x')
    plt.ylabel('y')

    if name_func == 'tg(x)':
        plt.xlim(-1.5 * np.pi, 1.5 * np.pi)
        plt.ylim(-12, 12)

    if name_func == '1/(1+x)':
        plt.xlim(-10, 10)
        plt.ylim(-1, 1)

    plt.axhline(0, color=COLOR_X_Y, linewidth=THICKNESS_X_Y)  # горизонтальная ось
    plt.axvline(0, color=COLOR_X_Y, linewidth=THICKNESS_X_Y)  # вертикальная ось

    if CELLS_GRAPHICS:
        plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend()
    plt.show()


def set_arcsin() -> None:
    """
    Создает график функции arcsin(x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """
    x = np.linspace(-1, 1, 400)
    y = np.arcsin(x)

    plt.plot(x, y, label='$\\arcsin(x)$', color=COLOR_FUNC)


def set_arccos() -> None:
    """
    Создает график функции arccos(x)

    matplotlib.lines.Line2D: Объект линии графика.

    :return: None
    """

    x = np.linspace(-1, 1, 400)
    y = np.arccos(x)

    plt.plot(x, y, label='$\\arccos(x)$', color=COLOR_FUNC)


def graphic_visualization(fun) -> None:
    """
    Отображает график выбранной функции.

    Аргумент:
    fun (str): название выбранной функции из списка доступных.

    :return: None
    """

    dict_funcs = {
        'sin(x)': 'set_sin()',
        'cos(x)': 'set_cos()',
        'tg(x)': 'set_tg()',
        'arctg(x)': 'set_arctg()',
        'e^(x)': 'set_e_x()',
        'ln(1 + x)': 'set_ln_x_1()',
        '1/(1+x)': 'set_1_1_x()',
        'arcsin(x)': 'set_arcsin()',
        'arccos(x)': 'set_arccos()'

    }

    if fun == 'sin(x)':
        set_sin()
        change_axis_x(fun)
        initialization(fun)

    elif fun == 'cos(x)':
        set_cos()
        change_axis_x(fun)
        initialization(fun)

    elif fun == 'tg(x)':
        set_tg()
        change_axis_x(fun)
        initialization(fun)

    elif fun == 'arctg(x)':
        set_arctg()
        change_axis_x(fun)
        initialization(fun)

    elif fun == 'e^(x)':
        set_e_x()
        change_axis_x(fun)
        initialization(fun)

    elif fun == 'ln(1 + x)':
        set_ln_x_1()
        change_axis_x(fun)
        initialization(fun)

    elif fun == '(1 + x)^m':
        set_1_x_m()
        change_axis_x(fun)
        initialization(fun)

    elif fun == '1/(1+x)':
        set_1_1_x()
        change_axis_x(fun)
        initialization(fun)

    elif fun == 'arcsin(x)':
        set_arcsin()
        change_axis_x(fun)
        initialization(fun)


    elif fun == 'arccos(x)':
        set_arccos()
        change_axis_x(fun)
        initialization(fun)

    else:
        print("функция не найден или некорректно введена,\n Словарь доступных функций:\n")
        print("название | вызов_функции")
        n = 0
        for key, value in dict_funcs.items():
            n += 1
            print(f'{n}. {key} {value}')


if __name__ == '__main__':
    pass
