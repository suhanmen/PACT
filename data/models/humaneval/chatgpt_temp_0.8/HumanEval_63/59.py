# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        fibfib_n_1 = 1
        fibfib_n_2 = 1
        fibfib_n_3 = 0
        for i in range(3, n+1):
            fibfib_n = fibfib_n_1 + fibfib_n_2 + fibfib_n_3
            fibfib_n_3 = fibfib_n_2
            fibfib_n_2 = fibfib_n_1
            fibfib_n_1 = fibfib_n
        return fibfib_n
