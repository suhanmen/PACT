def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    
    max_neg = None
    if neg_ints:
        max_neg = max(neg_ints)
        
    min_pos = None
    if pos_ints:
        min_pos = min(pos_ints)
        
    return (max_neg, min_pos)
