def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Convert a and b to strings to check their digits
    a_str = str(a)
    b_str = str(b)

    # Initialize a list to store the even digits
    even_digits = []

    # Iterate through the digits of a and b and check if they are even
    for digit in a_str + b_str:
        if int(digit) % 2 == 0:
            even_digits.append(int(digit))

    # Return the even digits in ascending order
    return sorted(even_digits)
