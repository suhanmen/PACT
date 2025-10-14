def largest_smallest_integers(lst):
    pos_ints = [num for num in lst if num > 0]
    neg_ints = [num for num in lst if num < 0]
    
    if not pos_ints:
        smallest_pos_int = None
    else:
        smallest_pos_int = min(pos_ints)
        
    if not neg_ints:
        largest_neg_int = None
    else:
        largest_neg_int = max(neg_ints)
        
    return (largest_neg_int, smallest_pos_int)
