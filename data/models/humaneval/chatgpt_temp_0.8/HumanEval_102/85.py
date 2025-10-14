def choose_num(x, y):
    # Check if x is even, if not, add 1 to make it even
    if x % 2 != 0:
        x += 1

    # Starting from x, check each even number in the range [x, y]
    for i in range(x, y + 1, 2):
        # If i is even and in the range [x, y], return it as the biggest even number
        if i % 2 == 0 and i <= y:
            return i
    
    # If there are no even numbers in the range [x, y], return -1
    return -1
