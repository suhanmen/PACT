def choose_num(x, y):
    max_even = -1  # initialize to -1 in case there are no even numbers
    for i in range(x, y+1):
        if i % 2 == 0 and i > max_even:
            max_even = i
    return max_even
