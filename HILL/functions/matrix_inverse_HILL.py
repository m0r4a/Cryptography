import numpy as np


def determinant_modulo(matrix, N):
    det = int(round(np.linalg.det(matrix))) % N
    return det


def adjoint_modulo(matrix, N):
    adjoint = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix))
    adjoint = adjoint.astype(int) % N
    return adjoint


def matrix_inverse_HILL(N, matrix):
    """
    Function to get the inverse for HILL encryption method

    :param int N: The size of the alphabet ^ block size (modulo value)
    :param np.ndarray matrix: The matrix which will be inversed

    :return: The inverse of the matrix
    """
    try:
        det_modulo = determinant_modulo(matrix, N)
        adjoint = adjoint_modulo(matrix, N)
        det_inverse = pow(det_modulo, -1, N)

        # Calculate the inverse using the adjoint and the inverse of the determinant
        inverse = (det_inverse * adjoint) % N

        return inverse

    except np.linalg.LinAlgError:
        print("The matrix is not invertible.")

        return None
