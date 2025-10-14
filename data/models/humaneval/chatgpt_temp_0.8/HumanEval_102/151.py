def choose_num(x, y):
    max_num = -1
    for i in range(x, y+1):
        if i % 2 == 0 and i > max_num:
            max_num = i
    return max_num
