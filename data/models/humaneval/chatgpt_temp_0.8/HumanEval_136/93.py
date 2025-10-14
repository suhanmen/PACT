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

    positive_ints = []
    negative_ints = []
    
    for num in lst:
        if num > 0:
            positive_ints.append(num)
        elif num < 0:
            negative_ints.append(num)
    
    if not positive_ints:
        smallest_positive = None
    else:
        smallest_positive = min(positive_ints)
        
    if not negative_ints:
        largest_negative = None
    else:
        largest_negative = max(negative_ints)
        
    return (largest_negative, smallest_positive)
