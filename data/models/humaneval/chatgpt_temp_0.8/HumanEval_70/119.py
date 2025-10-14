def strange_sort_list(lst):
    sorted_lst = []
    while lst:
        min_val = min(lst)
        max_val = max(lst)
        sorted_lst.append(min_val)
        if min_val != max_val:
            sorted_lst.append(max_val)
        lst.remove(min_val)
        if min_val != max_val:
            lst.remove(max_val)
    return sorted_lst
