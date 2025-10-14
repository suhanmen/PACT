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

    # Loop through the range of numbers from a to b (inclusive)
    for num in range(a, b + 1):
        # Convert the number to a string to access its individual digits
        num_str = str(num)
        # Loop through the individual digits of the number
        for digit in num_str:
            # Convert the digit back to an integer
            digit_int = int(digit)
            # Check if the digit is even and not already in the even_digits list
            if digit_int % 2 == 0 and digit_int not in even_digits:
                even_digits.append(digit_int)

    # Return the sorted list of even digits
    return sorted(even_digits)
