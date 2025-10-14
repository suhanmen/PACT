def next_smallest(lst):
    if len(lst) < 2:
        return None
    smallest = min(lst)
    second_smallest = float('inf')
    for num in lst:
        if num > smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest
