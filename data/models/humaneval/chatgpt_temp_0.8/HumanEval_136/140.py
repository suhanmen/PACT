def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]

    a = max(neg_ints) if len(neg_ints) > 0 else None
    b = min(pos_ints) if len(pos_ints) > 0 else None

    return (a, b)
