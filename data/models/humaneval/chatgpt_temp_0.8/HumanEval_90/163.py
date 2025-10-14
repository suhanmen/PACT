def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    smallest = float('inf')
    next_smallest = float('inf')
    
    for num in lst:
        if num < smallest:
            next_smallest = smallest
            smallest = num
        elif num < next_smallest and num != smallest:
            next_smallest = num
    
    if next_smallest == float('inf'):
        return None
    else:
        return next_smallest
