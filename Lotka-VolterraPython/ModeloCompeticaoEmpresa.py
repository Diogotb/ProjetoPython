import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do modelo Lotka-Volterra
r1 = 0.1  # Taxa intrínseca de crescimento de empresas A
r2 = 0.1  # Taxa intrínseca de crescimento de empresas B
a12 = 0.01  # Taxa de competição de empresas B em relação a empresas A
a21 = 0.01  # Taxa de competição de empresas A em relação a empresas B

# Condições iniciais
E1_0 = 100  # População inicial de empresas A
E2_0 = 100  # População inicial de empresas B

# Tempo
t = np.linspace(0, 100, 1000)

# Listas para armazenar a evolução das populações
E1 = []
E2 = []

# Simulação Lotka-Volterra
for time in t:
    dE1dt = r1 * E1_0 - a12 * E1_0 * E2_0
    dE2dt = r2 * E2_0 - a21 * E2_0 * E1_0
    E1_0 += dE1dt
    E2_0 += dE2dt
    E1.append(E1_0)
    E2.append(E2_0)

# Plotagem do gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, E1, label='Empresas A', color='blue')
plt.plot(t, E2, label='Empresas B', color='red')
plt.xlabel('Tempo')
plt.ylabel('População de Empresas')
plt.legend()
plt.title('Modelo Lotka-Volterra na Competição entre Empresas')
plt.grid()
plt.show()
