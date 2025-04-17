import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Datos
days = np.array([7, 21, 35, 49, 63, 77, 91])
height = np.array([8.5, 21, 50, 77, 89, 98, 99])
H = 102

# Modelo logístico linealizado
z = np.log(height / (H - height))
A = np.vstack([np.ones_like(days), days]).T
a, b = np.linalg.lstsq(A, z, rcond=None)[0]

# Función logística
def logistic(t, a, b):
    return H / (1 + np.exp(-(a + b * t)))

# Estimación en día 40
day_40 = 40
height_40 = logistic(day_40, a, b)

# Gráfica
plt.scatter(days, height, label='Datos')
t_values = np.linspace(0, 100, 200)
plt.plot(t_values, logistic(t_values, a, b), 'r', label='Modelo Logístico')
plt.xlabel('Días')
plt.ylabel('Altura (pulgadas)')
plt.legend()
plt.savefig('logistic_regression.png')
plt.show()

print(f"a ≈ {a:.4f}, b ≈ {b:.4f}")
print(f"Altura en día 40: {height_40:.1f} pulgadas")
