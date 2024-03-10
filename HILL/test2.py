import numpy as np
from functions.letter_to_number import letter_to_number
from functions.number_to_letter import number_to_letter
from functions.list_to_HILL_np import list_to_HILL_np
from functions.matrix_inverse_HILL import matrix_inverse_HILL
from functions.matrix_multiplication_HILL import matrix_multiplication_HILL


# Seccion de datos

n = 37
block_size = 2
matrix_size = 2
N = (n ** block_size)

texto_plano1 = "HIJOCOMOVAELSEMESTRE"
texto_plano2 = "DESEOPASARLOSEXAMENESZZZ"
texto_plano3 = "EXAGERATUSALEGRIASACADEMICASSIEMPREZ"

m = texto_plano2

matrix = np.array([[6, 8], [12, 10]])

# Proceso de encriptacion

print("------ Encontrando la matriz inversa ------\n\nTexto: ", matrix)

inverse = matrix_inverse_HILL(n, matrix)
print("\nMatriz inversa: ", inverse)

print("------ ENCRIPTANDO ------\n\nTexto: ", m)

numeros_planos = letter_to_number(n, block_size, m)
print("\nNumeros planos: ", numeros_planos)

numeros_planos_listos = list_to_HILL_np(matrix_size, numeros_planos)
print("\nMatriz creada lista para multiplicar: \n", numeros_planos_listos)

numeros_encriptados = matrix_multiplication_HILL(N, numeros_planos_listos, matrix)
print("\n\n --- Resultado ---", numeros_encriptados)

texto_encriptado = number_to_letter(n, block_size, numeros_encriptados)
print("Texto encriptado: ", texto_encriptado)


print("\n\n------ Desencriptando ------\nMensaje encriptado: ", texto_encriptado)

numeros_encriptados = letter_to_number(n, block_size, texto_encriptado)
print("Numeros encriptados que deberian ser iguales a el resultado", numeros_encriptados)

numeros_encriptados_listos = list_to_HILL_np(matrix_size, numeros_encriptados)
print("Numeros encriptados listos", numeros_encriptados_listos)

# HILL P = C * K^-1 mod n

matriz_invertida = matrix_inverse_HILL(N, matrix)
print("\nLa matriz invertida es igual a: ", matriz_invertida)

numeros_desencriptados = matrix_multiplication_HILL(N, numeros_encriptados_listos, matriz_invertida)

# Redondear los valores de los números desencriptados al entero más cercano
numeros_desencriptados = [[round(num) for num in sublist] for sublist in numeros_desencriptados]

print("Numeros desencriptados: ", numeros_desencriptados)

texto_desencriptado = number_to_letter(n, block_size, numeros_desencriptados)
print("\n\nTexto desencriptado: ", texto_desencriptado)
