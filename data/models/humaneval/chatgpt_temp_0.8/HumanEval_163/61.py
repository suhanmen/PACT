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

    # Iterate over the numbers between a and b
    for num in range(a, b+1):
        # Check if the number is even
        if num % 2 == 0:
            # Convert the number to a string and check if it contains an even digit
            if any(digit in ['0', '2', '4', '6', '8'] for digit in str(num)):
                # Add the number to the list of even digits
                even_digits.append(num)

    # Return the list of even digits
    return even_digits
