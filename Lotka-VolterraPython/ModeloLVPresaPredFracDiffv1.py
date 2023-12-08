import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Sistema de equações Lotka-Volterra
def lotka_volterra(t, z, alpha, beta, gamma, delta):
    x, y = z
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Parâmetros do modelo Lotka-Volterra
alpha = 0.1   # Taxa de crescimento dos coelhos na ausência de predadores
beta = 0.02   # Taxa de predação dos coelhos pelas raposas
gamma = 0.1   # Taxa de morte das raposas na ausência de presas
delta = 0.01  # Taxa de crescimento das raposas devido à predação dos coelhos

# Condições iniciais
initial_conditions = [40, 9]  # População inicial de coelhos e raposas

# Configuração do tempo
T = 200
dt = 0.1
time_span = (0, T)

# Integração numérica usando solve_ivp
solution = solve_ivp(
    fun=lambda t, z: lotka_volterra(t, z, alpha, beta, gamma, delta),
    t_span=time_span,
    y0=initial_conditions,
    method='RK45',
    t_eval=np.arange(0, T, dt)
)

# Plotagem do gráfico
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label='Coelhos')
plt.plot(solution.t, solution.y[1], label='Raposas')
plt.title('Modelo Lotka-Volterra com Integração Numérica')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()
plt.grid(True)
plt.show()
