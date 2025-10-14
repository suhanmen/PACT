def fib4(n: int):
    # initialize the first four numbers in the sequence
    a, b, c, d = 0, 0, 2, 0

    # compute each successive number in the sequence using a loop
    for i in range(4, n+1):
        # update the variables for the previous four numbers in the sequence
        a, b, c, d = b, c, d, a+b+c+d
    # return the n-th element in the sequence
    return d
