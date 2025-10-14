def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions."""
    
    # Initialize sum to zero
    total = 0
    
    # Loop through list and check if element is odd and in even position
    for i in range(1, len(lst), 2):
        if lst[i] % 2 != 0:
            total += lst[i]
            
    return total
