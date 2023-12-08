import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def fractional_derivative_laplace(y, alpha, dt):
    """
    Calcula a derivada fracionária usando a transformada de Laplace fracionária.

    Parâmetros:
    - y: Lista ou array contendo os valores da série temporal.
    - alpha: Ordem fracionária para a derivada.
    - dt: Incremento de tempo.

    Retorna:
    - Valor fracionário calculado.
    """
    y = np.asarray(y)  # Garante que y seja um array numpy
    N = len(y)  # Comprimento de y
    result = np.zeros_like(y)

    for i in range(1, N):
        result[i] = alpha / dt * (y[i] - y[i-1]) + result[i-1]

    return result

# Parâmetros do modelo Lotka-Volterra
alpha = 0.1   # Taxa de crescimento das presas na ausência de predadores
beta = 0.02   # Taxa de predação (interação entre presas e predadores)
gamma = 0.1   # Taxa de diminuição dos predadores na ausência de presas
delta = 0.01  # Taxa de crescimento dos predadores em função das presas
q = 0.5       # Ordem fracionária para a derivada (pode ser ajustada conforme necessário)

# Condições iniciais
R0 = 40  # População inicial de coelhos (presas)
F0 = 9   # População inicial de raposas (predadores)

# Configuração do tempo
t_max = 200  # Tempo máximo de simulação
dt = 0.1     # Incremento de tempo (passo)
time_points = np.arange(0, t_max, dt)  # Lista de pontos temporais

# Inicialização das populações
R = np.zeros(len(time_points))  # Lista para armazenar a população de coelhos
F = np.zeros(len(time_points))  # Lista para armazenar a população de raposas
R[0] = R0  # População inicial de coelhos
F[0] = F0  # População inicial de raposas


# Método de transformada de Laplace fracionária para resolver EDFs
for i in range(1, len(time_points)):
    # Equações Lotka-Volterra com derivadas fracionárias
    dRdt = alpha * R[i-1] - beta * R[i-1] * F[i-1] + delta * fractional_derivative_laplace(R[i-1], q, dt)
    dFdt = -gamma * F[i-1] + delta * R[i-1] * F[i-1] + delta * fractional_derivative_laplace(F[i-1], q, dt)

    # Atualização das populações usando o método de diferenças finitas fracionárias
    R[i] = R[i-1] + dt * dRdt
    F[i] = F[i-1] + dt * dFdt

# Plotagem dos resultados
plt.figure(figsize=(10, 6))
plt.plot(time_points, R, label='Coelhos (presas)')
plt.plot(time_points, F, label='Raposas (predadores)')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Modelo de Lotka-Volterra com Transformada de Laplace Fracionária')
plt.legend()
plt.show()
