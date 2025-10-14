def choose_num(x, y):
    # Check if the input values are valid
    if x > y or x < 0 or y < 0:
        return -1
    
    # Iterate through the range [x, y] backwards and return the first even number
    for num in range(y, x-1, -1):
        if num % 2 == 0:
            return num
    
    # If no even number was found, return -1
    return -1
