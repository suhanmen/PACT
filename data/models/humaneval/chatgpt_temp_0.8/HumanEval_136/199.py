def largest_smallest_integers(lst):
    neg_integers = [x for x in lst if x < 0]
    pos_integers = [x for x in lst if x > 0]
    
    if not neg_integers:
        largest_neg = None
    else:
        largest_neg = max(neg_integers)
    
    if not pos_integers:
        smallest_pos = None
    else:
        smallest_pos = min(pos_integers)
    
    return (largest_neg, smallest_pos)
