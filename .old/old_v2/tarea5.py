from functions.tools.letter_to_number import letter_to_number
from functions.tools.list_to_HILL import list_to_HILL
from functions.tools.number_to_letter import number_to_letter
from functions.matrix_DIY.matrix_inverse_HILL import matrix_inverse_HILL

from functions.matrix_DIY.matrix_multiplication_HILL_HW5 import matrix_multiplication_HILL_HW5

n = 26
mod = 1200
block_size = 2
matrix = [[7, 4], [5, 13]]
matrix_size = 2
m = 'GATOSZZZ'

# C = P * K mod (n)

plain_numers = letter_to_number(n, block_size, m)
print("Plain numbers", plain_numers)

plain_numers_matrix_ready = list_to_HILL(matrix_size, plain_numers)
print("Plain numbers after list to Hill: ", plain_numers_matrix_ready)

encrypted_numbers = matrix_multiplication_HILL_HW5(mod, plain_numers_matrix_ready, matrix)
print("\n\n\nNUMEROS ENCRIPTADOS", encrypted_numbers)

encrypted_text = number_to_letter(n, 3, encrypted_numbers)
print("Texto encriptado: ", encrypted_text)

encrypted_numbers = letter_to_number(n, 3, encrypted_text)
print("Numeros encryptados: ", encrypted_numbers)

encrypted_numbers_cleans = list_to_HILL(matrix_size, encrypted_numbers)
print("Numeros encriptados listos", encrypted_numbers_cleans)

matriz_inversa = matrix_inverse_HILL(mod, matrix)
print("Matriz inversa:", matriz_inversa)

numeros_desencriptados = matrix_multiplication_HILL_HW5(mod, encrypted_numbers_cleans, matriz_inversa)
print("Numeros desencriptados: ", numeros_desencriptados)

texto_desencriptado = number_to_letter(n, 1, numeros_desencriptados)
print("Texto desencriptado: ", texto_desencriptado)
