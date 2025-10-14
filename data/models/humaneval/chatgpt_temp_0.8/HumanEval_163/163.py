def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = [str(i) for i in range(0, 10, 2)]
    result = []
    for num in range(a, b+1):
        for digit in str(num):
            if digit in even_digits and int(digit) not in result:
                result.append(int(digit))
    return result
