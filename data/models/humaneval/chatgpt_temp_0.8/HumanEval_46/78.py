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
    if n <= 1:
        return 0
    if n == 2:
        return 2
    fib_list = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib_list[i%4] = fib_list[(i-1)%4] + fib_list[(i-2)%4] + fib_list[(i-3)%4] + fib_list[(i-4)%4]
    return fib_list[n%4]
