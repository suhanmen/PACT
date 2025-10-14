# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_0 = 0
        fibfib_1 = 0
        fibfib_2 = 1
        fibfib_n = 0
        for i in range(3, n+1):
            fibfib_n = fibfib_0 + fibfib_1 + fibfib_2
            fibfib_0 = fibfib_1
            fibfib_1 = fibfib_2
            fibfib_2 = fibfib_n
        return fibfib_n
