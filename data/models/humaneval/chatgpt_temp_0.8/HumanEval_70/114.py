def strange_sort_list(lst):
    result = []
    lst = sorted(lst)
    while lst:
        result.append(lst.pop(0))
        if lst:
            result.append(lst.pop())
    return result
