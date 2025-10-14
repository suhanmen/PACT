def fib4(n: int):
    if n <= 1:
        return 0
    if n == 2:
        return 2
    a, b, c, d = 0, 0, 2, 0
    for i in range(3, n+1):
        d = a + b + c + d
        a, b, c = b, c, d
    return d
