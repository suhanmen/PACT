def largest_smallest_integers(lst):
    neg_integers = [n for n in lst if n < 0] # get all negative integers
    pos_integers = [n for n in lst if n > 0] # get all positive integers
    
    # if there are no negative or positive integers, return None
    if not neg_integers:
        max_neg = None
    else:
        max_neg = max(neg_integers) # get the largest negative integer
        
    if not pos_integers:
        min_pos = None
    else:
        min_pos = min(pos_integers) # get the smallest positive integer
        
    return (max_neg, min_pos)
