def largest_smallest_integers(lst):
    pos_ints = [x for x in lst if x > 0]
    neg_ints = [x for x in lst if x < 0]
    if pos_ints:
        smallest = min(pos_ints)
    else:
        smallest = None
    if neg_ints:
        largest = max(neg_ints)
    else:
        largest = None
    return (largest, smallest)
