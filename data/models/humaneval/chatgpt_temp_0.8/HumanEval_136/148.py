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

    negative_integers = [i for i in lst if i < 0]
    positive_integers = [i for i in lst if i > 0]

    if not negative_integers:
        max_negative = None
    else:
        max_negative = max(negative_integers)

    if not positive_integers:
        min_positive = None
    else:
        min_positive = min(positive_integers)

    return (max_negative, min_positive)
