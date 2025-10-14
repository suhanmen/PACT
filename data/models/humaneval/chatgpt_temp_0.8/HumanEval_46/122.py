def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        # initialize the sequence
        fib_seq = [0, 0, 2, 0]
        for i in range(4, n+1):
            # compute the next number in the sequence using the previous four
            fib_seq[i % 4] = fib_seq[(i-1) % 4] + fib_seq[(i-2) % 4] + fib_seq[(i-3) % 4] + fib_seq[(i-4) % 4]
        return fib_seq[n % 4]
