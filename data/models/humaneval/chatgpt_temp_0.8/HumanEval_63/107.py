def fibfib(n: int):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    # Recursive case
    else:
        fibfib_n_minus_1 = 1
        fibfib_n_minus_2 = 0
        fibfib_n_minus_3 = 0
        for i in range(3, n+1):
            # Compute the next FibFib number using the last three FibFib numbers
            fibfib_n = fibfib_n_minus_1 + fibfib_n_minus_2 + fibfib_n_minus_3
            fibfib_n_minus_3 = fibfib_n_minus_2
            fibfib_n_minus_2 = fibfib_n_minus_1
            fibfib_n_minus_1 = fibfib_n
        return fibfib_n
