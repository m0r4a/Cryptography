#!/bin/python3

import argparse
import sys


def process_arguments():

    parser = argparse.ArgumentParser(description="Script to perform encryption using the AFFINE method")
    # Create a group for required arguments
    required_group = parser.add_argument_group("Required arguments")
    required_group.add_argument("-N", metavar="(Alphabet size raised)", type=int, help="Alphabet size raised to the power of the block size")
    required_group.add_argument("-a", metavar='(Value of "a")', type=int, help="This is the x value in the [a,b] = [x,y]")
    required_group.add_argument("-b", metavar='(Value of "b")', type=int, help="This is the y value in the [a,b] = [x,y]")
    required_group.add_argument("-m", metavar="(Number)", type=int, help="Represents the number you want to encrypt")

    args = parser.parse_args()

    # Check if all required arguments are present
    if not all((args.N, args.a, args.b, args.m)):
        parser.print_usage()
        sys.exit("Arguments -N, -a, -b, and -m are required. Usage: -N (alphabet size) -a (value of 'a') -b (value of 'b') -m (number to encrypt)")

    return args.N, args.a, args.b, args.m


def AFFINE_encrypt(N: int, a: int, b: int, number_to_encrypt):
    """
    Function to modify the numbers using the AFFINE encrypt method.

    :param int N: This is the alphabet size raised to the power of the block size (n ^ block_size)
    :param int a: This is the x value in the [a,b] = [x,y]
    :param int b: This is the y value in the [a,b] = [x,y]
    :param int number_to_encrypt: This is the number you want to encrypt using the AFIN method

    Important note, N is the value which will be the mod of the encryption

    :return: The number encrypted
    """

    result = []

    try:
        for number in number_to_encrypt:
            number_result = (a * number + b) % N
            result.append(number_result)
    except TypeError:
        number_result = (a * number_to_encrypt + b) % N
        result.append(number_result)

    return result


def main():
    # Process command-line arguments
    N, a, b, m = process_arguments()
    print(m)
    print(type(m))

    # Perform encryption
    encrypted_message = AFFINE_encrypt(N, a, b, m)

    # Print the encrypted message
    print("Encrypted message:", encrypted_message)


if __name__ == "__main__":
    main()
