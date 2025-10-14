def largest_smallest_integers(lst):
    pos_integers = [i for i in lst if i > 0]
    neg_integers = [i for i in lst if i < 0]

    if pos_integers:
        smallest_pos = min(pos_integers)
    else:
        smallest_pos = None

    if neg_integers:
        largest_neg = max(neg_integers)
    else:
        largest_neg = None

    return (largest_neg, smallest_pos)
