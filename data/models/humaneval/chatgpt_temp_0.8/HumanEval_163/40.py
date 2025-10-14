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

    # Check which value is the minimum and maximum of the two inputs
    min_value = min(a, b)
    max_value = max(a, b)

    # Loop through the numbers between min_value and max_value
    for i in range(min_value, max_value + 1):
        # Convert the number to a string so we can work with individual digits
        digits = str(i)
        # Loop through the digits and check if each one is even
        for digit in digits:
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Sort and return the list of even digits
    return sorted(even_digits)
