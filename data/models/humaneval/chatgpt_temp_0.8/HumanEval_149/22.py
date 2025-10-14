def sorted_list_sum(lst):
    # remove strings with odd lengths from list
    lst = [word for word in lst if len(word) % 2 == 0]
    # sort by length, then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
