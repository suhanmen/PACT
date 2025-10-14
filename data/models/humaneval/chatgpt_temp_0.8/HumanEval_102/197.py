def choose_num(x, y):
    # check if x or y is odd, if so, increment x until it is even
    while x % 2 != 0 and x <= y:
        x += 1
    # check if there are any even numbers in the range
    if x > y:
        return -1
    # iterate through the range and keep track of the biggest even number
    biggest_even = x
    for i in range(x+2, y+1, 2):
        if i % 2 == 0 and i > biggest_even:
            biggest_even = i
    return biggest_even
