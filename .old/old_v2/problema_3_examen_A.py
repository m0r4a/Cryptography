from functions.tools.letter_to_number import letter_to_number
from functions.AFIN.AFIN_encrypt import AFIN_encrypt
from functions.tools.number_to_letter import number_to_letter
from functions.AFIN.inverse_a import inverse_a
from functions.AFIN.AFIN_decrypt import AFIN_decrypt


# Seccion de datos

n = 31
block_size = 3
a = 11
b = 29
N = (n ** block_size)

texto_plano1 = "HIJOCOMOVAELSEMESTREZ"
texto_plano2 = "DESEOPASARLOSEXAMENES"
texto_plano3 = "EXAGERATUSALEGRIASACADEMICASSIEMPREZ"

m = texto_plano2

# Proceso de encriptacion

print("------ ENCRIPTANDO ------\n\nTexto: ", m)

numeros_planos = letter_to_number(n, block_size, m)
print("\nNumeros planos: ", numeros_planos)

numeros_encriptados = AFIN_encrypt(N, a, b, numeros_planos)
print("\nNumeros encriptados: ", numeros_encriptados)

mensaje_encriptado = number_to_letter(n, block_size, numeros_encriptados)
print("\nMensaje encriptado: ", mensaje_encriptado)

# Proceso de desencriptacion

print("\n\n------ Desencriptando ------\nMensaje encriptado: ", mensaje_encriptado)

a_inversa = inverse_a(a, N)
print(f"\na original: {a} y su inversa {a_inversa}")

numeros_test = letter_to_number(n, block_size, mensaje_encriptado)
print("\nNumeros test: estos deberan ser los numeros del  mensaje encriptado: ", numeros_test)

numeros_desencriptados = AFIN_decrypt(N, a_inversa, b, numeros_test)
print("\nNumeros desencriptados: ", numeros_desencriptados)

texto_desencriptado = number_to_letter(n, block_size, numeros_desencriptados)
print("\nTexto desencriptado: ", texto_desencriptado)
