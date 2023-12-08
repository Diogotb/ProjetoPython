import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# from fracdiff import fd

# Função para as EDOs do modelo de Lotka-Volterra
def model(y, t, alpha, beta, gamma, delta):
    R, F = y
    dRdt = alpha * R - beta * R * F
    dFdt = -gamma * F + delta * R * F
    return [dRdt, dFdt]

# Parâmetros
alpha_val = 0.1
beta_val = 0.02
gamma_val = 0.1
delta_val = 0.01

# Condições iniciais
initial_conditions = [40, 9]

# Tempo
time_points = np.linspace(0, 200, 1000)

# Resolver numericamente usando odeint
numerical_solution = odeint(model, initial_conditions, time_points, args=(alpha_val, beta_val, gamma_val, delta_val))

# Plotar resultados
plt.figure(figsize=(10, 6))
plt.plot(time_points, numerical_solution[:, 0], label='Coelhos (presas)')
plt.plot(time_points, numerical_solution[:, 1], label='Raposas (predadores)')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Modelo de Lotka-Volterra com Cálculos Fracionários')
plt.legend()
plt.show()
