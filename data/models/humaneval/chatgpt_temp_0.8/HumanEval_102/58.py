def choose_num(x, y):
    # If x is greater than y, there's no valid range to search
    if x > y:
        return -1
    
    # Iterate through the range [x,y] and check if each integer is even
    # If it is, store it as the current biggest even integer found
    biggest_even = -1
    for i in range(x, y+1):
        if i % 2 == 0 and i > biggest_even:
            biggest_even = i
    
    # If no even integer was found, return -1
    if biggest_even == -1:
        return -1
    
    # Otherwise, return the biggest even integer found
    return biggest_even
