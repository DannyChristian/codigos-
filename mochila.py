import streamlit as st

def knapsack(W, weights, values, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

st.title("Problema de la Mochila")

W = st.number_input("Capacidad de la Mochila", min_value=1)
weights_input = st.text_input("Pesos de los Objetos (separados por comas)")
values_input = st.text_input("Valores de los Objetos (separados por comas)")

if st.button("Calcular Valor Máximo"):
    try:
        weights = list(map(int, weights_input.split(',')))
        values = list(map(int, values_input.split(',')))
        n = len(weights)
        if n != len(values):
            st.error("El número de pesos y valores debe ser igual.")
        else:
            max_value = knapsack(W, weights, values, n)
            st.success(f"El valor máximo que se puede obtener es: {max_value}")
    except ValueError:
        st.error("Por favor, ingresa números válidos para pesos y valores.")

