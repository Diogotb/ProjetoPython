import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo Lotka-Volterra
alpha = 0.1   # Taxa de crescimento dos coelhos na ausência de predadores
beta = 0.02   # Taxa de predação dos coelhos pelas raposas
gamma = 0.1   # Taxa de morte das raposas na ausência de presas
delta = 0.01  # Taxa de crescimento das raposas devido à predação dos coelhos

# Condições iniciais
x0 = 40  # População inicial de coelhos
y0 = 9   # População inicial de raposas

# Configuração do tempo
T = 200
dt = 0.1
num_steps = int(T / dt)

# Arrays para armazenar resultados
x_values = np.zeros(num_steps)
y_values = np.zeros(num_steps)
time_values = np.zeros(num_steps)

# Inicialização das populações iniciais
x = x0
y = y0

# Simulação do modelo Lotka-Volterra usando o método de Euler
for i in range(num_steps):
    x_values[i] = x
    y_values[i] = y
    time_values[i] = i * dt
    
    # Equações de Lotka-Volterra usando o método de Euler
    dx = dt * (alpha * x - beta * x * y)
    dy = dt * (delta * x * y - gamma * y)
    
    # Atualização das populações
    x += dx
    y += dy

# Plotagem do gráfico bidimensional
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Dinâmica Populacional')
plt.title('Modelo Lotka-Volterra: Sistema Dinâmico Bidimensional')
plt.xlabel('População de Coelhos')
plt.ylabel('População de Raposas')
plt.legend()
plt.grid(True)
plt.show()