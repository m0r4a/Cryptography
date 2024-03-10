#!/bin/python3

import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to calculate the determinant of a square matrix")

    parser.add_argument("-n", metavar="(Alphabet size)", required=True, type=int, help="The amout of characters in your alphabet")
    parser.add_argument("-m", metavar="rows", nargs='+', type=str, required=True, help="Matrix rows separated by commas")

    args = parser.parse_args()

    matrix = [list(map(int, row.split(','))) for row in args.m]

    return args.n, matrix


def matrix_determinant_HILL(n, matrix):
    '''
    This function calcualtes the determinant of the matrix for HILL algorithm
    the only difference between this and a regular determinant calculation
    is that the final result will be result mod n

    : param int n: your alphabet size
    : param list matrix: the matrix which will be the determinant calculated
    '''

    size = len(matrix)
    if size == 1:
        return matrix[0][0]

    # Check if the matrix is square
    for row in matrix:
        if len(row) != size:
            raise ValueError("The matrix must be square (same number of rows and columns)")

    det = 0
    for j in range(size):
        minor = [[matrix[i][k] for k in range(size) if k != j] for i in range(1, size)]
        det += ((-1) ** j) * matrix[0][j] * matrix_determinant_HILL(n, minor)

    det = det % n

    return det


def main():
    try:
        n, matrix = process_arguments()

        for i, row in enumerate(matrix, start=1):
            print(row)

        det = matrix_determinant_HILL(n, matrix)  # Aquí se pasa el valor 'n'
        print(f"Determinant: {det}\n")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
