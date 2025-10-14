def choose_num(x, y):
    biggest_even = -1
    for n in range(x, y+1):
        if n % 2 == 0 and n > biggest_even:
            biggest_even = n
    return biggest_even
