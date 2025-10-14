def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Create an empty list to store the even digits
    even_digits = []

    # Swap a and b if a is greater than b
    if a > b:
        a, b = b, a

    # Loop through the integers from a to b
    for i in range(a, b+1):
        # Convert the integer to a string and loop through its digits
        for digit in str(i):
            # Convert the digit back to an integer and check if it's even
            if int(digit) % 2 == 0:
                # Append the even digit to the list
                even_digits.append(int(digit))

    # Remove duplicates and sort the list
    even_digits = sorted(list(set(even_digits)))

    return even_digits
