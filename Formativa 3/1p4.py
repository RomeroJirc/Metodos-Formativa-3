import numpy as np
import matplotlib.pyplot as plt

# Definimos los puntos dados
x = [3.0, 4.5, 7.0, 9.0]
y = [2.5, 1.0, 2.5, 0.5]

# Inicializamos la gráfica
plt.figure()

# Estimar el valor para x = 5
x_target = 5

# Función para calcular el polinomio cuadrático entre dos puntos con continuidad
def cuadratico_suave(xi, yi, xi_next, yi_next, x_next_next, y_next_next):
    # Resolvemos el sistema de ecuaciones para garantizar continuidad en la pendiente
    # y suavidad en la curva
    # Se resuelve imponiendo que la derivada de los segmentos coincida en los puntos intermedios
    
    A = np.array([
        [(xi - xi)**2, (xi - xi), 1],         # f(xi) = yi
        [(xi_next - xi)**2, (xi_next - xi), 1],  # f(xi_next) = yi_next
        [2*(xi_next - xi), 1, 0]                # f'(xi_next) debe ser suave
    ])
    
    B = np.array([yi, yi_next, (y_next_next - yi_next) / (x_next_next - xi_next)])
    
    # Resolver para los coeficientes a, b, c
    coef = np.linalg.solve(A, B)
    
    return coef

# Graficar los segmentos de trazadores cuadráticos
for i in range(len(x) - 2):
    # Calcular los coeficientes del polinomio cuadrático
    a, b, c = cuadratico_suave(x[i], y[i], x[i+1], y[i+1], x[i+2], y[i+2])
    
    # Generar los puntos para la gráfica entre x[i] y x[i+1]
    x_line = np.linspace(x[i], x[i+1], 100)
    y_line = a * (x_line - x[i])**2 + b * (x_line - x[i]) + c
    
    # Graficar el segmento
    plt.plot(x_line, y_line, label=f'Segmento {i+1}')
    
    # Si el punto objetivo x = 5 está en este intervalo, calcular el valor de y
    if x[i] <= x_target <= x[i+1]:
        y_target = a * (x_target - x[i])**2 + b * (x_target - x[i]) + c
        print(f"Estimación cuadrática por partes: y({x_target}) = {y_target}")
        plt.scatter(x_target, y_target, color='green', zorder=5, label=f'Estimación cuadrática x={x_target}')

# Graficar los puntos originales
plt.scatter(x, y, color='red', zorder=5)

# Etiquetas de los ejes
plt.xlabel('x')
plt.ylabel('y')

# Título y leyenda
plt.title('Trazador Cuadrático por Partes (Suavizado)')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()