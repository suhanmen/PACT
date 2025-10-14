def sorted_list_sum(lst):
    # Delete strings with odd lengths
    lst = [string for string in lst if len(string) % 2 == 0]

    # Sort the list by length, then alphabetically
    lst = sorted(lst, key=lambda x: (len(x), x))

    return lst
