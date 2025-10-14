def strange_sort_list(lst):
    sorted_list = []
    while lst:
        minimum = min(lst)
        maximum = max(lst)
        sorted_list.append(minimum)
        if minimum != maximum:
            sorted_list.append(maximum)
        lst.remove(minimum)
        if minimum != maximum:
            lst.remove(maximum)
    return sorted_list
