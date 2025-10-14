def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        fib_0, fib_1, fib_2, fib_3 = 0, 0, 2, 0
        for i in range(4, n+1):
            fib_3, fib_2, fib_1, fib_0 = fib_2, fib_1, fib_0, fib_0 + fib_1 + fib_2 + fib_3
        return fib_0 + fib_1 + fib_2 + fib_3
