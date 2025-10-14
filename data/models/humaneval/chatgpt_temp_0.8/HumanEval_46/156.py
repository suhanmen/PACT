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
        # Initialize the list with the first 4 elements of the sequence
        fib_seq = [0, 0, 2, 0]  
        for i in range(4, n+1):
            # Compute the next element of the sequence by summing the previous 4 elements
            fib_seq[i % 4] = sum(fib_seq)  
        return fib_seq[n % 4]
