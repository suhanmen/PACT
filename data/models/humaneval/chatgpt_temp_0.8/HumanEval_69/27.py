def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    max_val = -1
    freq_dict = {}
    for num in lst:
        if num > 0:
            freq_dict[num] = freq_dict.get(num, 0) + 1
    for key, value in freq_dict.items():
        if key <= value and key > max_val:
            max_val = key
    return max_val
