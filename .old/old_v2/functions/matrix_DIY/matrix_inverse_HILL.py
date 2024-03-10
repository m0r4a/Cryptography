from .matrix_determinant_HILL import matrix_determinant_HILL
from .matrix_adjungate_HILL import matrix_adjugate_HILL

import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="script to calculate the inverse of a matrix")

    parser.add_argument("-m", metavar="matrix", nargs='+', type=str, required=True, help="matrix rows separated by commas")
    parser.add_argument("-n", metavar="mod", type=int, required=True, help="modulo to apply to the result")

    args = parser.parse_args()

    matrix = [list(map(int, row.split(','))) for row in args.m]

    return args.n, matrix


def matrix_inverse_HILL(n, matrix):
    """
    Function to calculate the inverse matrix given the modulus, determinant, and adjugate.

    :param int n: The modulus
    :param int determinant: The determinant of the matrix
    :param list adjugate: The adjugate matrix of the original matrix

    :return: The inverse matrix
    """

    adjugate = matrix_adjugate_HILL(n, matrix)

    determinant = matrix_determinant_HILL(n, matrix)

    # Calculate the determinant inverse modulo n
    det_inverse = pow(determinant, -1, n)

    # Calculate the scalar inverse modulo n
    scalar_inverse = det_inverse % n

    # Calculate the inverse matrix elements
    inverse = [[(elem * scalar_inverse) % n for elem in row] for row in adjugate]

    return inverse


def main():
    try:
        n, matrix = process_arguments()

        inverse_matrix_val = matrix_inverse_HILL(n, matrix)

        print("--- Inverse Matrix ---\n\n", inverse_matrix_val)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
