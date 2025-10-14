def largest_smallest_integers(lst):
    max_neg = None
    min_pos = None
    for num in lst:
        if num < 0 and (max_neg is None or num > max_neg):
            max_neg = num
        elif num > 0 and (min_pos is None or num < min_pos):
            min_pos = num
    return (max_neg, min_pos)
