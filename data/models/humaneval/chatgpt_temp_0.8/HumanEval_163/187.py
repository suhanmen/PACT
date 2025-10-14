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

    # Make sure a is less than or equal to b
    if a > b:
        a, b = b, a

    # Loop through the range between a and b
    for num in range(a, b+1):
        # Convert the number to a string so we can loop through its digits
        num_str = str(num)
        for digit in num_str:
            # Check if the digit is even and add it to the even_digits list if it is
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Remove duplicates and sort the list in ascending order
    even_digits = list(set(even_digits))
    even_digits.sort()

    return even_digits
