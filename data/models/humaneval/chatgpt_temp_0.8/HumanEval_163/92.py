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

    # Loop through the range of numbers from a to b
    for num in range(a, b + 1):

        # Convert the number to a string to access the individual digits
        num_str = str(num)

        # Loop through the digits of the number
        for digit in num_str:

            # Check if the digit is even
            if int(digit) % 2 == 0:

                # Add the even digit to the list
                even_digits.append(int(digit))

    # Remove duplicates from the list
    even_digits = list(set(even_digits))

    # Sort the list in ascending order
    even_digits.sort()

    # Return the list of even digits
    return even_digits
