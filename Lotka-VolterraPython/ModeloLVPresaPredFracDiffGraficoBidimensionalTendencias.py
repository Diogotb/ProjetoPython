import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parâmetros do modelo
alpha = 1.0
beta = 0.5
gamma = 0.5
sigma = 2.0

# Função que retorna as derivadas fracionárias
def f(u, t):
    x, y = u
    dxdt = x * (alpha - beta * y)
    dydt = -y * (gamma - sigma * x)
    return [dxdt, dydt]

# Condições iniciais
u0 = [40, 9]

# Intervalo de tempo
T = 200
t = np.linspace(0, T, 1000)

# Resolvendo a equação diferencial ordinária
u = odeint(f, u0, t)

# Plotando o resultado em formato bidimensional
plt.figure(figsize=(10, 6))
plt.plot(t, u[:, 0], label='População de Coelhos')
plt.plot(t, u[:, 1], label='População de Raposas')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Modelo Presa-Predador de Lotka-Volterra (Bidimensional)')
plt.legend()
plt.grid(True)
plt.show()