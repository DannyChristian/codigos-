import time
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os
import psutil

# Función para medir el tiempo de ejecución y el uso de memoria
def medir_rendimiento(metodo, archivo):
    inicio_tiempo = time.time()
    inicio_memoria = psutil.Process(os.getpid()).memory_info().rss / 1024  # en kilobytes

    if metodo == 'read()':
        with open(archivo, 'r') as f:
            f.read()
    elif metodo == 'readline()':
        with open(archivo, 'r') as f:
            while f.readline():
                pass
    elif metodo == 'readlines()':
        with open(archivo, 'r') as f:
            f.readlines()
    elif metodo == 'pandas':
        pd.read_csv(archivo)

    fin_tiempo = time.time()
    fin_memoria = psutil.Process(os.getpid()).memory_info().rss / 1024  # en kilobytes

    tiempo_transcurrido = fin_tiempo - inicio_tiempo
    uso_memoria = fin_memoria - inicio_memoria

    return tiempo_transcurrido, uso_memoria

# Función para generar gráfico de barras
def graficar_resultados(resultados):
    metodos = [resultado[0] for resultado in resultados]
    tiempos = [resultado[1] for resultado in resultados]
    memorias = [resultado[2] for resultado in resultados]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.bar(metodos, tiempos, color='blue', alpha=0.7)
    ax1.set_ylabel('Tiempo de Ejecución (segundos)')
    ax1.set_title('Comparación de Tiempo de Ejecución por Método')

    ax2.bar(metodos, memorias, color='green', alpha=0.7)
    ax2.set_ylabel('Uso de Memoria (KB)')
    ax2.set_title('Comparación de Uso de Memoria por Método')

    plt.tight_layout()
    st.pyplot(fig)

# Streamlit UI
st.title('Comparación de Métodos de Lectura de Archivos y pandas para CSV')

# Selección de archivo CSV desde el usuario
archivo_csv = st.file_uploader("Selecciona un archivo CSV", type=['csv'])

# Ejecutar la medición de rendimiento al hacer clic en un botón
if archivo_csv and st.button('Ejecutar'):
    # Guardar el archivo temporalmente
    with open(archivo_csv.name, 'wb') as f:
        f.write(archivo_csv.getvalue())

    # Lista de métodos y medición de rendimiento
    metodos = ['read()', 'readline()', 'readlines()', 'pandas']
    resultados = []

    for metodo in metodos:
        tiempo, memoria = medir_rendimiento(metodo, archivo_csv.name)
        resultados.append((metodo, tiempo, memoria))

    # Eliminar el archivo temporal
    os.remove(archivo_csv.name)

    # Mostrar resultados en tabla
    st.subheader('Resultados:')
    df_resultados = pd.DataFrame(resultados, columns=['Método', 'Tiempo (segundos)', 'Memoria (KB)'])
    st.write(df_resultados)

    # Graficar resultados
    st.subheader('Gráficos de Comparación:')
    graficar_resultados(resultados)

# Información adicional o conclusiones
st.markdown("""
### Conclusión
Los resultados pueden variar según el tamaño y la estructura del archivo. `read()` y `readlines()` pueden consumir más memoria dependiendo del tamaño del archivo, mientras que `readline()` lee línea por línea, lo que puede ser más eficiente en términos de memoria para archivos muy grandes. Por otro lado, `pandas` está optimizado para manejar archivos CSV grandes de manera eficiente en términos de rendimiento y manejo de memoria.
""")
