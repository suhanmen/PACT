def strange_sort_list(lst):
    result = []
    lst.sort()
    while len(lst) > 0:
        result.append(lst.pop(0))
        if len(lst) > 0:
            result.append(lst.pop())
    return result
