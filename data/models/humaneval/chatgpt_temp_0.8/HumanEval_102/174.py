def choose_num(x, y):
    largest_even_num = -1

    for num in range(x, y + 1):
        if num % 2 == 0 and num > largest_even_num:
            largest_even_num = num

    return largest_even_num
