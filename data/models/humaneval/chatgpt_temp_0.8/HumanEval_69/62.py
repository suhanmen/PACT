def search(lst):
    max_val = -1
    for val in set(lst):
        if val > 0 and lst.count(val) >= val:
            max_val = max(max_val, val)
    return max_val
