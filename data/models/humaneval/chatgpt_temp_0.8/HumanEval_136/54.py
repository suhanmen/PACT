def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0]
    pos_ints = [i for i in lst if i > 0]
    
    a = max(neg_ints) if neg_ints else None
    b = min(pos_ints) if pos_ints else None
    
    return (a, b)
