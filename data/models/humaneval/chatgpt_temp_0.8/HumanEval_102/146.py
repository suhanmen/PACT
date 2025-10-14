def choose_num(x, y):
    biggest_even = -1 # initialize to -1 in case there is no even number in the range
    for num in range(x, y+1):
        if num % 2 == 0 and num > biggest_even:
            biggest_even = num
    return biggest_even
