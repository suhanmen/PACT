def largest_smallest_integers(lst):
    pos_int = None
    neg_int = None
    for num in lst:
        if num > 0 and (pos_int is None or num < pos_int):
            pos_int = num
        elif num < 0 and (neg_int is None or num > neg_int):
            neg_int = num
    return (neg_int, pos_int)
