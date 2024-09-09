import numpy as np
import matplotlib.pyplot as plt

# Definimos los puntos dados
x = [3.0, 4.5, 7.0, 9.0]
y = [2.5, 1.0, 2.5, 0.5]

# Inicializamos la gráfica
plt.figure()

# Calculamos las pendientes y graficamos cada segmento de línea
for i in range(len(x) - 1):
    # Calcular la pendiente (m) y el intercepto (b) de la recta entre dos puntos
    m = (y[i+1] - y[i]) / (x[i+1] - x[i])
    b = y[i] - m * x[i]
    
    # Generamos puntos para la línea
    x_line = np.linspace(x[i], x[i+1], 100)
    y_line = m * x_line + b
    
    # Graficamos el segmento de línea
    plt.plot(x_line, y_line, label=f'Segmento {i+1}')
    
# Graficamos los puntos originales
plt.scatter(x, y, color='red', zorder=5)

# Etiquetas de los ejes
plt.xlabel('x')
plt.ylabel('y')

# Título y leyenda
plt.title('Trazador Lineal')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()