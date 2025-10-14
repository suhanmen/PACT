def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Initialize an empty list to hold the even digits
    even_digits = []

    # Loop through the numbers from a to b (or b to a if a > b)
    for i in range(min(a, b), max(a, b) + 1):
        # Convert the number to a string and check each digit
        for digit in str(i):
            # Check if the digit is even and add it to the list if it is
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Sort the list in ascending order and return it
    return sorted(even_digits)
