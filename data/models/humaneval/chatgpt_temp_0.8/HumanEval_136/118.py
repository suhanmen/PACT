def largest_smallest_integers(lst):
    pos_integers = [n for n in lst if n > 0]
    neg_integers = [n for n in lst if n < 0]
    if len(pos_integers) == 0:
        b = None
    else:
        b = min(pos_integers)
    if len(neg_integers) == 0:
        a = None
    else:
        a = max(neg_integers)
    return (a, b)
