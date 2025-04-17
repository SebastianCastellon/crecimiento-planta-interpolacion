from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

# Datos
days = np.array([7, 21, 35, 49, 63, 77, 91])
height = np.array([8.5, 21, 50, 77, 89, 98, 99])

# Spline cúbico
cs = CubicSpline(days, height)

# Estimación en día 40
day_40 = 40
height_40 = cs(day_40)

# Gráfica
plt.scatter(days, height, label='Datos')
t_values = np.linspace(7, 91, 200)
plt.plot(t_values, cs(t_values), 'm', label='Spline Cúbico')
plt.xlabel('Días')
plt.ylabel('Altura (pulgadas)')
plt.legend()
plt.savefig('cubic_spline.png')
plt.show()

print(f"Altura en día 40 (Spline): {height_40:.1f} pulgadas")
