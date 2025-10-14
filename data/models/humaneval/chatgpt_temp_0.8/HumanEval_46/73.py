def fib4(n: int):
    # Initialize variables to hold the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0
    
    # If n is 0, return 0
    if n == 0:
        return a
    
    # If n is 1, return 0
    if n == 1:
        return b
    
    # If n is 2, return 2
    if n == 2:
        return c
    
    # Calculate the next n-3 elements of the sequence iteratively
    for i in range(3, n+1):
        # Calculate the next element of the sequence based on the previous four elements
        e = a + b + c + d
        # Update the variables to hold the four most recent elements of the sequence
        a = b
        b = c
        c = d
        d = e
    
    # Return the n-th element of the sequence
    return e
