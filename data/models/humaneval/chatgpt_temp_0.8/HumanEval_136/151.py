def largest_smallest_integers(lst):
    neg_ints = [x for x in lst if x < 0]
    pos_ints = [x for x in lst if x > 0]
    if not neg_ints:
        max_neg = None
    else:
        max_neg = max(neg_ints)
    if not pos_ints:
        min_pos = None
    else:
        min_pos = min(pos_ints)
    return (max_neg, min_pos)
