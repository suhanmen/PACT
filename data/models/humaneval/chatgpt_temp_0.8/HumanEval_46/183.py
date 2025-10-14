def fib4(n: int):
    if n == 0:
        return 0
    elif n <= 2:
        return 2 ** (n-1)
    else:
        fibs = [0, 0, 2, 0]
        for i in range(4, n+1):
            fibs[i%4] = sum(fibs)  # only store the last 4 fib4 numbers to save memory
        return fibs[n%4]
