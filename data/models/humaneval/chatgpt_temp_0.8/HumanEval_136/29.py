def largest_smallest_integers(lst):
    pos_ints = []
    neg_ints = []
    for num in lst:
        if num > 0:
            pos_ints.append(num)
        elif num < 0:
            neg_ints.append(num)
    pos_ints.sort()
    neg_ints.sort(reverse=True)
    largest_neg = neg_ints[0] if neg_ints else None
    smallest_pos = pos_ints[0] if pos_ints else None
    return (largest_neg, smallest_pos)
