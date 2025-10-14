def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Initialize a variable to hold the sum of odd elements in even positions
    odd_sum = 0
    
    # Loop through the list using a for loop
    for i in range(1, len(lst), 2):
        # Check if the current element is odd and in even position
        if lst[i] % 2 != 0:
            # Add the current element to the odd_sum variable
            odd_sum += lst[i]
    
    # Return the odd_sum variable
    return odd_sum
