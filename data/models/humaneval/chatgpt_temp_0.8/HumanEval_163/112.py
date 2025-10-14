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
    result = []

    # Loop through the range between a and b, inclusive
    for num in range(min(a, b), max(a, b) + 1):
        # Convert the integer to a string to access its digits
        digits = str(num)
        # Check if any of the digits are even
        if any(int(digit) % 2 == 0 for digit in digits):
            # If so, add the number to the result list
            result.append(num)

    # Return the result list
    return result
