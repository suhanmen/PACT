def largest_smallest_integers(lst):
    pos_ints = [i for i in lst if i > 0]
    neg_ints = [i for i in lst if i < 0]
    
    if len(pos_ints) == 0:
        b = None
    else:
        b = min(pos_ints)
    
    if len(neg_ints) == 0:
        a = None
    else:
        a = max(neg_ints)
    
    return (a, b)
