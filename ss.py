dimport time
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Generar listas de diferentes tamaños
list_sizes = [1000, 10000, 100000, 1000000]
results = []

for size in list_sizes:
    arr = sorted(random.sample(range(size * 2), size))
    target = random.choice(arr)

    # Medir tiempo de búsqueda lineal
    start_time = time.time()
    linear_search(arr, target)
    linear_time = time.time() - start_time

    # Medir tiempo de búsqueda binaria
    start_time = time.time()
    binary_search(arr, target)
    binary_time = time.time() - start_time

    results.append((size, linear_time, binary_time))

# Imprimir resultados
print(f"{'List Size':<10} {'Linear Search Time':<20} {'Binary Search Time':<20}")
for size, linear_time, binary_time in results:
    print(f"{size:<10} {linear_time:<20.6f} {binary_time:<20.6f}")
