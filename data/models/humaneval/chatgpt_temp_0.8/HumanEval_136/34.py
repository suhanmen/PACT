def largest_smallest_integers(lst):
    neg_lst = [i for i in lst if i < 0]
    pos_lst = [i for i in lst if i > 0]
    
    if neg_lst:
        max_neg = max(neg_lst)
    else:
        max_neg = None
    
    if pos_lst:
        min_pos = min(pos_lst)
    else:
        min_pos = None
    
    return (max_neg, min_pos)
