def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    if neg_ints:
        a = max(neg_ints)
    else:
        a = None
    if pos_ints:
        b = min(pos_ints)
    else:
        b = None
    return (a, b)
