# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    # Define the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0
    # Compute the n-th element of the sequence
    for i in range(4, n+1):
        d, c, b, a = c + b + a + d, d, c, b
    # Return the result
    return d if n > 2 else [0, 0, 2][n]
