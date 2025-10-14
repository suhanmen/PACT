# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0
    # Compute the remaining elements of the sequence iteratively
    for i in range(4, n+1):
        d = a + b + c + d
        a, b, c = b, c, d
    # Return the n-th element of the sequence
    return d if n > 2 else [0, 0, 2][n]
