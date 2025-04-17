import numpy as np
import matplotlib.pyplot as plt

# Datos
days = np.array([7, 21, 35, 49, 63, 77, 91])
height = np.array([8.5, 21, 50, 77, 89, 98, 99])

# Ajuste cuadrático
A = np.vstack([days**2, days, np.ones_like(days)]).T
c, d, e = np.linalg.lstsq(A, height, rcond=None)[0]

# Estimación en día 40
day_40 = 40
height_40 = c * day_40**2 + d * day_40 + e

# Gráfica
plt.scatter(days, height, label='Datos')
t_values = np.linspace(7, 91, 200)
plt.plot(t_values, c*t_values**2 + d*t_values + e, 'orange', label='Regresión Cuadrática')
plt.xlabel('Días')
plt.ylabel('Altura (pulgadas)')
plt.legend()
plt.savefig('quadratic_regression.png')
plt.show()

print(f"Altura en día 40 (Reg. Cuadrática): {height_40:.1f} pulgadas")
