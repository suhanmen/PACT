def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    # Initialize a variable to store the sum
    sum = 0
    
    # Iterate over the list using a for loop and range function
    for i in range(1, len(lst), 2):
        
        # Check if the element is odd and is in an even position
        if lst[i] % 2 == 1:
            
            # If yes, add it to the sum
            sum += lst[i]
    
    # Return the sum
    return sum
