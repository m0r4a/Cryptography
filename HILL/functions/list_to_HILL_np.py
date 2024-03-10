import numpy as np


def list_to_HILL_np(matrix_size: int, numbers: list) -> list:
    """
    Function to convert a list of numbers into an array usable for Hill encryption

    !!!THIS n IS NOT THE SAME AS THE n OF THE ALPHABET SIZE!!!

    :param int matrix_size: The size of each sublist
    :param list numbers: The list of numbers to be partitioned for transformation into numbers

    :return: A list of numpy matrices separated by sublists of size n
    """
    if matrix_size <= 0:
        raise ValueError("The size of each sublist must be greater than 0")

    # Calculate the number of sublists needed
    num_sublists = -(-len(numbers) // matrix_size)  # Equivalent to ceil(len(numbers) / n)

    # Create the list of matrices
    result = [np.array(numbers[i * matrix_size: (i + 1) * matrix_size]).reshape(1, -1) for i in range(num_sublists)]

    return result
