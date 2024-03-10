import numpy as np


def matrix_multiplication_generic(mod, matrix1, matrix2):
    """
    Function to multiply two matrices using NumPy and apply modulo afterward

    :param int mod: The modulo to apply to the result
    :param numpy.ndarray matrix1: The first matrix
    :param numpy.ndarray matrix2: The second matrix

    :return: The resulting matrix obtained upon the multiplication with modulo applied
    """
    result = np.dot(matrix1, matrix2)
    return result % mod
