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
        # Initialize a list to store the last 4 Fib4 numbers
        fib4_list = [0, 0, 2, 0]
        for i in range(3, n+1):
            # Compute the next Fib4 number by summing the last 4 numbers
            next_fib4 = fib4_list[1] + fib4_list[2] + fib4_list[3]
            # Update the list to include the next Fib4 number
            fib4_list = fib4_list[1:] + [next_fib4]
        return fib4_list[3]
