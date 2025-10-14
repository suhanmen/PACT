def choose_num(x, y):
    # Check if x is greater than y
    if x > y:
        return -1

    # Iterate from y to x (inclusive) and check for even integers
    for i in range(y, x-1, -1):
        if i % 2 == 0:
            return i

    # If no even integer is found, return -1
    return -1
