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
    # Check if a is less than b, if not swap their values
    if a > b:
        a, b = b, a
    
    # Iterate over the range [a, b] and check if each number has even digits
    for num in range(a, b+1):
        digits = list(str(num))
        for digit in digits:
            if int(digit) % 2 == 0:
                result.append(num)
                break
    
    return result
