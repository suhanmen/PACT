def strange_sort_list(lst):
    sorted_lst = []
    while lst:
        # find the minimum value in the list
        min_val = min(lst)
        sorted_lst.append(min_val)
        lst.remove(min_val)
        # if there are still values in the list, find the maximum value
        if lst:
            max_val = max(lst)
            sorted_lst.append(max_val)
            lst.remove(max_val)
    return sorted_lst
