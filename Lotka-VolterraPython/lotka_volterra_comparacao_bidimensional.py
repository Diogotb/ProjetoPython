import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parâmetros do modelo
alpha = 1.0
beta = 0.5
gamma = 0.5
sigma = 2.0

# Função que retorna as derivadas para o modelo de Lotka-Volterra
def f(u, t):
    x, y = u
    return np.array([x * (alpha - beta * y), -y * (gamma - sigma * x)])

# Função que retorna as derivadas para o modelo de Lotka-Volterra Fracdiff
def f_fracdiff(u, t):
    x, y = u
    return np.array([x ** 0.5 * (alpha - beta * y ** 0.5), -y ** 0.5 * (gamma - sigma * x ** 0.5)])

# Condições iniciais
u0 = [40, 9]

# Intervalo de tempo
t = np.linspace(0, 200, 1000)

# Resolvendo a equação diferencial para o modelo de Lotka-Volterra
u = odeint(f, u0, t)

# Resolvendo a equação diferencial para o modelo de Lotka-Volterra Fracdiff
u_fracdiff = np.zeros((len(t), 2))
u_fracdiff[0] = u0
for i in range(len(t) - 1):
    dt = t[i + 1] - t[i]
    u_fracdiff[i + 1] = u_fracdiff[i] + dt ** 0.5 * f_fracdiff(u_fracdiff[i], t[i])

# Plotando o resultado
plt.plot(u[:, 0], u[:, 1], label='Lotka-Volterra')
plt.plot(u_fracdiff[:, 0], u_fracdiff[:, 1], label='Lotka-Volterra Fracdiff')
plt.xlabel('População de Presas')
plt.ylabel('População de Predadores')
plt.title('Evolução das Populações de Presas e Predadores')
plt.legend()
plt.show()
