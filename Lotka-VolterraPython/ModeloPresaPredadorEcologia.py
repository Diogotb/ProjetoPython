import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Função que define as EDOs do modelo Lotka-Volterra
def lotka_volterra(t, y):
    P, Pr = y
    dPdt = rp * P - a * P * Pr
    dPrdt = b * P * Pr - d * Pr
    return [dPdt, dPrdt]

# Parâmetros do modelo fictícios
rp = 0.1
a = 0.02
b = 0.3
d = 0.1

# Condições iniciais
P0 = 40
Pr0 = 9
y0 = [P0, Pr0]

# Tempo
t_span = (0, 200)
t_eval = np.linspace(*t_span, 1000)

# Solução numérica das EDOs
solution = solve_ivp(lotka_volterra, t_span, y0, t_eval=t_eval)

# Gráfico das populações de presas e predadores ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label='Presas', color='blue')
plt.plot(solution.t, solution.y[1], label='Predadores', color='red')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()
plt.title('Modelo Lotka-Volterra (Presa-Predador) - Simulação')
plt.grid()
plt.show()
