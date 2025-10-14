def largest_smallest_integers(lst):
    neg_integers = [x for x in lst if x < 0]
    pos_integers = [x for x in lst if x > 0]
    
    max_neg = None
    min_pos = None
    
    if neg_integers:
        max_neg = max(neg_integers)
    if pos_integers:
        min_pos = min(pos_integers)
    
    return (max_neg, min_pos)
