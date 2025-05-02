import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados aleatórios
import numpy as np
np.random.seed(0)
x = np.random.rand(50)
y = 2 * x + np.random.rand(50)

df = pd.DataFrame({"X": x, "Y": y})

# Gráfico de dispersão
sns.jointplot(x="X", y="Y", data=df, kind="scatter", color="purple")
plt.suptitle("Relação entre X e Y")
plt.tight_layout()
plt.show()