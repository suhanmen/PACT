def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    
    # initialize the Fib4 number sequence
    fib_seq = [0] * (n + 1)
    fib_seq[2] = 2
    
    # calculate the rest of the sequence
    for i in range(3, n + 1):
        fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2] + fib_seq[i - 3] + fib_seq[i - 4]
    
    return fib_seq[n]
