def choose_num(x, y):
    biggest_even = -1
    for num in range(x, y+1):
        if num % 2 == 0:
            biggest_even = num
    return biggest_even
