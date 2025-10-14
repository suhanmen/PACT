# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Recursive case
    else:
        a, b, c = 0, 0, 1
        for i in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c
