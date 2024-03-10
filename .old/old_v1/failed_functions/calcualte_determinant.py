#!/bin/python3

import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to calculate the determinant of a square matrix")

    # Add required arguments for the matrices
    parser.add_argument("-m1", metavar="(Row of the matrix 1)", type=str, required=True, help="First row of the matrix separated by commas")
    parser.add_argument("-m2", metavar="(Row of the matrix 2)", type=str, required=True, help="Second row of the matrix separated by commas")
    parser.add_argument("-m3", metavar="(Row of the matrix 3)", type=str, help="Third row of the matrix separated by commas")

    args = parser.parse_args()

    matrix = []

    for i in range(1, 4):
        row_str = getattr(args, f"m{i}")
        if row_str:
            row = list(map(int, row_str.split(',')))
            matrix.append(row)

    return matrix


def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def determinant_3x3(matrix):
    det = 0
    for i in range(3):
        det += matrix[0][i] * (matrix[1][(i+1)%3] * matrix[2][(i+2)%3] - matrix[1][(i+2)%3] * matrix[2][(i+1)%3])
    return det


def calculate_determinant(*rows) -> int:
    '''
    Function to calculate the determinant of the given matrix

    :param rows: This should be two or three list of rows to form the matrix
    '''

    matrix_size = len(rows)

    if matrix_size == 2:
        for row in rows:

            try:
                row_size = len(row)
            except TypeError:
                print("The matix should be square. (Same amount of elements as rows")

        return determinant_2x2(rows)

    elif matrix_size == 3:
        for row in rows:
            row_size = len(row)
            print(row_size)
            if row_size != matrix_size:
                raise ValueError("The matix should be square. (Same amount of elements as rows")

        return determinant_3x3(rows)

    else:
        raise ValueError("Only supports matrices of size 2x2 and 3x3")


def main():
    try:
        matrix = process_arguments()

        for i, row in enumerate(matrix, start=1):
            print(row)

        det = calculate_determinant(matrix)
        print(f"Determinant: {det}\n")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
