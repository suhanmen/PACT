def choose_num(x, y):
    max_even = -1  # assume there's no even number in the range initially
    for num in range(x, y+1):  # iterate through the range [x, y] inclusive
        if num % 2 == 0:  # if the number is even
            if num > max_even:  # if the number is greater than the current max_even
                max_even = num  # update the max_even to be the current number
    return max_even
