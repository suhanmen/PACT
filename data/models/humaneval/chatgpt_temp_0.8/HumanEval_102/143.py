def choose_num(x, y):
    # Initialize max_even to -1
    max_even = -1
    
    # Loop through the range [x, y] inclusive
    for i in range(x, y+1):
        # Check if i is even and greater than the current max_even
        if i % 2 == 0 and i > max_even:
            max_even = i
    
    return max_even
