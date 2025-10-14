# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibs = [0, 0, 1]
        for i in range(3, n+1):
            fibs.append(fibs[i-1] + fibs[i-2] + fibs[i-3])
        return fibs[n]
