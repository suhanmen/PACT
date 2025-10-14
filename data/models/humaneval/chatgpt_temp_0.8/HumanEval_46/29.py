def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 0:
        raise ValueError("n must be a positive integer")

    # Base Cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize variables for the last 4 numbers in the sequence
    n1, n2, n3, n4 = 0, 0, 2, 0

    # Loop through the rest of the sequence up to n
    for i in range(4, n+1):
        # Calculate the next number in the sequence
        next_num = n1 + n2 + n3 + n4

        # Update the last 4 numbers in the sequence
        n1, n2, n3, n4 = n2, n3, n4, next_num
