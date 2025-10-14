# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        a, b, c = 1, 1, 0
        for _ in range(2, n):
            c = a + b + c
            a, b = b, c
        return c
