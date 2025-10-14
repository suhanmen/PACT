def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    
    # Initialize the sequence with the first four numbers
    seq = [0, 0, 2, 0]
    
    # Compute the i-th element of the sequence by summing the previous four elements
    for i in range(3, n+1):
        seq[i % 4] = seq[(i-1) % 4] + seq[(i-2) % 4] + seq[(i-3) % 4] + seq[(i-4) % 4]
    
    return seq[n % 4]
