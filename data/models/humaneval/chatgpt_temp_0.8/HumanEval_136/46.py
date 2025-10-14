def largest_smallest_integers(lst):
    neg_lst = [num for num in lst if num < 0]
    pos_lst = [num for num in lst if num > 0]
    if not neg_lst:
        max_neg = None
    else:
        max_neg = max(neg_lst)
    if not pos_lst:
        min_pos = None
    else:
        min_pos = min(pos_lst)
    return (max_neg, min_pos)
