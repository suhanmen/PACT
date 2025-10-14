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
    start, end = min(a, b), max(a, b)
    for i in range(start, end+1):
        digits = [int(x) for x in str(i)]
        for d in digits:
            if d % 2 == 0 and d not in result:
                result.append(d)
    return result
