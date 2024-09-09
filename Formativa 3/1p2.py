import numpy as np
import matplotlib.pyplot as plt

# Definimos los puntos dados
x = [3.0, 4.5, 7.0, 9.0]
y = [2.5, 1.0, 2.5, 0.5]

# Inicializamos la gráfica
plt.figure()

# Estimar el valor para x = 5
x_target = 5

# Calcular la pendiente y la recta correspondiente al intervalo que contiene x = 5
for i in range(len(x) - 1):
    # Calcular la pendiente (m) y el intercepto (b) de la recta entre dos puntos
    m = (y[i+1] - y[i]) / (x[i+1] - x[i])
    b = y[i] - m * x[i]
    
    # Si x_target está en el intervalo actual, estimamos el valor de y
    if x[i] <= x_target <= x[i+1]:
        y_target = m * x_target + b
        print(f"Estimación: y({x_target}) = {y_target}")
        
        # Graficar el punto estimado
        plt.scatter(x_target, y_target, color='green', zorder=5, label=f'Estimación x={x_target}')

    # Generar los puntos para la línea entre cada par de puntos
    x_line = np.linspace(x[i], x[i+1], 100)
    y_line = m * x_line + b
    
    # Graficar el segmento de línea
    plt.plot(x_line, y_line, label=f'Segmento {i+1}')
    
# Graficar los puntos originales
plt.scatter(x, y, color='red', zorder=5)

# Etiquetas de los ejes
plt.xlabel('x')
plt.ylabel('y')

# Título y leyenda
plt.title('Trazador Lineal con Estimación')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()