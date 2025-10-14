def largest_smallest_integers(lst):
    neg_lst = [i for i in lst if i < 0]
    pos_lst = [i for i in lst if i > 0]
    if len(neg_lst) == 0:
        a = None
    else:
        a = max(neg_lst)
    if len(pos_lst) == 0:
        b = None
    else:
        b = min(pos_lst)
    return (a, b)
