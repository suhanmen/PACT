def largest_smallest_integers(lst):
    neg_integers = [num for num in lst if num < 0]
    pos_integers = [num for num in lst if num > 0]
    if neg_integers:
        largest_neg = max(neg_integers)
    else:
        largest_neg = None
    if pos_integers:
        smallest_pos = min(pos_integers)
    else:
        smallest_pos = None
    return (largest_neg, smallest_pos)
