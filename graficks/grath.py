import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, CheckButtons


def plot_graph(name_function=None):
    """
    Построение графика выбранной функции.

    Параметры:
    - name_function (str): Название выбранной функции. Возможные значения:
        'sin(x)', 'cos(x)', 'tg(x)', 'arctg(x)', 'e^(x)', 'ln(1 + x)', '(1 + x)^m',
        '1/(1+x)', 'arcsin(x)', 'arccos(x)'.

    Возвращает: None
    """

    def change_axis_x(name_func):
        """
        Изменяет единицу измерения оси x на PI.

        Возвращает: None
        """
        x_ticks = None
        x_labels = None

        if name_func == 'sin(x)' or name_func == 'cos(x)':
            x_ticks = [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]
            x_labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$',
                        r'$\pi$',
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

        graph_axes.set_xticks(x_ticks)
        graph_axes.set_xticklabels(x_labels)

    def updateGraph():
        """
        Обновляет график при изменении параметров.
        """
        nonlocal name_function

        x = 1
        y = 4

        if name_function == 'sin(x)':
            x = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # от -2π до 2π
            y = np.sin(x)

        if name_function == 'cos(x)':
            x = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # от -2π до 2π
            y = np.cos(x)

        if name_function == 'tg(x)':
            x = np.linspace(-1.5 * np.pi, 1.5 * np.pi, 1000)
            y = np.tan(x)

        if name_function == 'arctg(x)':
            x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
            y = np.arctan(x)

        if name_function == 'e^(x)':
            x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
            y = np.exp(x)

        if name_function == 'ln(1 + x)':
            x_values = np.linspace(-np.pi, np.pi, 400)
            valid_indices = np.where(1 + x_values > 0)
            x = x_values[valid_indices]
            y = np.log(1 + x)

        if name_function == '(1 + x)^m':
            m = 2
            x = np.linspace(-np.pi, np.pi, 400)
            y = (1 + x) ** m

        if name_function == '1/(1+x)':
            x = np.linspace(-10, -1.01, 400)
            y = 1 / (1 + x)

        if name_function == 'arcsin(x)':
            x = np.linspace(-1, 1, 400)
            y = np.arcsin(x)

        if name_function == 'arccos(x)':
            x = np.linspace(-1, 1, 400)
            y = np.arccos(x)

        colors = {"Красный": "r", "Синий": "b", "Зеленый": "g"}

        style = colors[radiobuttons_color.value_selected]

        size = slider_size_func.val

        graph_axes.clear()
        graph_axes.axhline(0, linewidth=1.3, color='black')
        graph_axes.axvline(0, linewidth=1.3, color='black')

        grid_visible = checkbuttons_grid.get_status()[0]
        graph_axes.grid(grid_visible)

        if checkbuttons_pi.get_status()[0]:
            change_axis_x(name_function)

        graph_axes.set_title(f'График: {name_function}')

        if name_function == 'tg(x)':
            graph_axes.set_xlim(-1.5 * np.pi, 1.5 * np.pi)
            graph_axes.set_ylim(-12, 12)

        if name_function == '1/(1+x)':
            graph_axes.set_xlim(-10, 10)
            graph_axes.set_ylim(-1, 1)
            x2 = np.linspace(-0.99, 10, 400)
            y2 = 1 / (1 + x2)
            graph_axes.plot(x2, y2, color=style, linewidth=size)

        graph_axes.plot(x, y, color=style, linewidth=size)

        plt.draw()

    def onChangeValue(value: np.float64):
        '''!!! Обработчик события изменения значений слайдеров'''
        updateGraph()

    def onRadioButtonsClicked(value: str):
        """!!! Обработчик события при клике по RadioButtons"""
        updateGraph()

    def onCheckClicked(value: str):
        """!!! Обработчик события при нажатии на флажок"""
        updateGraph()

    fig, graph_axes = plt.subplots()  # окно с графиком
    fig.patch.set_facecolor('lightblue')
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    axes_slider_size_func = plt.axes([0.35, 0.17, 0.5, 0.04])
    slider_size_func = Slider(axes_slider_size_func,
                              label='size_fun',
                              valmin=0.05,
                              valmax=5.0,
                              valinit=0.95,
                              valfmt='%1.2f')

    axes_radiobuttons = plt.axes([0.05, 0.09, 0.17, 0.2])
    radiobuttons_color = RadioButtons(
        axes_radiobuttons, ["Красный", "Синий", "Зеленый"]
    )

    axes_checkbuttons = plt.axes([0.05, 0.01, 0.17, 0.07])
    checkbuttons_grid = CheckButtons(axes_checkbuttons, ["Сетка"], [True])

    axes_checkbuttons_pi = plt.axes([0.23, 0.01, 0.09, 0.07])
    checkbuttons_pi = CheckButtons(axes_checkbuttons_pi, ["PI"], [False])

    radiobuttons_color.on_clicked(onRadioButtonsClicked)
    slider_size_func.on_changed(onChangeValue)
    checkbuttons_grid.on_clicked(onCheckClicked)
    checkbuttons_pi.on_clicked(onCheckClicked)

    name_function = name_function
    updateGraph()
    plt.show()


def show_list_function():
    ls_fun = ['sin(x)',
              'cos(x)',
              'tg(x)',
              'e^(x)',
              'ln(1 + x)',
              '(1 + x)^m',
              '1/(1+x)',
              'arcsin(x)',
              'arctg(x)',
              'arccos(x)']

    for i in range(1, len(ls_fun) + 1):
        print(f'{i}. {ls_fun[i - 1]}')


if __name__ == '__main__':
    show_list_function()