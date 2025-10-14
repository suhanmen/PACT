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

    # Initialize an empty list to hold the even digits
    even_digits = []

    # Iterate over the digits in a and b
    for digit in a_str + b_str:
        # Convert the digit back to an integer
        digit_int = int(digit)

        # Check if the digit is even and not already in the list
        if digit_int % 2 == 0 and digit_int not in even_digits:
            even_digits.append(digit_int)

    # Sort the list of even digits and return it
    return sorted(even_digits)
