def strange_sort_list(lst):
    sorted_lst = []
    lst.sort()
    while len(lst) > 0:
        if len(lst) == 1:
            sorted_lst.append(lst.pop())
        else:
            sorted_lst.append(lst.pop(0))
            sorted_lst.append(lst.pop())
    return sorted_lst
