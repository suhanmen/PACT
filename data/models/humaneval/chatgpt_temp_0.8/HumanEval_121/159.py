def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    sum_odd = 0
    for i in range(0, len(lst), 2):  # iterate through even positions
        if lst[i] % 2 != 0:  # check if the element at even position is odd
            sum_odd += lst[i]  # add the odd element to sum_odd
    return sum_odd
