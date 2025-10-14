def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a # swap a and b if a is greater than b
    result = []
    for i in range(a, b+1):
        for j in str(i):
            if int(j) % 2 == 0:
                result.append(int(j))
    return sorted(set(result)) # return sorted unique even digits
