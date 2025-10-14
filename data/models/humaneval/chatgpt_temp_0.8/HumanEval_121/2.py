def solution(lst):
    """
    Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    """
    # initialize a variable to store the sum of odd elements
    odd_sum = 0
    # loop through the list starting at the second element with a step of 2
    for i in range(1, len(lst), 2):
        # check if the element is odd and add it to the sum
        if lst[i] % 2 != 0:
            odd_sum += lst[i]
    # return the sum of odd elements
    return odd_sum
