from functions.tools.letter_to_number import letter_to_number
from functions.tools.number_to_letter import number_to_letter

from functions.tools.list_to_HILL import list_to_HILL
from functions.matrix_DIY.matrix_inverse_HILL import matrix_inverse_HILL
from functions.matrix_DIY.matrix_multiplication_HILL_3x3 import matrix_multiplication_HILL_3x3


# Seccion de datos

n = 26
block_size = 2
N = (n ** block_size)

texto_plano1 = "HIJOCOMOVAELSEMESTREZZZ"
texto_plano2 = "DESEOPASARLOSEXAMENES"
texto_plano3 = "EXAGERATUSALEGRIASACADEMICASSIEMPREZ"

m = texto_plano1

# Proceso de encriptacion

print("------ ENCRIPTANDO ------\n\nTexto: ", m)

numeros_planos = letter_to_number(n, block_size, m)
print("\nNumeros planos: ", numeros_planos)

numeros_planos_listos_para_multiplicar = list_to_HILL(block_size, numeros_planos)
print("\nMatriz creada lista para multiplicar: ", numeros_planos_listos_para_multiplicar)

# HILL C = P * K mod n

matriz = [[8, 9], [7, 4]]


numeros_encriptados = matrix_multiplication_HILL_3x3(n, numeros_planos_listos_para_multiplicar, matriz)
print("Numeros encriptados: ", numeros_encriptados)


texto_encriptado = number_to_letter(n, block_size, numeros_encriptados)
print("Texto encriptado: ", texto_encriptado)


# Proceso de desencriptacion

print("\n\n------ Desencriptando ------\nMensaje encriptado: ", texto_encriptado)

# HILL P = C * K^-1 mod n

matriz_invertida = matrix_inverse_HILL(n, matriz)
print("\nLa matriz invertida es igual a: ", matriz_invertida)

numeros_desencriptados = matrix_multiplication_HILL_3x3(n, numeros_encriptados, matriz_invertida)
print("Numeros desencriptados: ", numeros_desencriptados)
