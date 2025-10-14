def strange_sort_list(lst):
    result = []
    while lst:
        # Add minimum value to result
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)
        # Add maximum value to result, if any
        if lst:
            max_val = max(lst)
            result.append(max_val)
            lst.remove(max_val)
    return result
