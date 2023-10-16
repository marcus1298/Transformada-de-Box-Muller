import numpy as np
import matplotlib.pyplot as plt

def box_muller_transform(n):
    # Gerar dois conjuntos de números aleatórios uniformemente distribuídos
    u1 = np.random.rand(n)
    u2 = np.random.rand(n)

    # Aplicar a Transformada de Box-Muller
    z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)

    return z0, z1

# Gerar 1 milhão de pontos usando a Transformada de Box-Muller
num_points = 1000000
z0, z1 = box_muller_transform(num_points)

# Criar o gráfico do histograma
plt.hist(z0, bins=100, density=True, alpha=0.75, color='b', label='Histograma')
plt.title('Histograma da Distribuição Normal')
plt.xlabel('Valores')
plt.ylabel('Densidade')
plt.legend()
plt.show()