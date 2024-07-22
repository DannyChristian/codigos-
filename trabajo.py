import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Personalización de estilos de gráficos
plt.style.use('Solarize_Light2')

def create_frequency_table(data, num_bins):
    df = pd.DataFrame(data, columns=['Valor'])
    data_range = df['Valor'].max() - df['Valor'].min()
    bin_width = data_range / num_bins
    bins = [df['Valor'].min() + i * bin_width for i in range(num_bins)] + [df['Valor'].max() + 1] # Ajuste en el último intervalo
    intervalos = [(round(bins[i], 2), round(bins[i+1], 2)) for i in range(len(bins)-1)]  
    
    # Calcula la marca de clase para cada intervalo
    marca_clase = [(intervalo[0] + intervalo[1]) / 2 if i < len(intervalos)-1 else intervalo[0] + bin_width / 2 for i, intervalo in enumerate(intervalos)]
    
    df['Intervalo'] = pd.cut(df['Valor'], bins, right=False)
    frequency_table = df['Intervalo'].value_counts().sort_index().reset_index()
    frequency_table.columns = ['Intervalo', 'Frecuencia']
    frequency_table['Frecuencia Relativa'] = frequency_table['Frecuencia'] / len(df)
    frequency_table['Frecuencia Acumulada'] = frequency_table['Frecuencia'].cumsum()
    frequency_table['Frecuencia Relativa Acumulada'] = frequency_table['Frecuencia Relativa'].cumsum()
    frequency_table['Marca de Clase'] = marca_clase
    frequency_table['Frecuencia Porcentil'] = frequency_table['Frecuencia Relativa'] * 100
    frequency_table['Frecuencia Porcentil Acumulada'] = frequency_table['Frecuencia Relativa Acumulada'] * 100
    frequency_table = frequency_table[['Intervalo', 'Marca de Clase', 'Frecuencia', 'Frecuencia Acumulada', 'Frecuencia Relativa', 'Frecuencia Relativa Acumulada', 'Frecuencia Porcentil', 'Frecuencia Porcentil Acumulada']] 
    frequency_table['Intervalo'] = intervalos
    
    # Calcular media, mediana, moda, rango, varianza y desviación estándar
    media = df['Valor'].mean()
    mediana = df['Valor'].median()
    moda = df['Valor'].mode()[0]  
    rango = df['Valor'].max() - df['Valor'].min()
    varianza = df['Valor'].var()
    desviacion_estandar = df['Valor'].std()
    
    return frequency_table, media, mediana, moda, rango, varianza, desviacion_estandar

def main():
    st.title("Cuadro Estadístico para Variable Cuantitativa Continua")
    
    # Opción para cargar un archivo de texto
    uploaded_file = st.file_uploader("Cargar archivo de texto", type=["txt"])
    
    if uploaded_file is not None:
        # Leer los datos del archivo de texto
        data = np.loadtxt(uploaded_file, dtype=float)
        
        # Número de intervalos (clases)
        num_bins = st.sidebar.selectbox("Número de intervalos", [5, 7, 9])
        
        frequency_table, media, mediana, moda, rango, varianza, desviacion_estandar = create_frequency_table(data, num_bins)

        # Visualizar tabla de frecuencias
        st.subheader("Tabla de Frecuencias")
        st.dataframe(frequency_table)

        # Mostrar estadísticas
        st.subheader("Estadísticas")

        show_mean = st.checkbox("Mostrar media", value=True)
        show_median = st.checkbox("Mostrar mediana", value=True)
        show_mode = st.checkbox("Mostrar moda", value=True)
        show_range = st.checkbox("Mostrar rango", value=True)
        show_variance = st.checkbox("Mostrar varianza", value=True)
        show_std_dev = st.checkbox("Mostrar desviación estándar", value=True)

        if show_mean:
            st.write(f"- Media: {media}")

        if show_median:
            st.write(f"- Mediana: {mediana}")

        if show_mode:
            st.write(f"- Moda: {moda}")

        if show_range:
            st.write(f"- Rango: {rango}")

        if show_variance:
            st.write(f"- Varianza: {varianza}")

        if show_std_dev:
            st.write(f"- Desviación Estándar: {desviacion_estandar}")

        # Graficar histograma
        st.subheader("Histograma")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(data, bins=num_bins, edgecolor='black', alpha=0.7)
        ax.set_title('Histograma de la Variable Cuantitativa Continua')
        ax.set_xlabel('Valor')
        ax.set_ylabel('Frecuencia')
        ax.grid(True)

        if st.button("Guardar histograma como PNG"):
            file_name = st.text_input("Nombre del archivo", value="histogram")
            plt.savefig(f"{file_name}.png")
            st.success(f"Histograma guardado como {file_name}.png")

        st.pyplot(fig)
        
        # Graficar polígono de frecuencias
        st.subheader("Polígono de Frecuencias")
        fig, ax = plt.subplots(figsize=(10, 6))
        marca_clase = frequency_table['Marca de Clase']
        frecuencia_relativa = frequency_table['Frecuencia Relativa']
        ax.plot(marca_clase, frecuencia_relativa, marker='o', linestyle='-')
        ax.set_title('Polígono de Frecuencias de la Variable Cuantitativa Continua')
        ax.set_xlabel('Marca de Clase')
        ax.set_ylabel('Frecuencia Relativa')
        ax.grid(True)

        if st.button("Guardar polígono de frecuencias como PNG"):
            file_name = st.text_input("Nombre del archivo", value="frequency_polygon")
            plt.savefig(f"{file_name}.png")
            st.success(f"Polígono de frecuencias guardado como {file_name}.png")

        st.pyplot(fig)
        
        # Graficar ojiva
        st.subheader("Ojiva")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(marca_clase, frequency_table['Frecuencia Acumulada'], marker='o', linestyle='-')
        ax.set_title('Ojiva de la Variable Cuantitativa Continua')
        ax.set_xlabel('Marca de Clase')
        ax.set_ylabel('Frecuencia Acumulada')
        ax.grid(True)

        if st.button("Guardar ojiva como PNG"):
            file_name = st.text_input("Nombre del archivo", value="ogive")
            plt.savefig(f"{file_name}.png")
            st.success(f"Ojiva guardada como {file_name}.png")

        st.pyplot(fig)

if __name__ == "__main__":
    main()