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
    negatives = [n for n in lst if n < 0]
    positives = [n for n in lst if n > 0]
    
    if not negatives:
        largest_neg = None
    else:
        largest_neg = max(negatives)
    
    if not positives:
        smallest_pos = None
    else:
        smallest_pos = min(positives)
    
    return (largest_neg, smallest_pos)
