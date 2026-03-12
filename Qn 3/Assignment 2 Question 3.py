# Numeric Pyramid Generator
# Example for n = 4
#    1
#   121
#  12321
# 1234321


def get_user_input():
    """
    This function gets input from the user and validates it.
    It ensures the input is a positive integer.
    """
    try:
        n = int(input("Enter the number of rows: "))

        if n <= 0:
            print("Error: Please enter a positive integer.")
            return None

        return n

    except ValueError:
        # Handles cases where the user enters non-numeric input
        print("Error: Invalid input. Please enter a valid integer.")
        return None


def print_spaces(count):
    """
    Prints leading spaces for pyramid alignment.
    Uses a loop instead of string multiplication.
    """
    for i in range(count):
        print(" ", end="")


def print_ascending_numbers(limit):
    """
    Prints numbers from 1 up to 'limit'.
    Example: limit = 3 -> 123
    """
    for num in range(1, limit + 1):
        print(num, end="")


def print_descending_numbers(start):
    """
    Prints numbers from start-1 down to 1.
    Example: start = 3 -> 21
    """
    for num in range(start - 1, 0, -1):
        print(num, end="")


def generate_pyramid(n):
    """
    Generates the numeric pyramid using nested loops.
    """

    for row in range(1, n + 1):

        # Print leading spaces
        print_spaces(n - row)

        # Print ascending numbers
        print_ascending_numbers(row)

        # Print descending numbers
        print_descending_numbers(row)

        # Move to next line
        print()


def main():
    """
    Main program controller.
    """

    n = get_user_input()

    # If input is valid, generate pyramid
    if n is not None:
        generate_pyramid(n)


# Run the program
main()