def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    for num in range(a, b+1):
        even_digits = [int(digit) for digit in str(num) if int(digit) % 2 == 0]
        if len(even_digits) > 0:
            result.extend(even_digits)
    return sorted(result)
