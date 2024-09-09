import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Datos proporcionados
x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 33, 244])

# Trazador cúbico
spline = CubicSpline(x, y)

# Estimar valor de y para x = 2.7
y_spline_est = spline(2.7)

# Mostrar el resultado
print(f"El valor estimado de y para x = 2.7 usando trazador cúbico es: {y_spline_est}")

# Graficar el trazador cúbico
x_vals = np.linspace(0, 3, 100)
y_vals = spline(x_vals)

plt.plot(x_vals, y_vals, label="Trazador cúbico", color='purple')
plt.scatter(x, y, color='blue', zorder=5, label="Datos originales")
plt.scatter(2.7, y_spline_est, color='green', zorder=5, label=f"Estimación x=2.7")
plt.legend()
plt.grid(True)
plt.title("Trazador Cúbico")
plt.xlabel("x")
plt.ylabel("y")
plt.show()