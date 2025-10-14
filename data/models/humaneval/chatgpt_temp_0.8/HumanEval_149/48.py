def sorted_list_sum(lst):
    # remove strings with odd length
    lst = [word for word in lst if len(word) % 2 == 0]
    # sort list by ascending length, then alphabetically
    lst = sorted(lst, key=lambda word: (len(word), word))
    return lst
