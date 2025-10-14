def largest_smallest_integers(lst):
    neg_lst = [i for i in lst if i < 0]
    pos_lst = [i for i in lst if i > 0]
    if not neg_lst:
        a = None
    else:
        a = max(neg_lst)
    if not pos_lst:
        b = None
    else:
        b = min(pos_lst)
    return (a, b)
