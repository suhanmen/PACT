def largest_smallest_integers(lst):
    neg_lst = [i for i in lst if i < 0]
    pos_lst = [i for i in lst if i > 0]
    if not neg_lst:
        largest_neg = None
    else:
        largest_neg = max(neg_lst)
    if not pos_lst:
        smallest_pos = None
    else:
        smallest_pos = min(pos_lst)
    return (largest_neg, smallest_pos)
