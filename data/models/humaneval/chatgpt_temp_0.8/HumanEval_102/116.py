def choose_num(x, y):
    # Check if x or y is even and within the range
    if x % 2 == 0 and x <= y:
        biggest_even = x
    elif y % 2 == 0 and y >= x:
        biggest_even = y
    else:
        return -1

    # Iterate through the range and find the biggest even number
    for i in range(biggest_even, y+1, 2):
        if i % 2 == 0:
            biggest_even = i
    
    return biggest_even
