def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Swap values of a and b if a is greater than b
    if a > b:
        a, b = b, a

    # Initialize an empty list to store even digits
    even_digits = []

    # Iterate over the range between a and b (inclusive)
    for num in range(a, b+1):
        # Convert the number to a string to access individual digits
        for digit in str(num):
            # Check if the digit is even and not already in the list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                even_digits.append(int(digit))

    return even_digits
