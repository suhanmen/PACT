def largest_smallest_integers(lst):
    neg_lst = [num for num in lst if num < 0]
    pos_lst = [num for num in lst if num > 0]
    if neg_lst:
        a = max(neg_lst)
    else:
        a = None
    if pos_lst:
        b = min(pos_lst)
    else:
        b = None
    return (a, b)
