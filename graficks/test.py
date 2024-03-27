import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2, 2, 400)
m = 2

plt.figure()
y = (1 + x) ** m
plt.plot(x, y, label='$(1 + x)^m$, m={}'.format(m), color='b')

plt.title('График функции $(1 + x)^m$')
plt.xlabel('x')
plt.ylabel('$(1 + x)^m$')

plt.legend()
plt.show()
