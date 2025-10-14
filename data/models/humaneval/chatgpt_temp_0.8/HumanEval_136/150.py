def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    if not neg_ints:
        largest_neg_int = None
    else:
        largest_neg_int = max(neg_ints)
    if not pos_ints:
        smallest_pos_int = None
    else:
        smallest_pos_int = min(pos_ints)
    return (largest_neg_int, smallest_pos_int)
