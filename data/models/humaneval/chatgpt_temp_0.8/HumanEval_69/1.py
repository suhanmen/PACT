def search(lst):
    max_val = -1
    for val in lst:
        if val > 0 and lst.count(val) >= val:
            if val > max_val:
                max_val = val
    return max_val
