def largest_smallest_integers(lst):
    neg_lst = [i for i in lst if i < 0]
    pos_lst = [i for i in lst if i > 0]
    if not neg_lst:
        largest = None
    else:
        largest = max(neg_lst)
    if not pos_lst:
        smallest = None
    else:
        smallest = min(pos_lst)
    return (largest, smallest)
