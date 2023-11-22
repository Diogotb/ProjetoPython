import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parâmetros do modelo
alpha = 0.1
beta = 0.02
delta = 0.01
gamma = 0.1

# Condições iniciais
initial_conditions = [40, 9]

# Intervalo de tempo
t = np.linspace(0, 200, 1000)

# Resolução tradicional com EDOs
solution_odeint = odeint(lotka_volterra, initial_conditions, t, args=(alpha, beta, delta, gamma))

# Resolução com cálculo fracionário
solution_fracdiff = lotka_volterra_fracdiff(initial_conditions, t, alpha, beta, delta, gamma)

# Plotagem dos resultados
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, solution_odeint[:, 0], label='Presas (EDO)', color='blue')
plt.plot(t, solution_odeint[:, 1], label='Predadores (EDO)', color='red')
plt.title('Resolução com EDOs')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, solution_fracdiff[:, 0], label='Presas (Fracionário)', linestyle='--', color='blue')
plt.plot(t, solution_fracdiff[:, 1], label='Predadores (Fracionário)', linestyle='--', color='red')
plt.title('Resolução com Cálculo Fracionário')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()

plt.tight_layout()
plt.show()

