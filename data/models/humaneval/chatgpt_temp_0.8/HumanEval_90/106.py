def next_smallest(lst):
    if len(lst) < 2 or len(set(lst)) < 2:
        return None

    sorted_list = sorted(set(lst))
    return sorted_list[1]
