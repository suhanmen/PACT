def largest_smallest_integers(lst):
    neg_lst = [num for num in lst if num < 0]
    pos_lst = [num for num in lst if num > 0]
    if not neg_lst:
        neg_max = None
    else:
        neg_max = max(neg_lst)
    if not pos_lst:
        pos_min = None
    else:
        pos_min = min(pos_lst)
    return (neg_max, pos_min)
