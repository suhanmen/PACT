def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    a = None
    b = None
    if len(neg_ints) > 0:
        a = max(neg_ints)
    if len(pos_ints) > 0:
        b = min(pos_ints)
    return (a, b)
