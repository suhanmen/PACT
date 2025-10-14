def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.

    Examples:
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """

    # Initialize sum to be 0
    sum = 0

    # Loop through the list and check if the element is odd and in even position
    for i in range(0, len(lst), 2):
        if lst[i] % 2 == 1:
            sum += lst[i]

    return sum
