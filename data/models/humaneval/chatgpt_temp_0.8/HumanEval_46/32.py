def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib = [0, 0, 2, 0]
        for i in range(3, n+1):
            fib[3] = fib[2] + fib[1] + fib[0] + fib[3]
            fib[0], fib[1], fib[2] = fib[1], fib[2], fib[3]
        return fib[3]
