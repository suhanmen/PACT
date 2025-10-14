def choose_num(x, y):
    # Check if x is an even number. If not, add 1 to make it even.
    if x % 2 == 1:
        x += 1

    # Loop through the range from x to y (inclusive) with a step size of 2
    # to only consider even numbers.
    for num in range(x, y+1, 2):
        # If a number is even, return it as the biggest even number in the range.
        if num % 2 == 0:
            return num

    # If there was no even number in the range, return -1.
    return -1
