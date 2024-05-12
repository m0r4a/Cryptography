#!/bin/python3

import argparse
import sys


def process_arguments():
    parser = argparse.ArgumentParser(description="Script to find the Greatest Common Divisor (GCD) using the Euclidean algorithm")

    # Create a group for required arguments
    required_group = parser.add_argument_group("Required arguments")
    required_group.add_argument("-a", metavar="(First number)", type=int, help="First number (a)")
    required_group.add_argument("-b", metavar="(Second number)", type=int, help="Second number (b)")

    args = parser.parse_args()

    # Check if all required arguments are present
    if not all((args.a, args.b)):
        parser.print_usage()
        sys.exit("Arguments -a and -b are required. Usage: -a (first number) -b (second number)")

    return args.a, args.b


def euclidean_alg(a: int, b: int):
    """
    Function to find the Greatest Common Divisor (GCD) using the Euclidean algorithm

    :param int a: This is the x value in the [a,b] = [x,y]
    :param int b: This is the y value in the [a,b] = [x,y]

    :return: The greatest common divisor
    """

    procedure = []

    while b != 0:
        procedure.append((a, b))
        a, b = b, a % b

    procedure.append((a, b))

    # Print the procedure if called as script with arguments
    if len(sys.argv) > 1:
        print("Complete procedure:")
        for step in procedure[:-1]:
            print(f"{step[0]} = ({step[1]})({step[0] // step[1]}) + {step[0] % step[1]}")

    result = procedure[-2][1]

    return result


if __name__ == "__main__":
    # Process command-line arguments
    a, b = process_arguments()

    # Perform Euclidean algorithm
    result = euclidean_alg(a, b)

    # Print the result
    print(f"\nGCD = {result}")
