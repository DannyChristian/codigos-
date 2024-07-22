import numpy as np
from collections import Counter

def entropy(data):
    counter = Counter(data)
    total = len(data)
    entropy = 0
    for count in counter.values():
        probability = count / total
        entropy -= probability * np.log2(probability)
    return entropy

# Conjuntos de datos de ejemplo
data1 = ['A', 'B', 'A', 'A', 'B', 'C', 'B', 'A', 'B' ,'D', 'E', 'F']
data2 = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'C']

# Calcular entropía de cada conjunto de datos
entropy1 = entropy(data1)
entropy2 = entropy(data2)

# Mostrar resultados
print(f"Entropía del conjunto de datos 1: {entropy1:.4f} bits")
print(f"Entropía del conjunto de datos 2: {entropy2:.4f} bits")
