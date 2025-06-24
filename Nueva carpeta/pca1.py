import numpy as np
import matplotlib.pyplot as plt

# Creamos datos simulados (2 variables fuertemente correlacionadas)
np.random.seed(42)
altura = 160 + 10 * np.random.randn(50)
peso = 50 + 0.5 * altura + 5 * np.random.randn(50)

# Graficamos los datos originales
plt.figure(figsize=(7, 6))
plt.scatter(altura, peso)
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Datos originales: Altura vs Peso')
plt.grid()
plt.show()
