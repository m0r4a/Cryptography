#!/bin/python3

import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to transform string into its numeric representation")

    # Create a group for required arguments
    required_group = parser.add_argument_group("Required arguments")
    required_group.add_argument("-n", metavar="(Alphabet size)", required=True, type=int, help="This is the alphabeth size without any exponential value")
    required_group.add_argument("-b", metavar="(Block size)", required=True, type=int, help='This is the graph "level"')
    required_group.add_argument("-m", metavar="(String)", required=True, type=str, help="This is the string you want to convert into a number")

    args = parser.parse_args()

    return args.n, args.b, args.m


def char_to_number(char):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chars = "@#$%^&*!(){}[]|\\/<>+=_-;:.,"
    if char in special_chars:
        return len(string) + special_chars.index(char)
    elif char in string:
        return string.index(char)
    else:
        return "Char not found"


def letter_to_number(alphabet_size: int, block_size: int, string):
    """
    Function to transform letters into numbers according to the AFIN encryption method.

    :param int alphabet_size: This is the amount of characters you have in your alphabet
    :param int block_size: This is the graph "level"
    :param str string: This is the string you want to convert into a number

    :return: The number obtained upon the letters
    """

    # Divide el string en bloques del tamaño especificado
    blocks = [string[i:i + block_size] for i in range(0, len(string), block_size)]

    # Convierte cada bloque en su representación numérica
    decimal_values = []
    for block in blocks:
        decimal_value = 0
        for i, char in enumerate(reversed(block)):
            # Convertir el carácter a su número correspondiente
            numeric_value = char_to_number(char)
            decimal_value += int(numeric_value) * (alphabet_size ** i)
        decimal_values.append(decimal_value)

    return decimal_values


def main():
    # Procesar los argumentos de la línea de comandos
    alphabet_size, block_size, string = process_arguments()

    # Convertir el string en su representación numérica
    decimal_values = letter_to_number(alphabet_size, block_size, string)

    # Imprimir los valores decimales
    print("Decimal values:")
    print(decimal_values)


if __name__ == "__main__":
    main()
