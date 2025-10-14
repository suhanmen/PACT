def next_smallest(lst):
    if len(lst) < 2:
        return None
    smallest = min(lst)
    lst.remove(smallest)
    second_smallest = min(lst)
    return second_smallest
