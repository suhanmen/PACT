def is_sorted(lst):
    # Check if there are more than 1 duplicates of the same number
    for num in lst:
        if lst.count(num) > 1:
            return False
    
    # Check if list is sorted in ascending order
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True
