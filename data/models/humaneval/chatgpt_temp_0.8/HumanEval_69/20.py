def search(lst):
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    """
    for num in sorted(set(lst), reverse=True): # iterate through unique sorted integers in reverse order
        if lst.count(num) >= num: # if frequency of integer is greater than or equal to the integer itself
            return num # return the integer
    return -1 # if no such integer exists, return -1
