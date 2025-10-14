def fib4(n: int):
    # Initialize the first four elements of the sequence
    seq = [0, 0, 2, 0]
    
    # Compute the next elements of the sequence iteratively
    for i in range(4, n+1):
        # Compute the sum of the previous four elements
        sum_prev = seq[i-1] + seq[i-2] + seq[i-3] + seq[i-4]
        seq.append(sum_prev)
    
    # Return the n-th element of the sequence
    return seq[n]
