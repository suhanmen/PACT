def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Initialize a variable to store the sum of odd elements in even positions
    odd_sum = 0
    
    # Loop through the list, starting at the second element and incrementing by 2
    for i in range(1, len(lst), 2):
        # If the element is odd and in an even position, add it to the sum
        if lst[i] % 2 != 0:
            odd_sum += lst[i]
            
    # Return the sum of odd elements in even positions
    return odd_sum
