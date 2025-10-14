def largest_smallest_integers(lst):
    pos = [n for n in lst if n > 0]
    neg = [n for n in lst if n < 0]
    if not pos:
        b = None
    else:
        b = min(pos)
    if not neg:
        a = None
    else:
        a = max(neg)
    return (a, b)
