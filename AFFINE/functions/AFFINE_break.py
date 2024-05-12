from .letter_to_number import letter_to_number
from .number_to_letter import number_to_letter
from .AFFINE_encrypt import AFFINE_encrypt
from .euclidean_alg import euclidean_alg


minimum_a_value = 1

minimum_b_value = 1
maximum_b_value = 1000


def coprime_values(n):
    return [i for i in range(minimum_a_value, n) if euclidean_alg(i, n) == 1]


def AFFINE_break(plain_text, encrypted_text, n, block_size=1, max_a=100000):
    """
    Function to bruteforce the values of a and b given an affine encrypt

    :param int n: This is the alphabet size
    :param int block_size: Is the level of graph u're using
    :param str plain_text: This is the plain text of the letters you know
    :param str encrypted_text: This is the encrypted text you've got

    This function abuses the fact that a has to be a coprime of N,
    greatly reducing the amount of testing that has to be done.

    :return: The possible values of a and b
    """

    i = 1
    N = n ** block_size

    coprime_list = coprime_values(N)

    for a in coprime_list:
        for b in range(minimum_b_value, maximum_b_value):
            plain_numbers = letter_to_number(n, block_size, plain_text)
            encrypted_numbers = AFFINE_encrypt(N, a, b, plain_numbers)
            encrypted_message = number_to_letter(n, block_size, encrypted_numbers)

#            print(f"Usando a: {a} y b:{b}\nEl mensaje que deberia de ser es: {encrypted_text} pero el que salio fue: {encrypted_message}")

            if encrypted_text == encrypted_message:
                print(f"\n\n--- Match {i} ---\nPossible value for a: {a}\nPossible value for b: {b}")
                i += 1
                value_found = True

    if value_found is False:
        print("No possible values for a or b were found")
