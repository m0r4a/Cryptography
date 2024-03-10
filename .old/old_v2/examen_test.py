from functions.tools.letter_to_number import letter_to_number
from functions.tools.number_to_letter import number_to_letter

texto_plano1 = "HIJOCOMOVAELSEMESTREZ"

n = 31
block_size = 3

print("Texto original: ", texto_plano1)

valor_numerico = letter_to_number(n, block_size, texto_plano1)
print("Valor numerico: ", valor_numerico)


r = number_to_letter(n, block_size, valor_numerico)
print("Texto: ", r)



