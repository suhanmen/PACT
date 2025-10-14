def fib4(n: int):
    # Initialize first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # Handle base cases
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    
    # Compute subsequent elements of the sequence using a loop
    for i in range(3, n+1):
        # Compute the next element of the sequence
        next_element = a + b + c + d
        
        # Update variables for next iteration
        a = b
        b = c
        c = d
        d = next_element
    
    # Return the n-th element of the sequence
    return next_element
