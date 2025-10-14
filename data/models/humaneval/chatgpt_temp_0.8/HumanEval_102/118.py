def choose_num(x, y):
    biggest = -1
    for i in range(x, y+1):
        if i % 2 == 0 and i > biggest:
            biggest = i
    return biggest
