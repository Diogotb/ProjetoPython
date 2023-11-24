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

# Configuração do plano (x, y) para os campos vetoriais
x_range = np.linspace(min(x_values), max(x_values), 20)
y_range = np.linspace(min(y_values), max(y_values), 20)
x_derivatives, y_derivatives = np.meshgrid(x_range, y_range)
dxdt = dt * (alpha * x_derivatives - beta * x_derivatives * y_derivatives)
dydt = dt * (delta * x_derivatives * y_derivatives - gamma * y_derivatives)

# Normaliza os vetores para melhor visualização
magnitude = np.sqrt(dxdt**2 + dydt**2)
dxdt /= magnitude
dydt /= magnitude

# Plotagem dos campos vetoriais
plt.figure(figsize=(12, 8))
plt.plot(x_values, y_values, label='Dinâmica Populacional')
plt.quiver(x_derivatives, y_derivatives, dxdt, dydt, scale=35, color='red', label='Campos Vetoriais')
plt.title('Modelo Lotka-Volterra: Campos Vetoriais')
plt.xlabel('População de Coelhos')
plt.ylabel('População de Raposas')
plt.legend()
plt.grid(True)
plt.show()
