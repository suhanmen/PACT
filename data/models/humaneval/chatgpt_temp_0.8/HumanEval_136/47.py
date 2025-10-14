def largest_smallest_integers(lst):
    neg = [i for i in lst if i < 0]
    pos = [i for i in lst if i > 0]
    if len(neg) == 0:
        largest_neg = None
    else:
        largest_neg = max(neg)
    if len(pos) == 0:
        smallest_pos = None
    else:
        smallest_pos = min(pos)
    return (largest_neg, smallest_pos)
