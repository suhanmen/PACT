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

    # Swap a and b if a is greater than b
    if a > b:
        a, b = b, a

    # Loop through the range between a and b
    for i in range(a, b+1):
        # Convert i to a string so that we can loop through its digits
        for digit in str(i):
            # Check if the digit is even and not already in the list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                # Append the even digit to the list
                even_digits.append(int(digit))

    # Sort the list in ascending order
    even_digits.sort()

    return even_digits
