def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    
    max_neg = None if not neg_ints else max(neg_ints)
    min_pos = None if not pos_ints else min(pos_ints)
    
    return (max_neg, min_pos)
