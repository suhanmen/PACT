def strange_sort_list(lst):
    sorted_lst = []
    lst.sort()
    while lst:
        sorted_lst.append(lst.pop(0))
        if lst:
            sorted_lst.append(lst.pop(-1))
    return sorted_lst
