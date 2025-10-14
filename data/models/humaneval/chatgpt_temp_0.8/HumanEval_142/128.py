def sum_squares(lst):
    # Initialize the sum to zero
    total = 0
    
    # Loop through the list
    for i in range(len(lst)):
        # Check if the index is a multiple of 3
        if i % 3 == 0:
            # Square the entry
            total += lst[i]**2
        # Check if the index is a multiple of 4 and not a multiple of 3
        elif i % 4 == 0 and i % 3 != 0:
            # Cube the entry
            total += lst[i]**3
        # Otherwise, do not change the entry
        else:
            total += lst[i]
    
    # Return the total sum
    return total
