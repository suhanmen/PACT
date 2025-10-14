def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    a = None if len(neg_ints) == 0 else max(neg_ints)
    b = None if len(pos_ints) == 0 else min(pos_ints)
    return (a, b)
