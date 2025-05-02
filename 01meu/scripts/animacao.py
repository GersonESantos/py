import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurar figura e eixos
fig, ax = plt.subplots()
x_data = []
y_data = []
line, = ax.plot([], [], 'b-', lw=2)  # Linha inicial (vazia)

# Definir limites do gráfico
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.set_title("Animação de Seno em Tempo Real")

# Função de inicialização
def init():
    line.set_data([], [])
    return line,

# Função de atualização (chamada a cada frame)
def update(frame):
    x = np.linspace(0, 10, 1000)
    y = np.sin(x + 0.5 * frame)  # Movimento senoidal
    line.set_data(x, y)
    return line,

# Criar animação
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

# Mostrar animação
plt.show()