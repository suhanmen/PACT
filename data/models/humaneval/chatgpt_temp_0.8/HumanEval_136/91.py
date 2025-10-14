def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]
    
    if neg_integers:
        max_neg = max(neg_integers)
    else:
        max_neg = None
        
    if pos_integers:
        min_pos = min(pos_integers)
    else:
        min_pos = None
        
    return (max_neg, min_pos)
