def choose_num(x, y):
    # Check if x and y are positive numbers
    if x <= 0 or y <= 0:
        return -1
    
    # Swap x and y if x is greater than y
    if x > y:
        x, y = y, x
        
    # Loop through the range [x, y] and find the biggest even integer
    for num in range(y, x-1, -1):
        if num % 2 == 0:
            return num
        
    # If there's no such number, return -1
    return -1
