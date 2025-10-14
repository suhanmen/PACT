def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c, d = 0, 0, 1, 1
        for i in range(3, n+1):
            a, b, c, d = b, c, d, a+b+c
        return d
