def choose_num(x, y):
    biggest_even_num = -1
    for i in range(x, y+1):
        if i % 2 == 0 and i > biggest_even_num:
            biggest_even_num = i
    return biggest_even_num
