from functions.letter_to_number import letter_to_number
from functions.list_to_HILL_np import list_to_HILL_np
from functions.matrix_multiplication_HILL import matrix_multiplication_HILL
from functions.matrix_inverse_HILL import matrix_inverse_HILL
import numpy as np
from functions.number_to_letter import number_to_letter

# Seccion de datos

n = 26
block_size = 1
matrix_size = 3
N = (n ** block_size)

texto_plano1 = "HIJOCOMOVAELSEMESTREZZZ"
texto_plano2 = "DESEOPASARLOSEXAMENES"
texto_plano3 = "EXAGERATUSALEGRIASACADEMICASSIEMPREZ"
texto_testing = "PAYMOREMONEY"

m = texto_testing

# Proceso de encriptacion

print("------ ENCRIPTANDO ------\n\nTexto: ", m)

numeros_planos = letter_to_number(n, block_size, m)
print("\nNumeros planos: ", numeros_planos)

numeros_planos_listos_para_multiplicar = list_to_HILL_np(matrix_size, numeros_planos)
print("\nMatriz creada lista para multiplicar: \n", numeros_planos_listos_para_multiplicar)

# HILL C = P * K mod n

matriz = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

resultado = matrix_multiplication_HILL(n, numeros_planos_listos_para_multiplicar, matriz)
print("\n\n --- Resultado ---", resultado)

texto_encriptado = number_to_letter(n, block_size, resultado)
print("Texto encriptado: ", texto_encriptado)

# Proceso de desencriptacion

print("\n\n------ Desencriptando ------\nMensaje encriptado: ", texto_encriptado)

numeros_encriptados = letter_to_number(n, block_size, texto_encriptado)
print("Numeros encriptados que deberian ser iguales a el resultado", numeros_encriptados)

numeros_encriptados_listos = list_to_HILL_np(matrix_size, numeros_encriptados)
print("Numeros encriptados listos", numeros_encriptados_listos)

# HILL P = C * K^-1 mod n

matriz_invertida = matrix_inverse_HILL(n, matriz)
print("\nLa matriz invertida es igual a: ", matriz_invertida)

numeros_desencriptados = matrix_multiplication_HILL(n, numeros_encriptados_listos, matriz_invertida)

# Redondear los valores de los números desencriptados al entero más cercano
numeros_desencriptados = [[round(num) for num in sublist] for sublist in numeros_desencriptados]

print("Numeros desencriptados: ", numeros_desencriptados)

texto_desencriptado = number_to_letter(n, block_size, numeros_desencriptados)
print("\n\nTexto desencriptado: ", texto_desencriptado)
