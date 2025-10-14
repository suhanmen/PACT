def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        # initialize a list to store the last four values of the sequence
        last_four = [0, 0, 2, 0]
        # iterate through the sequence, updating the last_four list as we go
        for i in range(3, n+1):
            next_val = sum(last_four)
            # shift the last_four list to the right and update the last value
            last_four = [last_four[1], last_four[2], last_four[3], next_val]
        return last_four[-1]
