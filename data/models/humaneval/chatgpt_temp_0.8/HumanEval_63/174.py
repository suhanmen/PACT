# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        x, y, z = 0, 0, 1
        for i in range(3, n+1):
            x, y, z = y, z, x+y+z
        return z
