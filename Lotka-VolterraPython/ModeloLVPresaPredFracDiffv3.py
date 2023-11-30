import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
alpha = 0.1
beta = 0.02
gamma = 0.1
delta = 0.01
q = 0.5  # Ordem fracionária

# Condições iniciais
R0 = 40
F0 = 9

# Tempo
t_max = 200
dt = 0.1
time_points = np.arange(0, t_max, dt)

# Inicialização das populações
R = np.zeros(len(time_points))
F = np.zeros(len(time_points))
R[0] = R0
F[0] = F0

# Método de diferenças finitas para EDFs
for i in range(1, len(time_points)):
    R[i] = R[i-1] + dt * (alpha * R[i-1] - beta * R[i-1] * F[i-1])
    F[i] = F[i-1] + dt * (-gamma * F[i-1] + delta * R[i-1] * F[i-1])

# Plotar resultados
plt.figure(figsize=(10, 6))
plt.plot(time_points, R, label='Coelhos (presas)')
plt.plot(time_points, F, label='Raposas (predadores)')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Modelo de Lotka-Volterra com Cálculos Fracionários (Diferenças Finitas)')
plt.legend()
plt.show()
