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
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize the Fib4 sequence list with the first four numbers
        fib4_seq = [0, 0, 2, 0]
        for i in range(3, n+1):
            # Calculate each successive number in the sequence using the formula
            fib4_seq[i%4] = fib4_seq[(i-1)%4] + fib4_seq[(i-2)%4] + fib4_seq[(i-3)%4] + fib4_seq[(i-4)%4]
        return fib4_seq[n%4]
