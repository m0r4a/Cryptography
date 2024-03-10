import argparse


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to find the inverse of x using the Extended Euclidean algorithm")

    # Create a group for required arguments
    required_group = parser.add_argument_group("Required arguments")
    required_group.add_argument("-a", metavar="(First number)", required=True, type=int, help="First number (a)")
    required_group.add_argument("-N", metavar="(Alphabet size)", required=True, type=int, help="The value of your alphabet raised to the graph level/block size")

    args = parser.parse_args()

    return args.a, args.N


def cero_del(array):
    if array and array[0] == 0:
        del array[0]
    return array


def add_ceros(array):
    array.insert(0, 0)
    array.insert(0, 0)
    return array


def table_create(quotients):
    a_arr = [0, 1]
    N_arr = [1, 0]

    for i in range(2, len(quotients)):
        nuevo_a = quotients[i] * a_arr[i - 1] + a_arr[i - 2]
        nuevo_N = quotients[i] * N_arr[i - 1] + N_arr[i - 2]
        a_arr.append(nuevo_a)
        N_arr.append(nuevo_N)

    return quotients, a_arr, N_arr


def inverse_a(a: int, N: int):
    """
    Function to find the inverse of x using the Extended Euclidean algorithm

    :param int a: This is the x value in the [a,b] = [x,y]
    :param int N: This is the alphabet size raised to the power of the block size (n ^ block_size)

    Important note, N is the value which will be the mod of the encryption

    :return: The inverse of x
    """
    show_proc = []  # This is the array where the process is saved
    quotients = []  # Here are the quotients stored

    # This is the loop where the operations are actually done
    while N != 0:
        show_proc.append((a, N))
        quotient = a // N
        quotients.append(quotient)
        a, N = N, a % N

    show_proc.append((a, N))

    quotients = cero_del(quotients)
    quotients = add_ceros(quotients)

    T = (len(quotients) - 2)

    quotients, a_arr, N_arr = table_create(quotients)

    inverse_a = (((-1) ** (T + 1)) * a_arr[T])

    return inverse_a


def main():
    # Process command-line arguments
    a, N = process_arguments()

    # Find the inverse of x
    result = inverse_a(a, N)

    # Print the result
    print(f"Inverse of x = {result}")


if __name__ == "__main__":
    main()
