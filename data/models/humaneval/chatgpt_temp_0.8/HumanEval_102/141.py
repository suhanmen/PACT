def choose_num(x, y):
    # Initialize the max_even to be -1
    max_even = -1
    
    # Iterate through the range [x, y]
    for i in range(x, y+1):
        # Check if i is an even integer
        if i % 2 == 0:
            # Update max_even if i is greater than the current max_even
            if i > max_even:
                max_even = i
    
    # Return max_even
    return max_even
