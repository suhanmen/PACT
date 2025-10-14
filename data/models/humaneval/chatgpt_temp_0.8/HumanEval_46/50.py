# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    if n < 2:
        return 0
    else:
        a, b, c, d = 0, 0, 2, 0
        for i in range(4, n+1):
            d, c, b, a = c + b + a + d, d, c, b
        return d
