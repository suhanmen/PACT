def search(lst):
    unique_lst = list(set(lst))
    max_val = -1
    
    for val in unique_lst:
        if lst.count(val) >= val and val > 0:
            max_val = max(max_val, val)
    
    return max_val
