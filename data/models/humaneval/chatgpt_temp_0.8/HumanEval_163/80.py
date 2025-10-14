def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = []

    # Swap a and b if a is greater than b
    if a > b:
        a, b = b, a

    # Iterate from a to b (inclusive) and check for even digits
    for num in range(a, b+1):
        for digit in str(num):
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Return a list of unique even digits in ascending order
    return sorted(list(set(even_digits)))
