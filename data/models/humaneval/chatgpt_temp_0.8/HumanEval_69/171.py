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
    max_num = -1  # initialize the maximum number to -1
    for num in set(lst):  # loop through the unique numbers in the list
        if num > 0 and lst.count(num) >= num:  # if the number meets the criteria
            if num > max_num:  # and if it's greater than the current max_num
                max_num = num  # set it as the new max_num
    return max_num  # return the max_num, or -1 if no such number exists
