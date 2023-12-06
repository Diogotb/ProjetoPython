# Importação de bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parâmetros do modelo para dinâmica da diabetes
alpha = 0.009  # Taxa de produção de glicose
beta = 0.004  # Taxa de absorção de glicose pelos tecidos
gamma = 0.01  # Taxa de degradação da insulina
delta = 0.001  # Eficácia da insulina em reduzir a concentração de glicose

# Sistema de equações diferenciais
def model(state, t):
    # Variáveis de estado
    x, y = state
    
    # Equações diferenciais que modelam a dinâmica da diabetes
    dxdt = alpha * x - beta * x * y  # Taxa de variação da glicose
    dydt = delta * x * y - gamma * y  # Taxa de variação da insulina
    
    return [dxdt, dydt]

# Condições iniciais (alta glicose, baixa insulina)
initial_state = [10, 2]

# Tempo (gerando 1000 pontos entre 0 e 200 unidades de tempo)
t = np.linspace(800, 2400, 16*60)

# Resolvendo as equações diferenciais usando odeint
solution = odeint(model, initial_state, t)

# Extraímos as soluções para glicose (x) e insulina (y)
x, y = solution.T

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(t, x*10, label='Glicose (x)')  # Multiplicamos x por 10 para melhor visualização
plt.plot(t, y, label='Insulina (y)')
plt.title('Dinâmica da Diabetes - Modelo Lotka-Volterra')
plt.xlabel('Tempo')
plt.ylabel('Concentração')
plt.legend()
plt.grid(True)
plt.show()
