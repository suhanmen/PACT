def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Initialize list to store even digits
    even_digits = []

    # Ensure a is less than or equal to b
    if a > b:
        a, b = b, a

    # Loop through range from a to b
    for num in range(a, b+1):

        # Convert number to string for digit-wise processing
        num_str = str(num)

        # Loop through digits in number and check if even
        for digit in num_str:
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Remove duplicates and sort list
    even_digits = list(set(even_digits))
    even_digits.sort()

    return even_digits
