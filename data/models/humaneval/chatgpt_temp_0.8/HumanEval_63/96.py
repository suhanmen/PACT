def fibfib(n: int):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        a, b, c = 1, 1, 0
        for i in range(3, n+1):
            fib = a + b + c
            c = b
            b = a
            a = fib
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
