def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número
try:
    numero = int(input("Introduce un número entero no negativo: "))
    if numero < 0:
        print("El número debe ser no negativo.")
    else:
        resultado = factorial(numero)
        print(f"El factorial de {numero} es {resultado}")
except ValueError:
    print("Por favor, introduce un número entero válido.")
