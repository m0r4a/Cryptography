def list_to_HILL(n: int, numbers: list) -> list:
    """
    Function to convert a list of numbers into an array usable for Hill encryption

    !!!THIS n IS NOT THE SAME AS THE n OF THE ALPHABET SIZEi!!!

    :param int n: The size of each sublist
    :param list numbers: The list of numbers to be partitioned for transformation into numbers

    :return: A list of your numbers separated by sublists of size n
    """
    if n <= 0:
        raise ValueError("The size of each sublist must be greater than 0")

    # Calculate the number of sublists needed
    num_sublists = -(-len(numbers) // n)  # Equivalent to ceil(len(numbers) / n)

    # Create the list of lists
    result = [numbers[i * n: (i + 1) * n] for i in range(num_sublists)]

    return result
