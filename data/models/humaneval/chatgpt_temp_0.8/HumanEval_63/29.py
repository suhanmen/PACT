# CANNOT PARSE CODE SNIPPET
python
def fibfib(n: int, cache={0: 0, 1: 0, 2: 1}) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    """
    if n in cache:
        return cache[n]
    else:
        result = fibfib(n-1, cache) + fibfib(n-2, cache) + fibfib(n-3, cache)
        cache[n] = result
        return result
