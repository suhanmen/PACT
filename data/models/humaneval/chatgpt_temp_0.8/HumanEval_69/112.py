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
    # Initialize a dictionary to store the frequencies of each integer
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Initialize a variable to keep track of the highest integer meeting the criteria
    highest_int = 0
    
    # Iterate over the dictionary to find the highest integer meeting the criteria
    for num in freq_dict:
        if num > highest_int and freq_dict[num] >= num:
            highest_int = num
    
    # Return the highest integer meeting the criteria, or -1 if no such integer exists
    if highest_int > 0:
        return highest_int
    else:
        return -1
