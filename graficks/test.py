import numpy as np
import matplotlib.pyplot as plt

# Генерируем значения для оси x от -2 до 2
x_values = np.linspace(-2, 2, 400)

# Ограничиваем диапазон значений x, чтобы 1 + x было положительным
valid_indices = np.where(1 + x_values > 0)
x_valid = x_values[valid_indices]

# Вычисляем значения функции ln(1 + x) для каждого значения x
y_values = np.log(1 + x_valid)

# Создаем новое графическое окно
plt.figure()

# Строим график функции ln(1 + x)
plt.plot(x_valid, y_values, label='ln(1 + x)', color='b')

# Устанавливаем метки на оси x в виде символов π
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])

# Добавляем заголовок и метки осей
plt.title('График функции ln(1 + x)')
plt.xlabel('x')
plt.ylabel('ln(1 + x)')

# Добавляем легенду
plt.legend()

# Показываем график
plt.show()
