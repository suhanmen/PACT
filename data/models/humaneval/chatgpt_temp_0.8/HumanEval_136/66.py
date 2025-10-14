def largest_smallest_integers(lst):
    max_neg = None
    min_pos = None
    for n in lst:
        if n < 0 and (max_neg is None or n > max_neg):
            max_neg = n
        elif n > 0 and (min_pos is None or n < min_pos):
            min_pos = n
    return (max_neg, min_pos)
