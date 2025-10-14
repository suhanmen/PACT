def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        # initialize the sequence with the first four elements
        seq = [0, 0, 2, 0]
        for i in range(4, n+1):
            # compute the next element using the previous four
            seq[i % 4] = sum(seq)
        return seq[n % 4]
