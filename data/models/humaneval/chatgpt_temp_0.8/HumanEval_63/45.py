# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 1
    a, b, c, d = 0, 0, 1, 1
    for i in range(3, n+1):
        a, b, c = b, c, d
        d = a + b + c
    return d
