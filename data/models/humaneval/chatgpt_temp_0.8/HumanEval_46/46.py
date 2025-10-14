def fib4(n: int):
    a, b, c, d = 0, 0, 2, 0
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    else:
        for i in range(3, n+1):
            d = a + b + c + d
            a, b, c = b, c, d
        return d
