import time
import random

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

tamanos_lista = [1000, 10000, 100000, 1000000]
resultados = []

for tamano in tamanos_lista:
    lista = sorted(random.sample(range(tamano * 2), tamano))
    objetivo = random.choice(lista)

    tiempo_inicio = time.time()
    busqueda_lineal(lista, objetivo)
    tiempo_lineal = time.time() - tiempo_inicio

    tiempo_inicio = time.time()
    busqueda_binaria(lista, objetivo)
    tiempo_binaria = time.time() - tiempo_inicio

    resultados.append((tamano, tiempo_lineal, tiempo_binaria))

print(f"{'Tamaño Lista':<15} {'Tiempo Búsqueda Lineal':<25} {'Tiempo Búsqueda Binaria':<25}")
for tamano, tiempo_lineal, tiempo_binaria in resultados:
    print(f"{tamano:<15} {tiempo_lineal:<25.6f} {tiempo_binaria:<25.6f}")
