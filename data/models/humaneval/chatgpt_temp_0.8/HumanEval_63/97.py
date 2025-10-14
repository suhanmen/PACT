def fibfib(n: int):
    if n < 2:
        return 0
    if n == 2:
        return 1
    a, b, c = 0, 0, 1
    for i in range(2, n):
        a, b, c = b, c, a + b + c
    return c
