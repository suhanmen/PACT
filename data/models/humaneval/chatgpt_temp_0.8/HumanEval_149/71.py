def sorted_list_sum(lst):
    # Delete strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    # Sort the list by ascending length, then alphabetically
    lst = sorted(lst, key=lambda x: (len(x), x))
    return lst
