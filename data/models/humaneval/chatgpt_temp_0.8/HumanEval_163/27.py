def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Convert a and b to strings so we can iterate over their digits
    a_str = str(a)
    b_str = str(b)

    # Initialize an empty list to hold the even digits we find
    even_digits = []

    # Iterate over the digits in a and b
    for digit in a_str + b_str:
        # Check if the digit is even
        if int(digit) % 2 == 0:
            # If it's even, add it to our list (if it's not already there)
            if int(digit) not in even_digits:
                even_digits.append(int(digit))

    # Sort the even digits in ascending order and return the list
    return sorted(even_digits)
