# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f0 = 0   # fibfib(n-3)
        f1 = 0   # fibfib(n-2)
        f2 = 1   # fibfib(n-1)
        for i in range(3, n+1):
            f3 = f0 + f1 + f2   # fibfib(n)
            f0 = f1
            f1 = f2
            f2 = f3
        return f3
