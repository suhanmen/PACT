def sorted_list_sum(lst):
    # remove strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    # sort the list by ascending length and then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
