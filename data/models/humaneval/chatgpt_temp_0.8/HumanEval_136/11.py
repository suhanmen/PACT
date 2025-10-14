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
    neg_lst = [x for x in lst if x < 0]
    pos_lst = [x for x in lst if x > 0]
    neg_max = None if len(neg_lst) == 0 else max(neg_lst)
    pos_min = None if len(pos_lst) == 0 else min(pos_lst)
    return (neg_max, pos_min)
