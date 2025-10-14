def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    if not neg_ints:
        neg_ints = None
    else:
        neg_ints = max(neg_ints)
    if not pos_ints:
        pos_ints = None
    else:
        pos_ints = min(pos_ints)
    return (neg_ints, pos_ints)
