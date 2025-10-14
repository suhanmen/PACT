def choose_num(x, y):
    # Check if x and y are positive integers
    if x <= 0 or y <= 0 or x > y:
        return -1
    
    # Check if there is an even number in the range [x, y]
    for num in range(y, x-1, -1):
        if num % 2 == 0:
            return num
    
    # If no even number is found, return -1
    return -1
