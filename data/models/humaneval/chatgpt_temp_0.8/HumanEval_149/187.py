def sorted_list_sum(lst):
    # Delete strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]

    # Sort the list by length, then alphabetically
    lst.sort(key=lambda x: (len(x), x))

    return lst
