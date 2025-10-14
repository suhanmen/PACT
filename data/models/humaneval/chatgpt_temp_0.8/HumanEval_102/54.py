def choose_num(x, y):
    max_even = -1  # default value in case there's no even number in range
    for num in range(x, y+1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even
