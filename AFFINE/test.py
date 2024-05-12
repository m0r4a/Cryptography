from functions.letter_to_number import letter_to_number
from functions.affine_encrypt import affine_encrypt
from functions.number_to_letter import number_to_letter
from functions.inverse_a import inverse_a
from functions.affine_decrypt import affine_decrypt


# declaring variables

n = 26
block_size = 1
a = 5
b = 4
n = (n ** block_size)

texto_plano1 = "hijocomovaelsemestrez"
texto_plano2 = "deseopasarlosexamenes"
texto_plano3z = "exageratusalegriasacademicassiemprez"
ejemplo = "et"

m = ejemplo

# encryption process

print("------ encrypting ------\n\ntext: ", m)

plain_numbers = letter_to_number(n, block_size, m)
print("\nplain numbers: ", plain_numbers)

encrypted_numbers = affine_encrypt(n, a, b, plain_numbers)
print("\nencrypted numbers: ", encrypted_numbers)

encrypted_message = number_to_letter(n, block_size, encrypted_numbers)
print("\nencrypted message: ", encrypted_message)


# decryption process

encrypted_message = "qaooyqqevheqv"

print("\n\n------ decrypting ------\nencrypted message: ", encrypted_message)

test_numbers = letter_to_number(n, block_size, encrypted_message)
print(f"\n## test numbers ##\nthese should be the numbers of the encrypted message: {test_numbers}")

a_inverse = inverse_a(a, n)
print(f"\noriginal a: {a} and its inverse {a_inverse}")

decrypted_numbers = affine_decrypt(n, a_inverse, b, test_numbers)
print("\ndecrypted numbers: ", decrypted_numbers)

decrypted_text = number_to_letter(n, block_size, decrypted_numbers)
print("\ndecrypted text: ", decrypted_text)
