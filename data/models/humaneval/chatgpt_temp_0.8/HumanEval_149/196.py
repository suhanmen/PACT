def sorted_list_sum(lst):
    # Filter out words with odd length
    lst = list(filter(lambda x: len(x) % 2 == 0, lst))

    # Sort the list by ascending length and then alphabetically
    lst.sort(key=lambda x: (len(x), x))

    return lst
