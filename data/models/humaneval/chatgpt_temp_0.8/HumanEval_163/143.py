python
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
    for n in range(min(a, b), max(a, b) + 1):
        digits = [int(d) for d in str(n)]
        for digit in digits:
            if digit % 2 == 0:
                result.append(digit)
    return sorted(list(set(result)))
