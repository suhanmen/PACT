def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b, c, d = 1, 1, 1, 0
    n -= 2  # to handle the edge case when n is 2
    while n:
        if n % 2:
            a, b, c, d = (a + b + d) * c, a * c + b * d, (a + b) * d, (b * b + c * c)
            n -= 1
        else:
            a, b, c, d = (a * a + b * c) * 2, (a + b) * (a + d), (a + c) * (b + d), (b * c + d * d)
            n //= 2
    return a
