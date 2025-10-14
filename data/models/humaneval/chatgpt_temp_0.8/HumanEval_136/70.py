def largest_smallest_integers(lst):
    neg_ints = [i for i in lst if i < 0] # extract negative integers
    pos_ints = [i for i in lst if i > 0] # extract positive integers
    max_neg = max(neg_ints) if neg_ints else None # find largest negative integer
    min_pos = min(pos_ints) if pos_ints else None # find smallest positive integer
    return (max_neg, min_pos) # return as tuple
