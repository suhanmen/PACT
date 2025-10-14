def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        a, b, c, d = 0, 0, 2, 0
        for i in range(3, n+1):
            d = a + b + c + d
            a, b, c = b, c, d
        return d
