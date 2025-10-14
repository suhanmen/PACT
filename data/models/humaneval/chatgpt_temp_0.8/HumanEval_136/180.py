def largest_smallest_integers(lst):
    neg_integers = [i for i in lst if i < 0]
    pos_integers = [i for i in lst if i > 0]
    
    if not neg_integers:
        largest = None
    else:
        largest = max(neg_integers)
    
    if not pos_integers:
        smallest = None
    else:
        smallest = min(pos_integers)
    
    return (largest, smallest)
