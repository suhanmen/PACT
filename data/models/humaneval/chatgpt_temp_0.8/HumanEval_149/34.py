def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    lst = [s for s in lst if len(s) % 2 == 0]
    # Sort the list by length first, then alphabetically
    lst = sorted(lst, key=lambda s: (len(s), s))
    return lst
