def largest_smallest_integers(lst):
    neg_integers = [x for x in lst if x < 0]
    pos_integers = [x for x in lst if x > 0]
    neg_max = max(neg_integers) if neg_integers else None
    pos_min = min(pos_integers) if pos_integers else None
    return (neg_max, pos_min)
