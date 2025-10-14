def largest_smallest_integers(lst):
    pos_integers = [i for i in lst if i > 0]
    neg_integers = [i for i in lst if i < 0]
    if len(pos_integers) == 0:
        smallest_pos = None
    else:
        smallest_pos = min(pos_integers)
    if len(neg_integers) == 0:
        largest_neg = None
    else:
        largest_neg = max(neg_integers)
    return (largest_neg, smallest_pos)
