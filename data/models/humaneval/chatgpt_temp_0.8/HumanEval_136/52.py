def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    if not neg_ints:
        largest = None
    else:
        largest = max(neg_ints)
    if not pos_ints:
        smallest = None
    else:
        smallest = min(pos_ints)
    return (largest, smallest)
