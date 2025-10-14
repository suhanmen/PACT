def largest_smallest_integers(lst):
    neg_lst = [x for x in lst if x < 0]
    pos_lst = [x for x in lst if x > 0]
    a = max(neg_lst) if len(neg_lst) > 0 else None
    b = min(pos_lst) if len(pos_lst) > 0 else None
    return (a, b)
