def largest_smallest_integers(lst):
    pos_ints = [x for x in lst if x > 0]
    neg_ints = [x for x in lst if x < 0]
    max_neg = None if len(neg_ints) == 0 else max(neg_ints)
    min_pos = None if len(pos_ints) == 0 else min(pos_ints)
    return (max_neg, min_pos)
