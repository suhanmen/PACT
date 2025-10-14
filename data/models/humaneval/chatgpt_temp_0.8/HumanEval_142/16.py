def sum_squares(lst):
    """
    This function takes a list of integers. For all entries in the list, the function squares the integer entry if its index is a 
    multiple of 3 and cubes the integer entry if its index is a multiple of 4 and not a multiple of 3. Entries in the list whose 
    indexes are not a multiple of 3 or 4 are unchanged. The function returns the sum of all entries. 
    
    Examples:
    For lst = [1,2,3], the output should be 6.
    For lst = [], the output should be 0.
    For lst = [-1,-5,2,-1,-5], the output should be -126.
    """
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num ** 2
        elif i % 4 == 0:
            total += num ** 3
        else:
            total += num
    return total
