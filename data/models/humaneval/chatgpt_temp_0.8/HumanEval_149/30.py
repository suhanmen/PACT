def sorted_list_sum(lst):
    # filter out strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    # sort the list by length and then alphabetically
    lst = sorted(lst, key=lambda x: (len(x), x))
    return lst
