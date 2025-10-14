def strange_sort_list(lst):
    result = []
    lst_sorted = sorted(lst)
    while lst_sorted:
        result.append(lst_sorted.pop(0))
        if lst_sorted:
            result.append(lst_sorted.pop())
    return result
