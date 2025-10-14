# CANNOT PARSE
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
    # Create a dictionary to store the frequency of each integer
    freq_dict = {}
    
    # Iterate through the list and update the frequency dictionary
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Initialize the result variable with -1
    result = -1
    
    # Iterate through the frequency dictionary
    for key, value in freq_dict.items():
        # Check if the frequency is greater than or equal to the integer itself
        if key <= value:
            # Update the result variable with the maximum value
            result = max(result, key)
    
    return result