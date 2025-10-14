def largest_smallest_integers(lst):
    pos_integers = [i for i in lst if i > 0]
    neg_integers = [i for i in lst if i < 0]
    if not pos_integers:
        b = None
    else:
        b = min(pos_integers)
    if not neg_integers:
        a = None
    else:
        a = max(neg_integers)
    return (a, b)
