import time
import matplotlib.pyplot as plt

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return end_time - start_time

sizes = list(range(2, 951))  # Cambio en el rango de números para calcular el factorial
recursive_times = []
iterative_times = []

for size in sizes:
    recursive_times.append(measure_time(factorial_recursive, size))
    iterative_times.append(measure_time(factorial_iterative, size))

plt.figure(figsize=(10, 5))
plt.plot(sizes, recursive_times, label='Recursivo')
plt.plot(sizes, iterative_times, label='Iterativo')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo de ejecución (s)')
plt.title('Comparación de rendimiento: Factorial Recursivo vs Iterativo')
plt.legend()
plt.show()

