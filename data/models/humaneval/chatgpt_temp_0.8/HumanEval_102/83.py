def choose_num(x, y):
    # If x is greater than y or x and y are both odd, no even integer in the range exists
    if x > y or (x % 2 != 0 and y % 2 != 0):
        return -1
    
    # Starting from the highest even integer in the range, return the first even integer found
    for i in range(y, x-1, -1):
        if i % 2 == 0:
            return i
