import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
alpha = 0.1
beta = 0.02
gamma = 0.1
delta = 0.01

# Condições iniciais
x0 = 40  # população inicial de coelhos
y0 = 9   # população inicial de raposas

# Tempo
T = 200
dt = 0.1
num_steps = int(T / dt)

# Arrays para armazenar resultados
x_values = np.zeros(num_steps)
y_values = np.zeros(num_steps)
time_values = np.zeros(num_steps)

# Inicialização
x = x0
y = y0

# Simulação
for i in range(num_steps):
    x_values[i] = x
    y_values[i] = y
    time_values[i] = i * dt
    
    # Equações de Lotka-Volterra usando o método de Euler
    dx = dt * (alpha * x - beta * x * y)
    dy = dt * (delta * x * y - gamma * y)
    
    x += dx
    y += dy

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(time_values, x_values, label='Coelhos')
plt.plot(time_values, y_values, label='Raposas')
plt.title('Dinâmica Populacional: Modelo Lotka-Volterra')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()
plt.grid(True)
plt.show()
