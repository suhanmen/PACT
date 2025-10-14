# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    if n == 0:
        return 0
    elif n < 3:
        return 2**(n-1)
    else:
        a, b, c, d = 0, 0, 0, 2
        for i in range(3, n+1):
            a, b, c, d = b, c, d, a+b+c+d
        return d
