import numpy as np
import matplotlib.pyplot as plt

def fractional_difference(y, alpha, dt):
    """
    Calcula a diferença fracionária usando o método de diferenças finitas fracionárias.

    Parâmetros:
    - y: Lista ou array contendo os valores da série temporal.
    - alpha: Ordem fracionária para a derivada.
    - dt: Incremento de tempo.

    Retorna:
    - Valor fracionário calculado.
    """
    if len(y) >= 2:
        # Se houver pelo menos dois elementos em y, calcula a diferença fracionária.
        return (1 - alpha) * y[-1] + alpha * y[-2]
    else:
        # Se houver menos de dois elementos, retorna o último elemento.
        return y[-1]

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

# Método de diferenças finitas fracionárias para resolver EDFs
for i in range(1, len(time_points)):
    # Equações Lotka-Volterra discretizadas com derivadas fracionárias
    dRdt = alpha * R[i-1] - beta * R[i-1] * F[i-1] + delta * fractional_difference(R[:i], q, dt)
    dFdt = -gamma * F[i-1] + delta * R[i-1] * F[i-1] + delta * fractional_difference(F[:i], q, dt)

    # Atualização das populações usando o método de diferenças finitas fracionárias
    R[i] = R[i-1] + dt * dRdt
    F[i] = F[i-1] + dt * dFdt

# Plotagem do gráfico bidimensional
plt.figure(figsize=(10, 6))
plt.plot(R, F, label='Dinâmica Populacional')
plt.title('Modelo Lotka-Volterra: Sistema Dinâmico Bidimensional')
plt.xlabel('População de Coelhos')
plt.ylabel('População de Raposas')
plt.legend()
plt.grid(True)
plt.show()