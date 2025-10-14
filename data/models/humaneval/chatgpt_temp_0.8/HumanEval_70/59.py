def strange_sort_list(lst):
    result = []
    lst = sorted(lst)
    while len(lst) > 0:
        result.append(lst.pop(0))
        if len(lst) > 0:
            result.append(lst.pop(-1))
    return result
