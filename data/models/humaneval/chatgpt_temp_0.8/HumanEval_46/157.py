# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    if n < 2:
        return 0
    a, b, c, d = 0, 0, 2, 0
    for i in range(3, n+1):
        d = a + b + c + d
        a, b, c = b, c, d
    return d
