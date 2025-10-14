def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        a, b, c, d = 0, 0, 2, 0
        for _ in range(3, n+1):
            d = a + b + c + d
            a = b
            b = c
            c = d
        return d
