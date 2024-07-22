import random
import time
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from fpdf import FPDF

def busqueda_lineal(array, numero):
    inicio = time.perf_counter()
    iteraciones = 0
    for i in range(len(array)):
        iteraciones += 1
        if array[i] == numero:
            fin = time.perf_counter()
            return i, iteraciones, fin - inicio
    fin = time.perf_counter()
    return -1, iteraciones, fin - inicio

st.title('Simulación de Búsqueda Lineal')
resultados = []

for ensayo in range(1, 101):
    tamano_arreglo = ensayo * 100
    array = [random.randint(0, 100) for _ in range(tamano_arreglo)]
    numero_a_buscar = random.randint(0, 100)
    resultado, iteraciones, tiempo_total = busqueda_lineal(array, numero_a_buscar)
    resultados.append({
        'Ensayo': int(ensayo),
        'Tamaño del arreglo': int(tamano_arreglo),
        'Número a buscar': int(numero_a_buscar),
        'Iteraciones': int(iteraciones),
        'Tiempo total (s)': round(tiempo_total, 8)
    })

df_resultados = pd.DataFrame(resultados)

# Gráfico de Volumen y Tiempo
plt.figure(figsize=(10, 6))
plt.plot(df_resultados['Tamaño del arreglo'], df_resultados['Tiempo total (s)'], marker='o', label='Tiempo total (s)')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo total (s)')
plt.title('Gráfico de Volumen y Tiempo')
plt.grid(True)
plt.legend()
st.pyplot(plt)

# Gráfico de Tiempo e Iteración
plt.figure(figsize=(10, 6))
plt.plot(df_resultados['Iteraciones'], df_resultados['Tiempo total (s)'], marker='o', color='orange', label='Tiempo total (s)')
plt.xlabel('Iteraciones')
plt.ylabel('Tiempo total (s)')
plt.title('Gráfico de Tiempo e Iteración')
plt.grid(True)
plt.legend()
st.pyplot(plt)

st.write('## Resultados de la Búsqueda Lineal')
st.dataframe(df_resultados)

def generar_pdf(dataframe):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, txt='Resultados de la Búsqueda Lineal', ln=True, align='C')

    pdf.set_font('Arial', 'B', 10)
    for col in dataframe.columns:
        pdf.cell(40, 10, col, border=1)
    pdf.ln()

    pdf.set_font('Arial', '', 10)
    for index, row in dataframe.iterrows():
        for col in dataframe.columns:
            if col in ['Ensayo', 'Tamaño del arreglo', 'Número a buscar', 'Iteraciones']:
                pdf.cell(40, 10, str(int(row[col])), border=1)
            elif col == 'Tiempo total (s)':
                pdf.cell(40, 10, f"{row[col]:.8f}", border=1)
        pdf.ln()

    return pdf

if st.button('Descargar resultados como PDF'):
    pdf = generar_pdf(df_resultados)
    pdf_file = 'resultados_busqueda_lineal.pdf'
    pdf.output(pdf_file)
    with open(pdf_file, 'rb') as f:
        st.download_button('Descargar PDF', f, file_name=pdf_file)
