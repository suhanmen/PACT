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

    # Ensure that a is smaller than or equal to b
    if a > b:
        a, b = b, a

    # Loop through the range of integers from a to b (inclusive)
    for num in range(a, b+1):
        # Convert the integer to a string so we can check each digit
        str_num = str(num)
        # Loop through each digit in the string
        for digit in str_num:
            # Check if the digit is even and not already in the list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                even_digits.append(int(digit))

    # Return the list of even digits in ascending order
    return sorted(even_digits)
