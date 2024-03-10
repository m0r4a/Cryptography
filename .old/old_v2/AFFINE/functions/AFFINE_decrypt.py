import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to decrypt a number encrypted by the AFFINE method")

    # Create a group for required arguments
    required_group = parser.add_argument_group("Required arguments")
    required_group.add_argument("-N", metavar="(Alphabet size)", required=True, type=int, help="The value of your alphabet raised to the graph level/block size")
    required_group.add_argument("-a", metavar="(Inverse of 'a')", required=True, type=int, help="The value of 'a' after the inverse function was used")
    required_group.add_argument("-b", metavar="(Original 'b')", required=True, type=int, help="The value of 'b' without any modification")
    required_group.add_argument("-m", metavar="(n1, n2, n3...nm)", required=True, type=str, help="The encrypted numbers to decrypt separated by commas")

    args = parser.parse_args()

    return args.N, args.a, args.b, args.m


def AFFINE_decrypt(N, a_inverse, original_b, encrypted_numbers):
    """
    Function to decrypt numbers encrypted by the AFFINE method

    :param int N: This is the alphabet size raised to the power of the block size (n ^ block_size)
    :param int a_inverse: Is the value of the a after the inverse function was used
    :param int original_b: Is the value of b without any modification
    :param list encrypted_numbers: The list of encrypted numbers to decrypt

    Important note, N is the value which will be the mod of the encryption

    :return: The list of decrypted numbers
    """
    decrypted_numbers = []

    for number in encrypted_numbers:
        try:
            decrypted_number = (a_inverse * (number - original_b)) % N
            decrypted_numbers.append(decrypted_number)
        except TypeError:
            decrypted_number = (a_inverse * (int(number) - original_b)) % N
            decrypted_numbers.append(decrypted_number)

    return decrypted_numbers


def main():
    # Process command-line arguments
    N, a_inv, original_b, numbers = process_arguments()

    try:
        encrypted = [int(num) for num in numbers.split(',')]
    except AttributeError:
        encrypted = numbers

    # Decrypt the number
    result = AFFINE_decrypt(N, a_inv, original_b, encrypted)

    # Print the result
    print(f"Decrypted numbers = {result}")


if __name__ == "__main__":
    main()
