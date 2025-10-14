def sorted_list_sum(lst):
    # remove strings with odd lengths
    lst = [string for string in lst if len(string) % 2 == 0]
    # sort list by length and then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
