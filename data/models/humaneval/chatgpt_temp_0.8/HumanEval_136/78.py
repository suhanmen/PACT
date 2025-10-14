def largest_smallest_integers(lst):
    pos_lst = [num for num in lst if num > 0]
    neg_lst = [num for num in lst if num < 0]
    
    if len(pos_lst) == 0:
        b = None
    else:
        b = min(pos_lst)
        
    if len(neg_lst) == 0:
        a = None
    else:
        a = max(neg_lst)
        
    return (a, b)
