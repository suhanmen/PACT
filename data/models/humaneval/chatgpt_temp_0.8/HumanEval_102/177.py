def choose_num(x, y):
    # If x is greater than y, return -1
    if x > y:
        return -1
    
    # Loop through the range [y, x] backwards
    for i in range(y, x-1, -1):
        # If i is even, return i
        if i % 2 == 0:
            return i
    
    # If no even number was found, return -1
    return -1
