python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst = list(set(lst)) # remove duplicates
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]
