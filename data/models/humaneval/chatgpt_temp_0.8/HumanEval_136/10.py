def largest_smallest_integers(lst):
    negs = [n for n in lst if n < 0]
    pos = [n for n in lst if n > 0]
    if len(negs) == 0:
        a = None
    else:
        a = max(negs)
    if len(pos) == 0:
        b = None
    else:
        b = min(pos)
    return (a, b)
