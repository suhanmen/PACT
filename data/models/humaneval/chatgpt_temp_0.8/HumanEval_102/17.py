def choose_num(x, y):
    biggest_even = -1
    for i in range(x, y+1):
        if i % 2 == 0:
            if i > biggest_even:
                biggest_even = i
    return biggest_even
