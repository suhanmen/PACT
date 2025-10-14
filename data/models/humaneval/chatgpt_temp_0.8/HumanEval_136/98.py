def largest_smallest_integers(lst):
    neg_ints = [num for num in lst if num < 0]
    pos_ints = [num for num in lst if num > 0]
    
    if not neg_ints:
        largest_neg = None
    else:
        largest_neg = max(neg_ints)
    
    if not pos_ints:
        smallest_pos = None
    else:
        smallest_pos = min(pos_ints)
    
    return (largest_neg, smallest_pos)
