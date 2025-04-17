from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

# Datos
days = np.array([7, 21, 35, 49, 63, 77, 91])
height = np.array([8.5, 21, 50, 77, 89, 98, 99])

# Polinomio de Lagrange
poly = lagrange(days, height)

# Estimación en día 40
day_40 = 40
height_40 = poly(day_40)

# Gráfica
plt.scatter(days, height, label='Datos')
t_values = np.linspace(7, 91, 200)
plt.plot(t_values, poly(t_values), 'g', label='Polinomio de Lagrange')
plt.xlabel('Días')
plt.ylabel('Altura (pulgadas)')
plt.legend()
plt.savefig('lagrange_interpolation.png')
plt.show()

print(f"Altura en día 40 (Lagrange): {height_40:.1f} pulgadas")
