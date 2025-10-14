def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n."""
    
    # Initialize a variable to store the sum
    total = 0
    
    # Loop through numbers from 1 to n and add them to the total
    for i in range(1, n + 1):
        total += i
    
    # Return the total
    return total
