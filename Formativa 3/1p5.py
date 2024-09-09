import numpy as np
import matplotlib.pyplot as plt

# Definimos los puntos dados
x = [3.0, 4.5, 7.0, 9.0]
y = [2.5, 1.0, 2.5, 0.5]

# Inicializamos la gráfica
plt.figure()

# Estimar el valor para x = 5
x_target = 5

# Ajuste cúbico
coef_cubico = np.polyfit(x, y, 3)  # Polinomio de grado 3
p_cubico = np.poly1d(coef_cubico)

# Estimar el valor para x = 5 usando el trazador cúbico
y_target_cubico = p_cubico(x_target)
print(f"Estimación cúbica: y({x_target}) = {y_target_cubico}")

# Graficar el polinomio cúbico
x_line = np.linspace(min(x), max(x), 100)
y_line_cubico = p_cubico(x_line)

plt.plot(x_line, y_line_cubico, label='Trazador Cúbico')

# Graficar el punto estimado para x = 5
plt.scatter(x_target, y_target_cubico, color='blue', zorder=5, label=f'Estimación cúbica x={x_target}')

# Graficar los puntos originales
plt.scatter(x, y, color='red', zorder=5)

# Etiquetas de los ejes
plt.xlabel('x')
plt.ylabel('y')

# Título y leyenda
plt.title('Trazador Cúbico con Estimación')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()