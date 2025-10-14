def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]

    if len(neg_integers) == 0:
        largest_neg_int = None
    else:
        largest_neg_int = max(neg_integers)

    if len(pos_integers) == 0:
        smallest_pos_int = None
    else:
        smallest_pos_int = min(pos_integers)

    return (largest_neg_int, smallest_pos_int)
