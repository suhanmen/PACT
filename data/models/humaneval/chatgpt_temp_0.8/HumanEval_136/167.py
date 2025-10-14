def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]
    if not neg_integers:
        max_neg = None
    else:
        max_neg = max(neg_integers)
    if not pos_integers:
        min_pos = None
    else:
        min_pos = min(pos_integers)
    return (max_neg, min_pos)
