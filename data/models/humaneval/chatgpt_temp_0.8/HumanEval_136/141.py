def largest_smallest_integers(lst):
    pos_ints = [x for x in lst if x > 0]
    neg_ints = [x for x in lst if x < 0]
    if pos_ints:
        smallest_pos = min(pos_ints)
    else:
        smallest_pos = None
    if neg_ints:
        largest_neg = max(neg_ints)
    else:
        largest_neg = None
    return (largest_neg, smallest_pos)
