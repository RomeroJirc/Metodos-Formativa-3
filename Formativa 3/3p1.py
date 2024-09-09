import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Datos proporcionados
x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 33, 244])

# Polinomio de Lagrange
polinomio = lagrange(x, y)

# Estimar valor de y para x = 2.7
x_val = 2.7
y_est = polinomio(x_val)

# Mostrar el polinomio
print("Polinomio de Lagrange:", polinomio)
print(f"El valor estimado de y para x = {x_val} es: {y_est}")

# Graficar el polinomio de Lagrange
x_vals = np.linspace(0, 3, 100)
y_vals = polinomio(x_vals)

plt.plot(x_vals, y_vals, label="Polinomio de Lagrange", color='red')
plt.scatter(x, y, color='blue', zorder=5, label="Datos originales")
plt.scatter(x_val, y_est, color='green', zorder=5, label=f"Estimación x={x_val}")
plt.legend()
plt.grid(True)
plt.title("Interpolación de Lagrange")
plt.xlabel("x")
plt.ylabel("y")
plt.show()