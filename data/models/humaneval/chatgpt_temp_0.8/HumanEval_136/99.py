def largest_smallest_integers(lst):
    neg_integers = []
    pos_integers = []
    for num in lst:
        if num < 0:
            neg_integers.append(num)
        elif num > 0:
            pos_integers.append(num)
    if len(neg_integers) == 0:
        a = None
    else:
        a = max(neg_integers)
    if len(pos_integers) == 0:
        b = None
    else:
        b = min(pos_integers)
    return (a, b)
