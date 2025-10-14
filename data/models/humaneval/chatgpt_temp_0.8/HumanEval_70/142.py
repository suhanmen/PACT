def strange_sort_list(lst):
    result = []
    while lst:
        min_val, max_val = min(lst), max(lst)
        result.append(min_val)
        if min_val != max_val:
            result.append(max_val)
        lst.remove(min_val)
        lst.remove(max_val)
    return result
