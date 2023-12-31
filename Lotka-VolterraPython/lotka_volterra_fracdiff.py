import numpy as np
import matplotlib.pyplot as plt
from fracdiff import fdiff
from scipy.integrate import solve_ivp

# Função para calcular a derivada fracionária
def frac_diff(x, alpha):
    fd = Fracdiff(alpha)
    return fd(x)

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

# Resolução numérica do modelo usando solve_ivp
solution = solve_ivp(
    fun=lambda t, z: lotka_volterra(t, z, alpha, beta, gamma, delta),
    t_span=time_span,
    y0=initial_conditions,
    method='RK45',
    t_eval=np.arange(0, T, dt)
)

# Calcula derivadas fracionárias
x_frac_diff = frac_diff(solution.y[0], 0.5)  # Exemplo: derivada fracionária de ordem 0.5
y_frac_diff = frac_diff(solution.y[1], 0.5)

# Plotagem do gráfico
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(solution.t, solution.y[0], label='Coelhos')
plt.title('População de Coelhos')

plt.subplot(3, 1, 2)
plt.plot(solution.t, solution.y[1], label='Raposas')
plt.title('População de Raposas')

plt.subplot(3, 1, 3)
plt.plot(solution.t, x_frac_diff, label='Derivada Fracionária de Coelhos')
plt.plot(solution.t, y_frac_diff, label='Derivada Fracionária de Raposas')
plt.title('Derivadas Fracionárias')

plt.xlabel('Tempo')
plt.legend()
plt.tight_layout()
plt.show()
