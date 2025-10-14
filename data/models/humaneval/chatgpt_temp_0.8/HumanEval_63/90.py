# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize the sequence with the first three elements
        fib = [0, 0, 1]
        # Compute the sequence up to the n-th element
        for i in range(3, n+1):
            # Compute the i-th element using the recurrence relation
            fib_i = fib[i-1] + fib[i-2] + fib[i-3]
            # Add the i-th element to the sequence
            fib.append(fib_i)
        # Return the n-th element
        return fib[n]
