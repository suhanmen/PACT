def tri(n):
    """
    The Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    """
    if n == 0:
        return []
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 1]
    else:
        result = [3, 1, 2]
        a, b, c = 3, 1, 2
        for i in range(3, n + 1):
            if i % 2 == 0:
                x = 1 + i // 2
            else:
                x = a + b + c
                a, b, c = b, c, x
            result.append(x)
        return result
