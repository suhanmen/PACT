python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        # Remove duplicates and sort list
        sorted_lst = sorted(set(lst))
        if len(sorted_lst) < 2:
            return None
        else:
            return sorted_lst[1]
