def choose_num(x, y):
    largest_even = -1
    for i in range(x, y+1):
        if i % 2 == 0 and i > largest_even:
            largest_even = i
    return largest_even
