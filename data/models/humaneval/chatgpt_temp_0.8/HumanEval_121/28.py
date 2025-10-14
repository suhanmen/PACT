def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    # create a variable to hold the sum
    sum = 0

    # loop through the list with a step of 2 to access only even positions
    for i in range(0, len(lst), 2):
        # check if the element is odd
        if lst[i] % 2 != 0:
            # add the odd element to the sum
            sum += lst[i]

    # return the sum
    return sum
