python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    sorted_list = sorted(set(lst))
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
