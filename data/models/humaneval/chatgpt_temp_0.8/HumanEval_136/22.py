def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    if neg_ints:
        largest_neg = max(neg_ints)
    else:
        largest_neg = None
    if pos_ints:
        smallest_pos = min(pos_ints)
    else:
        smallest_pos = None
    return (largest_neg, smallest_pos)
