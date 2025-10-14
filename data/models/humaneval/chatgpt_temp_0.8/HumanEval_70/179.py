python
def strange_sort_list(lst):
    strange_sorted = []
    lst.sort()
    while len(lst) > 0:
        strange_sorted.append(lst.pop(0))
        if len(lst) > 0:
            strange_sorted.append(lst.pop())
    return strange_sorted
