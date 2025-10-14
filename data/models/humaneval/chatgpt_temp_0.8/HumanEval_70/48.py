def strange_sort_list(lst):
    sorted_lst = []
    while len(lst) > 0:
        sorted_lst.append(min(lst))
        lst.remove(min(lst))
        if len(lst) > 0:
            sorted_lst.append(max(lst))
            lst.remove(max(lst))
    return sorted_lst
