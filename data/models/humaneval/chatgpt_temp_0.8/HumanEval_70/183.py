def strange_sort_list(lst):
    sorted_lst = []
    while lst:
        minimum = min(lst)
        maximum = max(lst)
        sorted_lst.append(minimum)
        if minimum != maximum:
            sorted_lst.append(maximum)
        lst.remove(minimum)
        if minimum != maximum:
            lst.remove(maximum)
    return sorted_lst
