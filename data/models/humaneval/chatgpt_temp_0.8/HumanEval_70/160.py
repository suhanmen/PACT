python
def strange_sort_list(lst):
    sorted_lst = []
    lst_copy = lst.copy()
    while len(lst_copy) > 0:
        sorted_lst.append(min(lst_copy))
        lst_copy.remove(min(lst_copy))
        if len(lst_copy) > 0:
            sorted_lst.append(max(lst_copy))
            lst_copy.remove(max(lst_copy))
    return sorted_lst
