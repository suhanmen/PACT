def choose_num(x, y):
    # If x is odd, move to the next even number
    if x % 2 == 1:
        x += 1
    
    # If y is odd, move to the previous even number
    if y % 2 == 1:
        y -= 1
    
    # If there's no even number in the range, return -1
    if x > y:
        return -1
    
    # Return the largest even number in the range
    return y
