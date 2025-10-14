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

    # Iterate through the range from a to b, inclusive
    for num in range(a, b+1):
        # Convert the number to a string to easily access each digit
        str_num = str(num)

        # Check each digit to see if it's even
        for digit in str_num:
            if int(digit) % 2 == 0:
                # If the digit is even, add it to the list
                even_digits.append(int(digit))
    
    # Sort and return the list of even digits
    return sorted(even_digits)
