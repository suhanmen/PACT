def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions. """
    
    return sum([num for index, num in enumerate(lst) if index % 2 == 0 and num % 2 != 0])
    
