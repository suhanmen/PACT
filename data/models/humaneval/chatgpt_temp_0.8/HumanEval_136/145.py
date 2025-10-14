def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]
    if neg_integers:
        a = max(neg_integers)
    else:
        a = None
    if pos_integers:
        b = min(pos_integers)
    else:
        b = None
    return (a, b)
