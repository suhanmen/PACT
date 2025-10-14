def choose_num(x, y):
    # Check if x and y are positive
    if x <= 0 or y <= 0:
        return -1
    
    # Determine the range of integers to check
    start = x if x % 2 == 0 else x + 1
    end = y if y % 2 == 0 else y - 1
    
    # Check if there are any even numbers in the range
    if start > end:
        return -1
    
    # Find the biggest even number in the range
    max_even = start
    for num in range(start, end+1, 2):
        if num > max_even:
            max_even = num
    
    return max_even
