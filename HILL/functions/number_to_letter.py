import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to transform decimal numbers into letter representation")

    # Create a group for required arguments
    required_group = parser.add_argument_group("Required arguments")
    required_group.add_argument("-n", metavar="(Alphabet size)", required=True, type=int, help="The amount of characters in your alphabet")
    required_group.add_argument("-b", metavar="(Block size)", required=True, type=int, help="The graph level of your encryption")
    required_group.add_argument("-m", metavar="(n1,n2,n3...nm)", required=True, type=str, help="The numbers you want to transform into letters separated by commas")

    args = parser.parse_args()

    return args.n, args.b, args.m


def number_to_char(num):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chars = "@#$%^&*!(){}[]|\\/<>+=_-;:.,"
    if num < len(string):
        return string[num]
    elif num < len(string) + len(special_chars):
        return special_chars[num - len(string)]
    else:
        return "Index out of range"


def number_to_letter(alphabet_size: int, block_size: int, decimal_values):
    """
    Function to transform numbers into letters according to the AFIN encryption method.

    :param int alphabet_size: This is the amount of characters you have in your alphabet
    :param int block_size: This is the graph "level"
    :param str or list or list of lists decimal_values: The numbers you want to transform into letters separated by commas. It can be a single string, a list of numbers, or a list of lists of numbers.

    :return: The letter obtained upon the numbers
    """

    if isinstance(decimal_values[0], list):  # If decimal_values is a list of lists
        # Flatten the list of lists
        decimal_values = [item for sublist in decimal_values for item in sublist]
    elif isinstance(decimal_values, str):  # If decimal_values is a string, split it into a list of numbers
        decimal_values = [int(num) for num in decimal_values.split(',')]

    string = ""

    for value in decimal_values:
        block = ""
        while value > 0 or len(block) < block_size:
            quotient = value // alphabet_size
            remainder = value % alphabet_size
            char = number_to_char(remainder)
            block = char + block
            value = quotient
        # Rellenar con 'A' si es necesario
        while len(block) < block_size:
            block = 'A' + block
        string += block

    return string


def main():
    # Procesar los argumentos de la línea de comandos
    alphabet_size, block_size, numbers = process_arguments()

    # Convertir los valores decimales a su representación de letras
    string = number_to_letter(alphabet_size, block_size, numbers)

    # Imprimir la representación de letras resultante
    print(f"String representation: {string}")


if __name__ == "__main__":
    main()
