def largest_smallest_integers(lst):
    pos = [num for num in lst if num > 0]
    neg = [num for num in lst if num < 0]
    if pos:
        smallest_pos = min(pos)
    else:
        smallest_pos = None
    if neg:
        largest_neg = max(neg)
    else:
        largest_neg = None
    return (largest_neg, smallest_pos)
