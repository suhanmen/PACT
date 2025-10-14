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
    
    for num in range(min(a, b), max(a, b) + 1):
        digits = [int(digit) for digit in str(num)]
        even_digits = [digit for digit in digits if digit % 2 == 0]
        if even_digits == digits:
            result.append(num)
    
    return result
