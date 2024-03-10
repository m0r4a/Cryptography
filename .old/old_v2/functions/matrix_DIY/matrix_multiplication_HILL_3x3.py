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


def matrix_multiplication_HILL_3x3(n, vector, matrix):
    """
    Function to multiply a vector or multiple vectors by a matrix

    This was succesfully tested with a 3x3 matrix

    :param int n: The modulo to apply to the result
    :param list vectors: This is either a single vector or a list of vectors to be multiplied by the matrix
    :param list matrix: This is the matrix to be multiplied by the vector(s)

    :return: The resulting vector or list of vectors obtained upon the multiplication
    """
    # If vectors is not a list, convert it into a list with a single element
    if not isinstance(vector, list):
        vector = [vector]

    # If vectors is a list of integers, convert it into a list of a single vector
    if all(isinstance(v, int) for v in vector):
        vector = [vector]

    # Check if the dimensions match
    for v in vector:
        if len(v) != len(matrix):
            raise ValueError("The size of the vector does not match the number of rows in the matrix.")

    # Initialize the result list
    results = []

    # Perform multiplication for each vector
    for v in vector:
        max_length = max(len(row) for row in matrix)
        for row in matrix:
            if len(row) < max_length:
                row.extend([0] * (max_length - len(row)))

        result = [0] * len(matrix[0])

        for i in range(len(v)):
            for j in range(len(matrix[0])):
                result[j] += v[i] * matrix[i][j]

        # Apply modulo n to each element of the result
        result = [x % n for x in result]

        results.append(result)

    # If there was only one input vector, return a single result
    if len(results) == 1:
        return results[0]
    else:
        return results


def main():
    try:
        vector, matrix, n = process_arguments()
        result = matrix_multiplication_HILL_3x3(n, vector, matrix)
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

