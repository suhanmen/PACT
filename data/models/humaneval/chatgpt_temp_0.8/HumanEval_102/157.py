def choose_num(x, y):
    largest_even_num = -1
    for i in range(x, y+1):
        if i % 2 == 0 and i > largest_even_num:
            largest_even_num = i
    return largest_even_num
