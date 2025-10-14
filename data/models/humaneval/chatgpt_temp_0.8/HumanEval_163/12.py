def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Initialize an empty list to store the even digits
    even_digits = []

    # Iterate over the range between a and b, inclusive
    for i in range(a, b+1):
        # Convert the integer to a string so we can access its digits
        digits = str(i)
        # Iterate over the digits and add any even digits to the list
        for digit in digits:
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Remove any duplicates from the list and sort it in ascending order
    even_digits = sorted(list(set(even_digits)))

    return even_digits
