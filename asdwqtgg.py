import math
from collections import Counter

def calculate_entropy(data):
    counter = Counter(data)
    total_count = len(data)
    probabilities = [count / total_count for count in counter.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy
data_set_1 = "AAAAABBBBCCCCDDDE"
data_set_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
entropy_set_1 = calculate_entropy(data_set_1)
entropy_set_2 = calculate_entropy(data_set_2)
print(f"Entropía del Conjunto de Datos 1: {entropy_set_1:.4f}")
print(f"Entropía del Conjunto de Datos 2: {entropy_set_2:.4f}")
import matplotlib.pyplot as plt
data_labels = ['Conjunto de Datos 1', 'Conjunto de Datos 2']
entropy_values = [entropy_set_1, entropy_set_2]
plt.bar(data_labels, entropy_values, color=['blue', 'green'])
plt.xlabel('Conjunto de Datos')
plt.ylabel('Entropía')
plt.title('Comparación de la Entropía entre dos Conjuntos de Datos')
plt.show()
