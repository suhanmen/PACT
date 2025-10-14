def strange_sort_list(lst):
    res = []
    while lst:
        minimum = min(lst)
        maximum = max(lst)
        res.append(minimum)
        if minimum != maximum:
            res.append(maximum)
        lst.remove(minimum)
        if minimum != maximum:
            lst.remove(maximum)
    return res
