import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to multiply a vector by a matrix")

    parser.add_argument("-v", metavar="vector", type=str, required=True, help="Vector separated by commas")
    parser.add_argument("-m", metavar="matrix", nargs='+', type=str, required=True, help="Matrix rows separated by commas")
    parser.add_argument("-n", metavar="mod", type=int, required=True, help="Modulo to apply to the result")

    args = parser.parse_args()

    vector = list(map(int, args.v.split(',')))
    matrix = [list(map(int, row.split(','))) for row in args.m]

    return vector, matrix, args.n


def matrix_multiplication_HILL_HW5(n, vector, matrix):
    """
    Function to multiply a vector or multiple vectors by a matrix

    This was used with a 2x2 matrix multiplying a 1x2 matrix

    :param int n: The modulo to apply to the result
    :param list vector: This is either a single vector or a list of vectors to be multiplied by the matrix
    :param list matrix: This is the matrix to be multiplied by the vector(s)

    :return: The resulting vector or list of vectors obtained upon the multiplication
    """
    # If vector is not a list, convert it into a list with a single element
    if not isinstance(vector[0], list):
        vector = [vector]

    # Check if the dimensions match
    if len(matrix[0]) != len(vector[0]):
        raise ValueError("The number of columns in the matrix does not match the length of the vector.")

    # Initialize the result list
    results = []

    # Perform multiplication for each vector
    for v in vector:
        # Check if the number of elements in the vector matches the number of columns in the matrix
        if len(v) != len(matrix[0]):
            raise ValueError("The length of the vector does not match the number of columns in the matrix.")

        result = []
        for row in matrix:
            dot_product = sum((x * y) % n for x, y in zip(row, v))
            result.append(dot_product % n)
        results.append(result)

    # If there was only one input vector, return a single result
    if len(results) == 1:
        return results[0]
    else:
        return results


def main():
    try:
        vector, matrix, n = process_arguments()
        result = matrix_multiplication_HILL(n, vector, matrix)
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
