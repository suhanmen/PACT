python
def fib4(n: int):
    """
    The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    This function efficiently computes the n-th element of the fib4 number sequence without using recursion.

    Args:
        n (int): the n-th element to compute

    Returns:
        int: the n-th element of the fib4 number sequence
    """
    if n == 0:
        return 0
    if n == 1 or n == 3:
        return 0
    if n == 2:
        return 2

    # Initialize the list with the first 4 elements of the sequence
    fib_seq = [0, 0, 2, 0]

    # Calculate the sequence for all n > 3
    for i in range(4, n + 1):
        fib_i = sum(fib_seq)
        fib_seq.pop(0)
        fib_seq.append(fib_i)

    return fib_seq[-1]
