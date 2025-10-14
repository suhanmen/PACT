def tri(n):
    # Initialize the first three numbers of the sequence
    tribonacci = [0, 0, 3]
    
    # Find the remaining n-2 numbers in the sequence
    for i in range(3, n+3):
        if i % 2 == 0:
            tribonacci.append(1 + i / 2)
        else:
            tribonacci.append(tribonacci[i-1] + tribonacci[i-2] + tribonacci[i+1])
    
    # Return the list of n+1 numbers in the sequence
    return tribonacci[:n+1]
