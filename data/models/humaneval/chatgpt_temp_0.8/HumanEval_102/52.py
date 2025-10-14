def choose_num(x, y):
    # Check if x and y are positive integers
    if x <= 0 or y <= 0 or x != int(x) or y != int(y):
        return -1
    
    # Swap x and y if x is greater than y
    if x > y:
        x, y = y, x
    
    # Iterate through the range [x, y] backwards and return the first even number
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i
    
    # If no even number was found, return -1
    return -1
