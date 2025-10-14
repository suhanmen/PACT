def is_sorted(lst):
    # Check if there are more than 1 duplicate of the same number
    for num in lst:
        if lst.count(num) > 1:
            return False
    
    # Check if list is sorted in ascending order
    prev_num = lst[0]
    for num in lst[1:]:
        if num < prev_num:
            return False
        prev_num = num
    
    return True
