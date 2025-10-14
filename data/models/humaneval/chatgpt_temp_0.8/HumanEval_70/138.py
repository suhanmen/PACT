def strange_sort_list(lst):
    result = []
    while len(lst) > 0:
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)
        if len(lst) > 0:
            max_val = max(lst)
            result.append(max_val)
            lst.remove(max_val)
    return result
