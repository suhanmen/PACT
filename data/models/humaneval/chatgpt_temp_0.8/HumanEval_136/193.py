def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]
    if neg_integers:
        largest_negative = max(neg_integers)
    else:
        largest_negative = None
    if pos_integers:
        smallest_positive = min(pos_integers)
    else:
        smallest_positive = None
    return (largest_negative, smallest_positive)
