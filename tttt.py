import time
import pandas as pd
import os
import psutil

# Funciones para medir el uso de memoria
def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 ** 2  # convertir bytes a MB

# Leer archivo usando read()
def read_method(file_path):
    start_time = time.time()
    mem_before = memory_usage()
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    mem_after = memory_usage()
    elapsed_time = time.time() - start_time
    
    return elapsed_time, mem_after - mem_before

# Leer archivo usando readline()
def readline_method(file_path):
    start_time = time.time()
    mem_before = memory_usage()
    
    with open(file_path, 'r') as file:
        while file.readline():
            pass
    
    mem_after = memory_usage()
    elapsed_time = time.time() - start_time
    
    return elapsed_time, mem_after - mem_before

# Leer archivo usando readlines()
def readlines_method(file_path):
    start_time = time.time()
    mem_before = memory_usage()
    
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    mem_after = memory_usage()
    elapsed_time = time.time() - start_time
    
    return elapsed_time, mem_after - mem_before

# Leer archivo usando pandas
def pandas_method(file_path):
    start_time = time.time()
    mem_before = memory_usage()
    
    df = pd.read_csv(file_path)
    
    mem_after = memory_usage()
    elapsed_time = time.time() - start_time
    
    return elapsed_time, mem_after - mem_before

# Ruta del archivo de prueba (asegúrate de que esta ruta sea correcta)
file_path = 'C:/Users/USER/Documents/codigos/large_file.csv'

# Ejecutar los métodos y recoger los resultados
results = {
    'Method': [],
    'Time (s)': [],
    'Memory (MB)': []
}

methods = {
    'read()': read_method,
    'readline()': readline_method,
    'readlines()': readlines_method,
    'pandas.read_csv()': pandas_method
}

for method_name, method in methods.items():
    time_taken, memory_used = method(file_path)
    results['Method'].append(method_name)
    results['Time (s)'].append(time_taken)
    results['Memory (MB)'].append(memory_used)

# Crear un DataFrame para visualizar los resultados
results_df = pd.DataFrame(results)
print(results_df)

# Graficar los resultados
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Method')
ax1.set_ylabel('Time (s)', color=color)
ax1.bar(results_df['Method'], results_df['Time (s)'], color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Memory (MB)', color=color)
ax2.plot(results_df['Method'], results_df['Memory (MB)'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Performance Comparison of File Reading Methods')
plt.show()

