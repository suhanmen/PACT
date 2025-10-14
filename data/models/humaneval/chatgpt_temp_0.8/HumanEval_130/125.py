def tri(n):
    # Initialize the list with the first three numbers of the sequence
    seq = [3, 0, 0]
    
    # Loop through the remaining numbers and compute the values based on the recurrence relation
    for i in range(1, n + 1):
        if i % 2 == 0:
            seq.append(1 + i // 2)
        else:
            seq.append(seq[i - 1] + seq[i - 2] + seq[i + 1])
    
    # Return the list of n + 1 numbers in the sequence
    return seq[:n + 1]
