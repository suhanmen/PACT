def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    
    if len(neg_ints) == 0:
        largest_neg = None
    else:
        largest_neg = max(neg_ints)
        
    if len(pos_ints) == 0:
        smallest_pos = None
    else:
        smallest_pos = min(pos_ints)
        
    return (largest_neg, smallest_pos)
