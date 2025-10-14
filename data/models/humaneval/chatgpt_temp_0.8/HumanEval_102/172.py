def choose_num(x, y):
    # Check if x and y are positive integers
    if x <= 0 or y <= 0 or x > y:
        return -1
    # Find the biggest even integer in the range [x, y]
    biggest_even = -1
    for i in range(x, y+1):
        if i % 2 == 0 and i > biggest_even:
            biggest_even = i
    return biggest_even
