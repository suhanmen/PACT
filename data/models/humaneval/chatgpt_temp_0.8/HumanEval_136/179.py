def largest_smallest_integers(lst):
    neg_ints = [n for n in lst if n < 0]
    pos_ints = [n for n in lst if n > 0]
    
    if len(neg_ints) == 0:
        a = None
    else:
        a = max(neg_ints)
        
    if len(pos_ints) == 0:
        b = None
    else:
        b = min(pos_ints)
        
    return (a, b)
