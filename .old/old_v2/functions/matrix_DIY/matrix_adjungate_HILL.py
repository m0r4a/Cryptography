import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to calculate the adjugate of a matrix")

    parser.add_argument("-m", metavar="matrix", nargs='+', type=str, required=True, help="Matrix rows separated by commas")
    parser.add_argument("-n", metavar="mod", type=int, required=True, help="Modulo to apply to the result")

    args = parser.parse_args()

    matrix = [list(map(int, row.split(','))) for row in args.m]

    return matrix, args.n


def minor(matrix, i, j):
    """
    Function to calculate the minor of a matrix for a given row and column.

    :param list matrix: The input matrix
    :param int i: The row index
    :param int j: The column index

    :return: The minor matrix
    """
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def determinant(matrix):
    """
    Function to calculate the determinant of a matrix.

    :param list matrix: The input matrix

    :return: The determinant value
    """
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(len(matrix)):
            det += ((-1) ** j) * matrix[0][j] * determinant(minor(matrix, 0, j))
        return det


def cofactor(matrix):
    """
    Function to calculate the cofactor matrix of a given matrix.

    :param list matrix: The input matrix

    :return: The cofactor matrix
    """
    cofactors = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            minor_mat = minor(matrix, i, j)
            cofactor_row.append(((-1) ** (i + j)) * determinant(minor_mat))
        cofactors.append(cofactor_row)
    return cofactors


def transpose(matrix):
    """
    Function to calculate the transpose of a matrix.

    :param list matrix: The input matrix

    :return: The transpose matrix
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def apply_modulo(matrix, n):
    """
    Function to apply modulo n to each element of a matrix.

    :param list matrix: The input matrix
    :param int n: The modulo

    :return: The matrix with modulo n applied to each element
    """
    return [[elem % n for elem in row] for row in matrix]


def matrix_adjugate_HILL(n, matrix):
    """
    Function to calculate the adjugate of a matrix with modulo n applied to each value.

    :param int n: The modulo to apply to the result
    :param list matrix: The input matrix

    :return: The adjugate matrix with modulo n applied to each value
    """
    cofactors = cofactor(matrix)
    adjugate = transpose(cofactors)
    adjugate_mod = apply_modulo(adjugate, n)
    return adjugate_mod


def main():
    try:
        matrix, n = process_arguments()
        adjugate_mod = matrix_adjugate_HILL(n, matrix)
        print("Adjugate Matrix:", adjugate_mod)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

