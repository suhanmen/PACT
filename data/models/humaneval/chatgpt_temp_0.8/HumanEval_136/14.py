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
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    
    if not neg_ints:
        max_neg = None
    else:
        max_neg = max(neg_ints)
    
    if not pos_ints:
        min_pos = None
    else:
        min_pos = min(pos_ints)
    
    return (max_neg, min_pos)
