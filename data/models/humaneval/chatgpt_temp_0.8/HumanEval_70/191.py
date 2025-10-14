def strange_sort_list(lst):
    sorted_list = []
    while lst:
        min_val = min(lst)
        max_val = max(lst)
        lst.remove(min_val)
        if min_val == max_val:
            sorted_list.append(min_val)
            break
        lst.remove(max_val)
        sorted_list.extend([min_val, max_val])
    return sorted_list
