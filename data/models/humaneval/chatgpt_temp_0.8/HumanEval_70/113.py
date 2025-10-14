def strange_sort_list(lst):
    result = []
    while lst:
        # find minimum value
        min_val = min(lst)
        result.append(min_val)
        lst.remove(min_val)
        # check if there are remaining values
        if lst:
            # find maximum value
            max_val = max(lst)
            result.append(max_val)
            lst.remove(max_val)
    return result
