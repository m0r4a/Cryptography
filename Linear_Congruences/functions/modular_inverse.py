import argparse
from sympy.ntheory.modular import solve_congruence


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to solve 2 or 3 linear congruences")
    parser.add_argument("-c1", metavar="congruence_1", type=str, required=True, help="First congruence separated by commas")
    parser.add_argument("-c2", metavar="congruence_2", type=str, required=True, help="Second congruence separated by commas")
    parser.add_argument("-c3", metavar="congruence_3", type=str, nargs='?', default=None, help="Third congruence separated by commas")

    args = parser.parse_args()

    congruence_1 = list(map(int, args.c1.split(',')))
    congruence_2 = list(map(int, args.c2.split(',')))
    congruence_3 = None

    if args.c3:
        congruence_3 = list(map(int, args.c3.split(',')))

    return congruence_1, congruence_2, congruence_3


def modular_inverse(arr1, arr2, arr3=None):
    """
    Function to solve linear congruences of 2 or 3 values

    :param list arr1: First array with the form (a, b) where a and b are integrers
    :param list arr2: Second array with the form (a, b) where a and b are integrers
    :param list arr3: Third array with the form (a, b) where a and b are integrers

    In the arrays, a and b represent a congruence with the form x = a (mod b)

    Uses the sympy library to calculate the result using the Chinese Remainder Theorem

    :return: The value of x for the congruences
    """

    if arr3:
        # Three congruences
        x = solve_congruence((arr1[0], arr1[1]), (arr2[0], arr2[1]), (arr3[0], arr3[1]))[0]
        return x % (arr1[1] * arr2[1] * arr3[1])
    else:
        # Two congruences
        x = solve_congruence((arr1[0], arr1[1]), (arr2[0], arr2[1]))[0]
        return x % (arr1[1] * arr2[1])


def main():
    try:
        congr_1, congr_2, congr_3 = process_arguments()

        if congr_3:
            result = modular_inverse(congr_1, congr_2, congr_3)
        else:
            result = modular_inverse(congr_1, congr_2)

        print("Value of X:", result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
