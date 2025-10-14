def largest_smallest_integers(lst):
    neg_lst = [num for num in lst if num < 0]
    pos_lst = [num for num in lst if num > 0]

    if neg_lst:
        largest_neg = max(neg_lst)
    else:
        largest_neg = None

    if pos_lst:
        smallest_pos = min(pos_lst)
    else:
        smallest_pos = None

    return (largest_neg, smallest_pos)
