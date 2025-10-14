def choose_num(x, y):
    # Check if x is greater than y or if x is odd
    if x > y or x % 2 != 0:
        return -1
    
    # Find the biggest even integer number in the range [x, y]
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            return i
    
    # If no even integer number is found in the range, return -1
    return -1
