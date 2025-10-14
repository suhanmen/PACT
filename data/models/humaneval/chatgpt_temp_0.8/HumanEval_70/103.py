def strange_sort_list(lst):
    sorted_lst = []
    while lst:
        # Find minimum and add to sorted list
        min_val = min(lst)
        sorted_lst.append(min_val)
        lst.remove(min_val)
        # If list is empty, break out of loop
        if not lst:
            break
        # Find maximum and add to sorted list
        max_val = max(lst)
        sorted_lst.append(max_val)
        lst.remove(max_val)
    return sorted_lst
