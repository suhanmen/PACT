def sorted_list_sum(lst):
    # remove odd-length strings
    lst = [string for string in lst if len(string) % 2 == 0]
    # sort by length, then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
