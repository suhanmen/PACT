# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Initialize the sequence with first four values
        fib = [0, 0, 2, 0]
        for i in range(3, n+1):
            # Compute the next value in the sequence
            fib[i % 4] = fib[(i-1) % 4] + fib[(i-2) % 4] + fib[(i-3) % 4] + fib[(i-4) % 4]
        return fib[n % 4]
