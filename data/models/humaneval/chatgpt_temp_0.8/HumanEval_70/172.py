def strange_sort_list(lst):
    result = []

    while lst:
        # get minimum value
        min_val = min(lst)
        lst.remove(min_val)
        result.append(min_val)

        if lst:
            # get maximum of the remaining integers
            max_val = max(lst)
            lst.remove(max_val)
            result.append(max_val)

    return result
