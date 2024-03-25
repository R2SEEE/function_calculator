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

    if name_func == 'tg(x)':
        x_ticks = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
        x_labels = [r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$']

    if name_func == 'arctg(x)' or name_func == 'e^(x)':
        x_ticks = [-5 * np.pi, -3 * np.pi, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi, 5 * np.pi]
        x_labels = [r'$-5\pi$', r'$-3\pi$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$',
                    r'$3\pi$', r'$5\pi$']

    if MEASUREMENT_AXIS_X == 'pi':
        return plt.xticks(x_ticks, x_labels)


def set_sin():
    """
    Создает график функции синуса sin(x)
    :return: matplotlib.lines.Line2D: Объект линии графика.
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # от -2π до 2π
    y_values = np.sin(x_values)
    return plt.plot(x_values, y_values, color=COLOR_FUNC, label='sin(x)')


def set_cos():
    """
    Создает график функции синуса cos(x)
    :return: matplotlib.lines.Line2D: Объект линии графика.
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y_values = np.cos(x_values)
    return plt.plot(x_values, y_values, color=COLOR_FUNC, label='cos(x)')


def set_tg():
    """
    Создает график функции синуса tg(x)
    :return: matplotlib.lines.Line2D: Объект линии графика.
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-1.5 * np.pi, 1.5 * np.pi, 500)  # от -1.5π до 1.5π
    x_values = x_values[np.abs(np.cos(x_values)) > 1e-3]
    y_values = np.tan(x_values)
    return plt.plot(x_values, y_values, color=COLOR_FUNC, label='tg(x)')


def set_arctg():
    """
    Создает график функции синуса arctg(x)

    :return: matplotlib.lines.Line2D: Объект линии графика.
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
    y_values = np.arctan(x_values)
    return plt.plot(x_values, y_values, label='arctan(x)', color=COLOR_FUNC)


def set_e_x():
    """
    Создает график функции синуса e^(x)

    :return: matplotlib.lines.Line2D: Объект линии графика.
    """
    plt.figure(facecolor='lightgray')
    x_values = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
    y_values = np.exp(x_values)
    return plt.plot(x_values, y_values, label='$e^x$', color=COLOR_FUNC)


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
        plt.ylim(-10, 10)

    plt.axhline(0, color=COLOR_X_Y, linewidth=THICKNESS_X_Y)  # горизонтальная ось
    plt.axvline(0, color=COLOR_X_Y, linewidth=THICKNESS_X_Y)  # вертикальная ось
    plt.grid(CELLS_GRAPHICS, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()


def graphic_visualization(fun) -> None:
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


if __name__ == '__main__':
    graphic_visualization('e^(x)')
