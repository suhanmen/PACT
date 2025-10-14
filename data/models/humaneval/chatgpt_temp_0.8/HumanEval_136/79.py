def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    if len(neg_ints) == 0:
        max_neg = None
    else:
        max_neg = max(neg_ints)
    if len(pos_ints) == 0:
        min_pos = None
    else:
        min_pos = min(pos_ints)
    return (max_neg, min_pos)
