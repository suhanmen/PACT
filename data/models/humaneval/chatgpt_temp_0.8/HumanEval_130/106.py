def tri(n):
    """
    Returns a list of the first n + 1 numbers of the Tribonacci sequence.
    """
    # Initialize the list with the first three numbers
    sequence = [0, 0, 1]
    
    # Loop from 3 to n
    for i in range(3, n + 1):
        # Check if i is even
        if i % 2 == 0:
            # Calculate tribonacci number for even i
            tribonacci = 1 + i // 2
        else:
            # Calculate tribonacci number for odd i
            tribonacci = sequence[i-1] + sequence[i-2] + sequence[i+1]
        # Add the tribonacci number to the sequence
        sequence.append(tribonacci)
    
    return sequence[:n+1]  # Return the first n + 1 elements of the sequence
