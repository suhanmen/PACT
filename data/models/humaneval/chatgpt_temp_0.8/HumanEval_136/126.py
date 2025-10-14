def largest_smallest_integers(lst):
    pos_ints = [i for i in lst if i > 0]
    neg_ints = [i for i in lst if i < 0]
    max_neg = min(neg_ints) if len(neg_ints) > 0 else None
    min_pos = max(pos_ints) if len(pos_ints) > 0 else None
    return (max_neg, min_pos)
