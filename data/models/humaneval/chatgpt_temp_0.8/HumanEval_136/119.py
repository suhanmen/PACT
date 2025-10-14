def largest_smallest_integers(lst):
    pos_ints = [n for n in lst if n > 0]
    neg_ints = [n for n in lst if n < 0]
    
    if pos_ints:
        b = min(pos_ints)
    else:
        b = None
        
    if neg_ints:
        a = max(neg_ints)
    else:
        a = None
    
    return (a, b)
