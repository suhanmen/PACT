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

    # Check if a is greater than b and if so, swap their values
    if a > b:
        a, b = b, a

    # Iterate through the range from a to b (inclusive)
    for num in range(a, b+1):

        # Convert num to a string to check each digit
        num_str = str(num)

        # Iterate through each digit in num
        for digit in num_str:

            # Check if the digit is even and if so, add it to the list of even digits
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Return the list of even digits in ascending order
    return sorted(even_digits)
