def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib_seq = [0, 0, 2, 0, 0]
        for i in range(4, n+1):
            fib_seq[i%5] = fib_seq[(i-1)%5] + fib_seq[(i-2)%5] + fib_seq[(i-3)%5] + fib_seq[(i-4)%5]
        return fib_seq[n%5]
