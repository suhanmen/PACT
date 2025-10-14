def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    # initialize sum to 0
    sum = 0
    
    # iterate through list using range to access even positions
    for i in range(0, len(lst), 2):
        # check if element at even position is odd
        if lst[i] % 2 != 0:
            # add odd element to sum
            sum += lst[i]
    
    # return sum of odd elements in even positions
    return sum
