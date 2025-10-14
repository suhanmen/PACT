# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 2
    a, b, c, d = 0, 0, 0, 2
    for i in range(3, n+1):
        a, b, c, d = b, c, d, a+b+c+d
    return d
