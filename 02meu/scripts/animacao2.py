import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
scat = ax.scatter([], [], c='red')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    data = np.random.rand(10, 2) * 10  # 10 pontos aleatórios
    scat.set_offsets(data)
    return scat,

ani = FuncAnimation(fig, update, frames=50, init_func=init, blit=True, interval=200)
plt.show()