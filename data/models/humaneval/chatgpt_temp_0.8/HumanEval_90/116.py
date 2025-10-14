def next_smallest(lst):
    if len(lst) < 2:
        return None
    
    smallest = lst[0]
    second_smallest = None
    
    for num in lst[1:]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest or second_smallest is None:
            second_smallest = num
    
    return second_smallest
