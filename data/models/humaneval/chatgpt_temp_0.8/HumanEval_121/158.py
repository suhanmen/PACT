def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # initialize a sum variable to store the sum of odd elements at even positions
    sum_odd = 0
    
    # iterate over the list and check for odd elements at even positions
    for i in range(1, len(lst), 2):
        if lst[i] % 2 != 0:
            sum_odd += lst[i]
    
    return sum_odd
