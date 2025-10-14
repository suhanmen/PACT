def sum_squares(lst):
    """
    This function takes a list of integers. For all entries in the list, the function squares the integer entry if its index is a 
    multiple of 3 and cubes the integer entry if its index is a multiple of 4 but not a multiple of 3. Entries whose indexes are not 
    a multiple of 3 or 4 are not changed. The function then returns the sum of all entries. 
    
    Examples:
    sum_squares([1, 2, 3]) returns 6
    sum_squares([]) returns 0
    sum_squares([-1, -5, 2, -1, -5]) returns -126
    """
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num ** 2
        elif i % 4 == 0 and i % 3 !=0:
            total += num ** 3
        else:
            total += num
    return total
