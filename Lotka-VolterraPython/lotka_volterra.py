import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parâmetros do modelo
alpha = 1.0
beta = 0.5
gamma = 0.5
sigma = 2.0

# Função que retorna as derivadas
def f(u, t):
    x, y = u
    return np.array([x * (alpha - beta * y), -y * (gamma - sigma * x)])

# Condições iniciais
u0 = [2, 1]

# Intervalo de tempo
t = np.linspace(0, 10, 1000)

# Resolvendo a equação diferencial
u = odeint(f, u0, t)

# Plotando o resultado
plt.plot(t, u[:, 0], label='Presa')
plt.plot(t, u[:, 1], label='Predador')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Modelo Presa-Predador de Lotka-Volterra')
plt.legend()
plt.show()