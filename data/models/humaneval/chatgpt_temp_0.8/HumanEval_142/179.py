def sum_squares(lst):
    """
    This function takes a list of integers. For all entries in the list, the function squares the integer entry if its index
    is a multiple of 3 and cubes the integer entry if its index is a multiple of 4 and not a multiple of 3. The function 
    will not change the entries in the list whose indexes are not a multiple of 3 or 4. The function then returns the 
    sum of all entries.
    """
    result = 0
    for index, value in enumerate(lst):
        if index % 3 == 0:
            result += value ** 2
        elif index % 4 == 0 and index % 3 != 0:
            result += value ** 3
        else:
            result += value
    return result
