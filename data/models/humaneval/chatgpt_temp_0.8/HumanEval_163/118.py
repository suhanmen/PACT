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
    for i in range(a, b+1):
        s = str(i)
        for j in range(len(s)):
            if int(s[j]) % 2 == 0:
                result.append(int(s[j]))
    return sorted(set(result))
