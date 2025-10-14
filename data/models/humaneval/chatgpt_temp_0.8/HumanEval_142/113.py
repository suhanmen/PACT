def sum_squares(lst):
    """
    This function takes a list of integers. For all entries in the list, the function squares the integer entry if its index is a 
    multiple of 3 and cubes the integer entry if its index is a multiple of 4 and not a multiple of 3. 
    Entries whose indexes are not a multiple of 3 or 4 are not changed.
    The function returns the sum of all entries. 
    """
    result = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            result += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += lst[i] ** 3
        else:
            result += lst[i]
    return result
