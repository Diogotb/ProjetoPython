import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parâmetros do modelo para insulina
P = 0.1  # Produção de insulina pelo pâncreas
D = 0.02  # Degradação natural da insulina
G0 = 100   # Nível inicial de glicose (valor arbitrário)
S = 0.01  # Sensibilidade à glicose

# Sistema de equações diferenciais
def model(state, t):
    I, G = state
    dIdt = P - D * I - S * (G - G0) * I
    dGdt = 0  # Aqui, estamos mantendo a concentração de glicose constante, mas você pode adicionar um modelo de glicose mais complexo
    return [dIdt, dGdt]

# Condições iniciais
initial_state = [9, 100]  # Nível inicial de insulina e glicose

# Tempo
t = np.linspace(0, 240, 24*60)

# Resolvendo as equações diferenciais
solution = odeint(model, initial_state, t)

# Extraímos as soluções para I e G
I, G = solution.T

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(t, I, label='Insulina (I)')
plt.plot(t, G, label='Glicose (G)')
plt.title('Modelo de Insulina e Glicose')
plt.xlabel('Tempo')
plt.ylabel('Concentração')
plt.legend()
plt.grid(True)
plt.show()
