import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

# Función para leer el archivo de texto y convertirlo en un DataFrame
def leer_archivo(file):
    numeros = []
    
    for line in file:
        try:
            numero = float(line.strip())
            numeros.append(numero)
        except ValueError:
            st.error(f"La línea '{line}' no tiene un número válido.")
    
    df = pd.DataFrame({
        'Número': numeros
    })
    
    return df

# Función para calcular estadísticas descriptivas
def calcular_estadisticas(df):
    estadisticas = {
        'Media': df['Número'].mean(),
        'Mediana': df['Número'].median(),
        'Moda': df['Número'].mode()[0] if not df['Número'].mode().empty else np.nan,
        'Rango': df['Número'].max() - df['Número'].min(),
        'Varianza': df['Número'].var(),
        'Desviación Estándar': df['Número'].std()
    }
    return estadisticas

st.title("Cuadro Unidimensional Estadístico")

# Subida de archivo
uploaded_file = st.file_uploader("Sube un archivo de texto", type="txt")

if uploaded_file is not None:
    st.write("Contenido del archivo:")
    content = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.text(content.getvalue())
    
    # Procesar el archivo
    df = leer_archivo(content)
    
    if not df.empty:
        st.write("Datos procesados:")
        st.dataframe(df)
        
        # Calcular y mostrar estadísticas descriptivas
        st.write("Estadísticas Descriptivas:")
        estadisticas = calcular_estadisticas(df)
        for clave, valor in estadisticas.items():
            st.write(f"{clave}: {valor}")
    else:
        st.error("El archivo no contiene datos válidos.")
else:
    st.info("Por favor, sube un archivo de texto.")
