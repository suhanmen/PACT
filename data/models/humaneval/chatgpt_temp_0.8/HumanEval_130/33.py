def tri(n):
    # Initialize the first three elements of the Tribonacci sequence
    seq = [0, 0, 3]
    
    # Loop through the remaining elements of the sequence
    for i in range(3, n+1):
        # If i is even, use the formula tri(n) = 1 + n/2
        if i % 2 == 0:
            seq.append(1 + i/2)
        # If i is odd, use the formula tri(n) = tri(n-1) + tri(n-2) + tri(n+1)
        else:
            seq.append(seq[i-1] + seq[i-2] + seq[i+1])
    
    # Return the first n+1 elements of the sequence
    return seq[:n+1]
