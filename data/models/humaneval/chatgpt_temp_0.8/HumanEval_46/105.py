# CANNOT PARSE CODE SNIPPET
def fib4(n: int) -> int:
    # Initialize the first four numbers in the sequence
    fib = [0, 0, 2, 0]
    
    if n < 4:
        return fib[n]
    
    # Iterate from 4 to n and update the sequence
    for i in range(4, n+1):
        # Compute the next element in the sequence
        next_fib = fib[1] + fib[2] + fib[3] + fib[0]
        # Shift the values in the sequence to the left by 1
        fib[0], fib[1], fib[2], fib[3] = fib[1], fib[2], fib[3], next_fib
        
    return fib[3]
