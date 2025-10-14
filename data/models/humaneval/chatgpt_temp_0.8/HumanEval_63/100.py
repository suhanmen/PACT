# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0
        b = 0
        c = 1
        for i in range(3, n+1):
            d = a + b + c
            a = b
            b = c
            c = d
        return c
