def fib4(n: int):
    # initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0
    # iterate from 4 to n
    for i in range(4, n+1):
        # compute the next element
        d = a + b + c + d
        # update the four elements
        a, b, c, d = b, c, d, 0
    # return the n-th element
    return d if n == 3 else c
