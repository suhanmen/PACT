def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    # Initialize a variable to store the sum of odd elements in even positions
    sum_odd = 0
    
    # Loop through the even indices of the list
    for i in range(0, len(lst), 2):
        # Check if the element at the current index is odd
        if lst[i] % 2 != 0:
            # If the element is odd, add it to the sum_odd variable
            sum_odd += lst[i]
    
    # Return the sum of odd elements in even positions
    return sum_odd
