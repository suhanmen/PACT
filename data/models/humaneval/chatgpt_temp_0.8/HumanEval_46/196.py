def fib4(n: int):
    fib_sequence = [0, 0, 2, 0] + [0]*(n-3) # initialize the first few elements of the sequence
    for i in range(4, n+1):
        fib_sequence[i%4] = fib_sequence[(i-1)%4] + fib_sequence[(i-2)%4] + fib_sequence[(i-3)%4] + fib_sequence[(i-4)%4] # calculate the i-th element of the sequence
    return fib_sequence[n%4]
