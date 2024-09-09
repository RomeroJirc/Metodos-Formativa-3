
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator

# Definir la función f(x)
def f(x):
    return np.sin(2 * np.pi * x)

# Nodos
x = np.linspace(0, 1, 4)
y = f(x)

# Interpolación usando un trazador cuadrático (PchipInterpolator)
pchip = PchipInterpolator(x, y)

# Crear un conjunto de puntos para graficar la aproximación
x_vals = np.linspace(0, 1, 100)
y_vals = f(x_vals)
y_approx = pchip(x_vals)

# Graficar la función original y la aproximación
plt.plot(x_vals, y_vals, label="f(x) = sin(2πx)", color='blue')
plt.plot(x_vals, y_approx, label="Aproximación cuadrática", color='red', linestyle='--')
plt.scatter(x, y, color='black', zorder=5, label="Nodos")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Aproximación con trazador cuadrático")
plt.grid(True)
plt.show()