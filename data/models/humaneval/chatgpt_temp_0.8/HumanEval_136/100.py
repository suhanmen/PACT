def largest_smallest_integers(lst):
    pos_ints = []
    neg_ints = []
    for num in lst:
        if num > 0:
            pos_ints.append(num)
        elif num < 0:
            neg_ints.append(num)
    if len(pos_ints) == 0:
        b = None
    else:
        b = min(pos_ints)
    if len(neg_ints) == 0:
        a = None
    else:
        a = max(neg_ints)
    return (a, b)
