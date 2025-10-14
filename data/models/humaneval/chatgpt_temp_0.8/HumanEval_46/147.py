def fib4(n: int):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the list with the first four elements of the sequence
    seq = [0, 0, 2, 0]
    
    # Loop through the remaining elements and compute each one
    for i in range(4, n+1):
        seq[i % 4] = sum(seq) # Compute the sum of the previous four elements
    return seq[n % 4]
