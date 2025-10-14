def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    if neg_ints:
        max_neg_int = max(neg_ints)
    else:
        max_neg_int = None
    if pos_ints:
        min_pos_int = min(pos_ints)
    else:
        min_pos_int = None
    return (max_neg_int, min_pos_int)
