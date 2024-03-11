import numpy as np


def matrix_multiplication_HILL(N: int, matrices: list, matrix: np.ndarray) -> list:
    """
    Function to multiply each matrix in the list by the given matrix modulo n for HILL encryption method

    :param int N: The size of the alphabet ^ to the block size
    :param list matrices: List of numpy matrices
    :param np.ndarray matrix: The matrix to multiply each matrix in the list by

    :return: A list of numpy matrices resulting from the multiplication
    """
    result = [(np.dot(mat, matrix) % N).flatten().tolist() for mat in matrices]
    return result


# Define matrices and matrix
matrices = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
matrix = np.array([[1, 0], [0, 1]])

result = matrix_multiplication_HILL(N=26, matrices=matrices, matrix=matrix)
print(result)
