from functions.letter_to_number import letter_to_number
from functions.AFFINE_encrypt import AFFINE_encrypt
from functions.number_to_letter import number_to_letter
from functions.inverse_a import inverse_a
from functions.AFFINE_decrypt import AFFINE_decrypt


# Declaring variables

n = 31
block_size = 3
a = 11
b = 29
N = (n ** block_size)

texto_plano1 = "HIJOCOMOVAELSEMESTREZ"
texto_plano2 = "DESEOPASARLOSEXAMENES"
texto_plano3 = "EXAGERATUSALEGRIASACADEMICASSIEMPREZ"

m = texto_plano2

# Encryption process

print("------ ENCRYPTING ------\n\nText: ", m)

plain_numbers = letter_to_number(n, block_size, m)
print("\nPlain numbers: ", plain_numbers)

encrypted_numbers = AFFINE_encrypt(N, a, b, plain_numbers)
print("\nEncrypted numbers: ", encrypted_numbers)

encrypted_message = number_to_letter(n, block_size, encrypted_numbers)
print("\nEncrypted message: ", encrypted_message)


# Decryption process

print("\n\n------ Decrypting ------\nEncrypted message: ", encrypted_message)

test_numbers = letter_to_number(n, block_size, encrypted_message)
print(f"\n## Test numbers ##\nThese should be the numbers of the encrypted message: {test_numbers}")

a_inverse = inverse_a(a, N)
print(f"\nOriginal a: {a} and its inverse {a_inverse}")

decrypted_numbers = AFFINE_decrypt(N, a_inverse, b, test_numbers)
print("\nDecrypted numbers: ", decrypted_numbers)

decrypted_text = number_to_letter(n, block_size, decrypted_numbers)
print("\nDecrypted text: ", decrypted_text)
