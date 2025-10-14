def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''

    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]
    
    largest_negative = None
    smallest_positive = None
    
    if len(neg_integers) > 0:
        largest_negative = max(neg_integers)
        
    if len(pos_integers) > 0:
        smallest_positive = min(pos_integers)
        
    return (largest_negative, smallest_positive)
